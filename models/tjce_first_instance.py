from constants import constants
from models.crawler_esaj_first_instance import CrawlerFirstInstanceEsaj


class TjceFirstInstance(CrawlerFirstInstanceEsaj):
    @property
    def court_code(self) -> str:
        return constants.TJCE_CODE

    @property
    def url(self) -> str:
        return f"https://esaj.tjce.jus.br/cpopg/show.do"
