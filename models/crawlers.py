import logging
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from constants import constants
from helpers.utils import remove_special_symbols_from_string, is_cnj_format_valid, find_court_from_cnj_by_regex


class Crawler:

    def __init__(self, cnj: str):
        self.cnj = cnj

    def __str__(self):
        return f'{self.__class__.__name__}__{self.unmask_cnj}'

    @property
    def unmask_cnj(self):
        return self.cnj.replace('-', '').replace('.', '')

    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def court_code(self) -> str:
        pass

    @abstractmethod
    def extract(self) -> dict:
        pass

    def __get_page__(self, url: str) -> object or None:
        # TODO: buscar entender como tornar essa parte assíncrona
        try:
            request = requests.get(url)
        except requests.RequestException:
            return None
        return BeautifulSoup(request.text, 'html.parser')

    def get_body(self, url: str) -> object or None:
        soup: object = self.__get_page__(url)
        if soup is not None:
            return soup.body
        return None


class TjalFirstInstance(Crawler):

    def url(self) -> str:
        return f'https://www2.tjal.jus.br/cpopg/show.do?processo.numero={self.cnj}'

    def court_code(self) -> str:
        return constants.TJAL_CODE

    def extract(self):
        if not is_cnj_format_valid(self.cnj):
            logging.error('Formato de CNJ inválido!')
            # TODO: Na chamada da API, essa condicional deve retornar uma response de erro
            # TODO: Caso inválido, mostrar mensagem de erro ainda no campo do form do front-end

        logging.info('Formato de CNJ válido!')
        if find_court_from_cnj_by_regex(self.cnj, self.court_code()):
            logging.info('Iniciando crawler para busca de 1ª instância no TJAL...')

            body = self.get_body(self.url())

            main_section = body.find_all('div', {'id': 'containerDadosPrincipaisProcesso'})

            result = dict(
                principal=dict(
                    classe=None,
                    assunto=None,
                    juiz=None
                ),
                detalhes=dict(
                    area=None,
                    dataHoraDistribuicao=None,
                    valorAcao=None
                ),
                partesProcesso=dict()
            )

            for div_id in main_section:
                result.get('principal')['classe'] = div_id.find(
                    'span', {'id': 'classeProcesso'}
                ).text.strip()
                result.get('principal')['assunto'] = div_id.find(
                    'span', {'id': 'assuntoProcesso'}
                ).text.strip()
                result.get('principal')['juiz'] = div_id.find(
                    'span', {'id': 'juizProcesso'}
                ).text.strip()

            more_details_section = body.find_all('div', {'id': 'maisDetalhes'})

            for label in more_details_section:
                result.get('detalhes')['area'] = label.find(
                    'div', {'id': 'areaProcesso'}
                ).text.strip()
                result.get('detalhes')['dataHoraDistribuicao'] = label.find(
                    'div', {'id': 'dataHoraDistribuicaoProcesso'}
                ).text.strip()
                result.get('detalhes')['valorAcao'] = label.find(
                    'div',
                    {'id': 'valorAcaoProcesso'}
                ).text.strip()

            logging.info('Coletando informações das partes envolvidas no processo...')
            parts_section = body.find('table', {'id': 'tableTodasPartes'})

            parts_section_rows = parts_section.find_all('tr')

            for block in parts_section_rows:
                part_type = remove_special_symbols_from_string(block.find(class_='tipoDeParticipacao').text).lower()
                list_parts_process = block.find(class_='nomeParteEAdvogado').text.strip().split('\t \n')

                for element in list_parts_process:
                    part = remove_special_symbols_from_string(element.strip())
                    if not part:
                        continue
                    person_data = part.split(':')
                    person_data.reverse()  # garante que o nome do indivíduo esteja sempre no primeiro índice

                    if part_type not in result.get('partesProcesso').keys():
                        result.get('partesProcesso').update(
                            {
                                part_type: list()
                            }
                        )
                    result.get('partesProcesso').get(f'{part_type}').append(
                        (
                            person_data[0],
                            person_data[1] if len(person_data) > 1 else 'N/A'
                        )
                    )

            return result
