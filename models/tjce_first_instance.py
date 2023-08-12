from constants import constants
from mocks.mocks import create_bs4_object_from_tjce
from models.crawler_esaj import CrawlerEsaj


class TjceFirstInstance(CrawlerEsaj):
    def __init__(self, base_url: str, cnj: str):
        super().__init__(base_url, cnj)
        self._body = create_bs4_object_from_tjce().body

    @property
    def court_code(self) -> str:
        return constants.TJCE_CODE

    @property
    def url(self) -> str:
        return f"https://esaj.tjce.jus.br/cpopg/open.do?processo.numero={self.cnj}"
