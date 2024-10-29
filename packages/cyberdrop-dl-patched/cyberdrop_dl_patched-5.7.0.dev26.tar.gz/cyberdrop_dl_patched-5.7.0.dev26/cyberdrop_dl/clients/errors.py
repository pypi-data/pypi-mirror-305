from typing import TYPE_CHECKING
from pathlib import Path
from yaml.constructor import ConstructorError

if TYPE_CHECKING:
    from cyberdrop_dl.scraper.crawler import ScrapeItem

class InvalidContentTypeFailure(Exception):
    """This error will be thrown when the content type isn't as expected"""

    def __init__(self, *, message: str = "Invalid content type"):
        self.message = message
        super().__init__(self.message)

class InvalidYamlConfig(Exception):
    """This error will be thrown when a yaml config file has invalid values"""

    def __init__(self, file: Path, e: ConstructorError):
        self.file = file
        mark = e.problem_mark if hasattr(e, 'problem_mark') else e
        self.message = f"ERROR: File '{file}' has an invalid config. Please verify and edit it manually\n {mark}"
        self.message_rich = self.message.replace("ERROR:", "[bold red]ERROR:[/bold red]")
        super().__init__(self.message)


class NoExtensionFailure(Exception):
    """This error will be thrown when no extension is given for a file"""

    def __init__(self, *, message: str = "Extension missing for file"):
        self.message = message
        super().__init__(self.message)


class PasswordProtected(Exception):
    """This error will be thrown when a file is password protected"""

    def __init__(self,/, scrape_item: 'ScrapeItem'):
        self.message = "File/Folder is password protected"
        self.scrape_item = scrape_item
        super().__init__(self.message)


class DDOSGuardFailure(Exception):
    """This error will be thrown when DDoS-Guard is detected"""

    def __init__(self, status: int, message: str = "DDoS-Guard detected"):
        self.status = status
        self.message = message
        super().__init__(self.message)
        super().__init__(self.status)


class DownloadFailure(Exception):
    """This error will be thrown when a request fails"""

    def __init__(self, status: int, message: str = "Something went wrong"):
        self.status = status
        self.message = message
        super().__init__(self.message)
        super().__init__(self.status)


class ScrapeFailure(Exception):
    """This error will be thrown when a request fails"""

    def __init__(self, status: int, message: str = "Something went wrong"):
        self.status = status
        self.message = message
        super().__init__(self.message)
        super().__init__(self.status)


class FailedLoginFailure(Exception):
    """This error will be thrown when the login fails for a site"""

    def __init__(self, *, status: int, message: str = "Failed login."):
        self.status = status
        self.message = message
        super().__init__(self.message)
        super().__init__(self.status)


class JDownloaderFailure(Exception):
    """Basic failure template for JDownloader"""

    def __init__(self, message: str = "Something went wrong"):
        self.message = message
        super().__init__(self.message)
