import requests
from bs4 import BeautifulSoup


def parser(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    charcode_un = soup.find_all("charcode")
    value_un = soup.find_all("value")
    charcode = []
    value = []
    for item in charcode_un:
        charcode.append(item.text)
    for i in value_un:
        value.append(i.text)
    charcode_value = dict(zip(charcode, value))
    print(f'Курс доллара: {charcode_value.setdefault("USD")}')
    print(f'Курс евро: {charcode_value.setdefault("EUR")}')

def main():
    parser("http://www.cbr.ru/scripts/XML_daily.asp")


if __name__ == '__main__':
    main()
