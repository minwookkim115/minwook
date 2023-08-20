import json
from pprint import pprint



def book_info(book):
    # 여기에 코드를 작성합니다.  
    book = open("data/book.json", mode="r", encoding="utf-8")
    book_detail = json.load(book)

    new_dict = {
        "id": book_detail.get("id"),
        "title": book_detail.get("title"),
        "author": book_detail.get("author"),
        "priceSales": book_detail.get("priceSales"),
        "description": book_detail.get("description"),
        "cover": book_detail.get("cover"),
        "categoryId": book_detail.get("categoryId")
    }

    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
