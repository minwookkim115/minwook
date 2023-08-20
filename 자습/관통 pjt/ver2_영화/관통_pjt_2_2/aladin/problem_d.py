import requests
from pprint import pprint


def author_other_works(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': 'ttbminwookkim1151611001',
        'Query': f"{title}",
        'QueryType': 'Title',
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

    for i in list(response[0]["author"]):
        if i == "(":
            i_author = "".join(list(response[0]["author"])[0:list(response[0]["author"]).index(i)-1])

    for i in response:
        for j in list(response[i]["author"]):
            if j =="(":
                j_author = "".join(list(response[i]["author"])[0:list(response[i]["author"]).index(j)-1])

    author_other_list = []
    for  in j_author
        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    # pprint(author_other_works('개미'))

    # pprint(author_other_works('*'))
