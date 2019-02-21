import requests
from OLXParser import OLXParser
from CSVModule import CSVModule
from OtoDomParser import OtoDomParser


def main():
    olx_page = requests.get('https://www.olx.pl/nieruchomosci/mieszkania/wroclaw')
    oto_dom_page = requests.get('https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw')
    parsers = [
        OLXParser(olx_page.content),
        OtoDomParser(oto_dom_page.content),
    ]

    for parser in parsers:
        parser.collect_flats_info()
        flats = parser.get_flats_info()
        csv_module = CSVModule(flats, './data/flats_info.csv')
        csv_module.save_flats_to_file()


if __name__ == '__main__':
    main()


