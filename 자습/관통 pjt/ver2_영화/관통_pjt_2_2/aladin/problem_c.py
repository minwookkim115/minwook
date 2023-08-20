import requests
from pprint import pprint


def bestseller_book():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': 'ttbminwookkim1151611001',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }
    
    # response = requests.get(URL, params=params)
    # response = response.json()
    
    response = requests.get(URL, params=params).json()
    response = response['item']

    salespoint_list = []
    for i in response:
        salespoint_list.append(i["salesPoint"])

    five_salespoint_list = sorted(salespoint_list, reverse=True)[0:5]

    five_rank_list = []
    for i in five_salespoint_list:
        for j in response:
            if i == j["salesPoint"]:
                five_rank_list.append(j["title"])
                
    return five_rank_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

