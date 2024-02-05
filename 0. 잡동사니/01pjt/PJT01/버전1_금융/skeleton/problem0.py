import pprint
import requests

def get_deposit_products():
    api_key = '97c2b63c0e9118c93a466f1430d8dc69'

    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
    response = requests.get(url, params=params).json()
    return response



if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    
    print(type(result))
    print(result.keys())
    print(result["result"])
    
    # prrint.prrint(): json을 보기 좋은 형식으로 출력
    # pprint.pprint(result)
