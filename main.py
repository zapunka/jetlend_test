import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs

SITE_URL = 'https://jetlend.ru/'


def main():
    page_content = requests.get(SITE_URL)
    page_content.raise_for_status()

    parsed_content = bs(page_content.text, features='html.parser')
    with_attributes_count = 0
    result_by_tags = {}
    for tag in parsed_content.findAll():
        if result_by_tags.get(tag.name):
            result_by_tags[tag.name] += 1
        else:
            result_by_tags[tag.name] = 1

        if tag.attrs:
            with_attributes_count += 1

    print(f'total tags count = {len(parsed_content.findAll())}')
    for tag_name in result_by_tags:
        print(f'{tag_name}: {result_by_tags[tag_name]}')
    print(f'total with attributes = {with_attributes_count}')


if __name__ == '__main__':
    try:
        main()
    except HTTPError as ex:
        print(f'Exception was occurred while fetching url {SITE_URL}, ex: {ex}')
