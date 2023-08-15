from constants import constants
from models.crawler_esaj_second_instance import CrawlerSecondInstanceEsaj


class TjalSecondInstance(CrawlerSecondInstanceEsaj):
    def court_code(self) -> str:
        return constants.TJAL_CODE

    @property
    def url(self) -> str:
        return f"https://www2.tjal.jus.br/cposg5/open.do"
