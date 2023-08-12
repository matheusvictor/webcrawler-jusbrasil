import logging

from helpers.utils import save_json_file
from models.crawlers import TjalFirstInstance, TjceFirstInstance

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')


def main():
    crawler_tjal = TjalFirstInstance('0017486-52.2009.8.02.0001')
    result_tjal = crawler_tjal.extract()
    save_json_file(result_tjal, f'{str(crawler_tjal)}.json')

    crawler_tjce = TjceFirstInstance('0200599-25.2022.8.06.0071')
    # 0200599-25.2022.8.06.0071
    result_tjce = crawler_tjce.extract()
    save_json_file(result_tjce, f'{str(crawler_tjce)}.json')


if __name__ == '__main__':
    main()
