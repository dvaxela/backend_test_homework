from pprint import pprint

import requests
import xmltodict


def parse_tickers_list():
    url_ru_stock = 'https://iss.moex.com/iss/statistics/engines/stock/quotedsecurities'
    response_xml = requests.get(url=url_ru_stock)
    response_json = xmltodict.parse(response_xml.content)
    tickers_value_list = response_json['document']['data'][0]['rows']['row']
    ticker_dict = {}
    for i in range(0,len(tickers_value_list)):
        ticker = tickers_value_list[i]['@SECID']
        ticker_dict[f'{ticker}'] = tickers_value_list[i]['@NAME']
    pprint(ticker_dict)
    print(tickers_value_list[0])
    

parse_tickers_list()
