import logging

from helpers.utils import save_json_file
from models.crawlers import TjalFirstInstance

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')


def main():
    crawler = TjalFirstInstance('0710802-55.2018.8.02.0001')
    result = crawler.extract()
    save_json_file(result, f'{str(crawler)}.json')


if __name__ == '__main__':
    main()
