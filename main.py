import logging

from constants import constants
from helpers.utils import (find_court_from_cnj_by_regex,
                           is_cnj_format_valid)
from models.models import CrawlerTJCE, CrawlerTJAL

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')


def main():
    # cnj = '0070337-91.2008.8.06.0001'
    cnj = '0070337-91.2008.8.02.0001'

    if not is_cnj_format_valid(cnj):
        logging.error('Formato de CNJ inválido!')
        # TODO: Na chamada da API, essa condicional deve retornar uma response de erro

    logging.info('Formato de CNJ válido!')
    if find_court_from_cnj_by_regex(cnj, constants.TJAL_CODE):
        logging.info('Iniciando crawler para busca de 1ª instância no TJAL...')
        crawler_tjal = CrawlerTJAL()

        body = crawler_tjal.get_body(
            url=f'https://www2.tjal.jus.br/cpopg/show.do?processo.numero=0710802-55.2018.8.02.0001',
        )

        crawler_tjal.get_all_div_from_page(body)
        # print(crawler_tjal.get_more_details(body))

        print(crawler_tjal.get_tags_from_page_by_properties(body, 'div', {'class': 'unj-entity-header__details'}))

        # body = crawler_tjal.get_body_for_first_instance_page(
        #     url=f'https://www2.tjal.jus.br/cpopg/show.do?processo.numero=0710802-55.2018.8.02.0001',
        #     tag='div',
        #     properties={'id': 'containerDadosPrincipaisProcesso'}
        # )
        # print(body)

    elif find_court_from_cnj_by_regex(cnj, constants.TJCE_CODE):
        crawler_tjce = CrawlerTJCE()
        body = crawler_tjce.get_div_by_id(
            url='https://esaj.tjce.jus.br/cpopg/show.do?processo.numero=0070337-91.2008.8.06.0001',
            tag='div',
            properties={'id': 'containerDadosPrincipaisProcesso'}
        )
        print(body)
    else:
        logging.info('Tribunal desconhecido. Encerrando o crawler.')
        exit(1)


if __name__ == '__main__':
    main()
