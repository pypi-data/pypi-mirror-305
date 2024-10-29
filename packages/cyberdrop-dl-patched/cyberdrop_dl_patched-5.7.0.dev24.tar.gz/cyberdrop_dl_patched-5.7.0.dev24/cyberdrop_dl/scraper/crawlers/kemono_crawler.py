from __future__ import annotations

import calendar
import datetime
import re
from typing import TYPE_CHECKING, Tuple, Dict, Optional

from aiolimiter import AsyncLimiter
from yarl import URL
from aiohttp import ClientResponse

from cyberdrop_dl.clients.errors import NoExtensionFailure
from cyberdrop_dl.scraper.crawler import Crawler
from cyberdrop_dl.utils.dataclasses.url_objects import ScrapeItem
from cyberdrop_dl.utils.utilities import get_filename_and_ext, error_handling_wrapper

if TYPE_CHECKING:
    from cyberdrop_dl.managers.manager import Manager


class KemonoCrawler(Crawler):
    def __init__(self, manager: Manager):
        super().__init__(manager, "kemono", "Kemono")
        self.primary_base_domain = URL("https://kemono.su")
        self.api_url = URL("https://kemono.su/api/v1")
        self.services = ['patreon', 'fanbox', 'fantia', 'afdian', 'boosty', 'dlsite', 'gumroad', 'subscribestar']
        self.request_limiter = AsyncLimiter(10, 1)

        self.maximum_offset = None

    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    async def check_last_page(self, response: ClientResponse) -> bool:
        """Checks if the response is the last page"""
        current_offset = int(response.url.query.get("o", 0))
        return current_offset != self.maximum_offset

    async def fetch(self, scrape_item: ScrapeItem) -> None:
        """Determines where to send the scrape item based on the url"""
        task_id = await self.scraping_progress.add_task(scrape_item.url)

        if "thumbnails" in scrape_item.url.parts:
            parts = [x for x in scrape_item.url.parts if x not in ("thumbnail", "/")]
            link = URL(f"https://{scrape_item.url.host}/{'/'.join(parts)}")
            scrape_item.url = link
            await self.handle_direct_link(scrape_item)
        elif "discord" in scrape_item.url.parts:
            await self.discord(scrape_item)
        elif "post" in scrape_item.url.parts:
            await self.post(scrape_item)
        elif any(x in scrape_item.url.parts for x in self.services):
            await self.profile(scrape_item)
        else:
            await self.handle_direct_link(scrape_item)

        await self.scraping_progress.remove_task(task_id)

    @error_handling_wrapper
    async def profile(self, scrape_item: ScrapeItem) -> None:
        """Scrapes a profile"""
        offset = 0
        service, user = await self.get_service_and_user(scrape_item)
        user_str = await self.get_user_str_from_profile(scrape_item)
        api_call = self.api_url / service / "user" / user
        while True:
            async with self.request_limiter:
                JSON_Resp = await self.client.get_json(self.domain, api_call.with_query({"o": offset}))
                offset += 50
                if not JSON_Resp:
                    break

            for post in JSON_Resp:
                await self.handle_post_content(scrape_item, post, user, user_str)

    @error_handling_wrapper
    async def discord(self, scrape_item: ScrapeItem) -> None:
        """Scrapes a profile"""
        offset, maximum_offset = await self.get_offsets(scrape_item)
        channel = scrape_item.url.raw_fragment
        api_call = self.api_url / "discord/channel" / channel
        while offset <= maximum_offset:
            async with self.request_limiter:
                JSON_Resp = await self.client.get_json(self.domain, api_call.with_query({"o": offset}))
                offset += 150
                if not JSON_Resp:
                    break

            for post in JSON_Resp:
                await self.handle_post_content(scrape_item, post, channel, channel)

    @error_handling_wrapper
    async def post(self, scrape_item: ScrapeItem) -> None:
        """Scrapes a post"""
        service, user, post_id = await self.get_service_user_and_post(scrape_item)
        user_str = await self.get_user_str_from_post(scrape_item)
        api_call = self.api_url / service / "user" / user / "post" / post_id
        async with self.request_limiter:
            post = await self.client.get_json(self.domain, api_call)
        await self.handle_post_content(scrape_item, post, user, user_str)

    @error_handling_wrapper
    async def handle_post_content(self, scrape_item: ScrapeItem, post: Dict, user: str, user_str: str) -> None:
        """Handles the content of a post"""
        date = post["published"].replace("T", " ")
        post_id = post["id"]
        post_title = post.get("title", "")

        scrape_item.album_id = post_id 
        scrape_item.part_of_album = True

        await self.get_content_links(scrape_item, post, user_str)

        async def handle_file(file_obj):
            link = self.primary_base_domain / ("data" + file_obj['path'])
            link = link.with_query({"f": file_obj['name']})
            await self.create_new_scrape_item(link, scrape_item, user_str, post_title, post_id, date)

        if post.get('file'):
            await handle_file(post['file'])

        for file in post['attachments']:
            await handle_file(file)

    async def get_content_links(self, scrape_item: ScrapeItem, post: Dict, user: str) -> None:
        """Gets links out of content in post"""
        content = post.get("content", "")
        if not content:
            return

        date = post["published"].replace("T", " ")
        post_id = post["id"]
        title = post.get("title", "")

        post_title = None
        if self.manager.config_manager.settings_data['Download_Options']['separate_posts']:
            post_title = f"{date} - {title}"
            if self.manager.config_manager.settings_data['Download_Options']['include_album_id_in_folder_name']:
                post_title = post_id + " - " + post_title

        new_title = await self.create_title(user, None, None)
        scrape_item = await self.create_scrape_item(scrape_item, scrape_item.url, new_title, True, None,
                                                    await self.parse_datetime(date))
        await scrape_item.add_to_parent_title(post_title)
        await scrape_item.add_to_parent_title("Loose Files")

        yarl_links = []
        all_links = [x.group().replace(".md.", ".") for x in
                    re.finditer(r"(?:http.*?)(?=($|\n|\r\n|\r|\s|\"|\[/URL]|']\[|]\[|\[/img]|</a>|</p>))", content)]
        for link in all_links:
            yarl_links.append(URL(link))

        for link in yarl_links:
            if "kemono" in link.host:
                continue
            scrape_item = await self.create_scrape_item(scrape_item, link, "", add_parent = scrape_item.url.joinpath("post",post_id))
            await self.handle_external_links(scrape_item)

    @error_handling_wrapper
    async def handle_direct_link(self, scrape_item: ScrapeItem) -> None:
        """Handles a direct link"""
        try:
            filename, ext = await get_filename_and_ext(scrape_item.url.query["f"])
        except NoExtensionFailure:
            filename, ext = await get_filename_and_ext(scrape_item.url.name)
        await self.handle_file(scrape_item.url, scrape_item, filename, ext)

    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    async def parse_datetime(self, date: str) -> int:
        """Parses a datetime string into a unix timestamp"""
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        return calendar.timegm(date.timetuple())

    @error_handling_wrapper
    async def get_user_str_from_post(self, scrape_item: ScrapeItem) -> str:
        """Gets the user string from a scrape item"""
        async with self.request_limiter:
            soup = await self.client.get_BS4(self.domain, scrape_item.url)
        user = soup.select_one("a[class=post__user-name]").text
        return user

    @error_handling_wrapper
    async def get_user_str_from_profile(self, scrape_item: ScrapeItem) -> str:
        """Gets the user string from a scrape item"""
        async with self.request_limiter:
            soup = await self.client.get_BS4(self.domain, scrape_item.url)
        user = soup.select_one("span[itemprop=name]").text
        return user

    async def get_service_and_user(self, scrape_item: ScrapeItem) -> Tuple[str, str]:
        """Gets the service and user from a scrape item"""
        user = scrape_item.url.parts[3]
        service = scrape_item.url.parts[1]
        return service, user

    async def get_service_user_and_post(self, scrape_item: ScrapeItem) -> Tuple[str, str, str]:
        """Gets the service, user and post id from a scrape item"""
        user = scrape_item.url.parts[3]
        service = scrape_item.url.parts[1]
        post = scrape_item.url.parts[5]
        return service, user, post

    async def get_maximum_offset(self, scrape_item: ScrapeItem) -> int:
        """Gets the maximum offset for a scrape item"""
        soup = await self.client.get_BS4(self.domain, scrape_item.url)
        menu = soup.select_one("menu")
        if menu is None:
            self.maximum_offset = 0
            return 0
        pagination_links = menu.find_all("a", href=True)
        offsets = [int(x['href'].split('?o=')[-1]) for x in pagination_links]
        offset = max(offsets)
        self.maximum_offset = offset
        return offset

    async def get_offsets(self, scrape_item: ScrapeItem) -> int:
        """Gets the offset for a scrape item"""
        current_offset = int(scrape_item.url.query.get("o", 0))
        maximum_offset = await self.get_maximum_offset(scrape_item)
        return current_offset, maximum_offset

    async def create_new_scrape_item(self, link: URL, old_scrape_item: ScrapeItem, user: str, title: str, post_id: str,
                                    date: str, add_parent: Optional[URL] = None) -> None:
        """Creates a new scrape item with the same parent as the old scrape item"""
        post_title = None
        if self.manager.config_manager.settings_data['Download_Options']['separate_posts']:
            post_title = f"{date} - {title}"
            if self.manager.config_manager.settings_data['Download_Options']['include_album_id_in_folder_name']:
                post_title = post_id + " - " + post_title

        new_title = await self.create_title(user, None, None)
        new_scrape_item = await self.create_scrape_item(old_scrape_item, link, new_title, True, None,
                                                        await self.parse_datetime(date), add_parent = add_parent)
        await new_scrape_item.add_to_parent_title(post_title)
        self.manager.task_group.create_task(self.run(new_scrape_item))
