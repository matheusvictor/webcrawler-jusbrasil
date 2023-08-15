from constants import constants
from models.crawler_esaj_second_instance import CrawlerSecondInstanceEsaj


class TjceSecondInstance(CrawlerSecondInstanceEsaj):
    def court_code(self) -> str:
        return constants.TJCE_CODE

    @property
    def url(self) -> str:
        return f"https://esaj.tjce.jus.br/cposg5/open.do"
