import requests

from bs4 import BeautifulSoup


class Crawler:
    def __get_page__(self, url) -> object:
        request = requests.get(url)
        return BeautifulSoup(request.text, 'html.parser')

    def get_body(self, url: str):
        soup: object = self.__get_page__(url)
        if soup is not None:
            return soup.body

    def get_all_div_from_page(self):
        pass

    def get_body_for_first_instance_page(self, url: str, tag: str = 'div', properties=None):
        if properties is None:
            properties = {'id': 'containerDadosPrincipaisProcesso'}
        bs: object = self.__get_page__(url)
        if bs is not None:
            # print(bs.find_all('div'))
            print('-' * 20)
            return bs.find_all(tag, properties)
        return None

    def get_more_details(self, url: str, tag: str = 'div', properties=None):
        if properties is None:
            properties = {'id': 'unj-entity-header__details'}
        pass
