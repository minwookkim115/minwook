import requests
from pprint import pprint


def best_review_books():
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

    nine_point_book = []
    for i in response:
        if i["customerReviewRank"] >= 9:
            nine_point_book.append(i)

    return nine_point_book



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
