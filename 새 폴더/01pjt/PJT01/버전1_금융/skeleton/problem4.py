import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다


def get_deposit_products():
  api_key = "92a203c358e35b6c17bb43c760f73b89"
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

  result = requests.get(url).json() # 1. 응답을 json 형식으로 변환합니다.
  key_list = result['result'] # 2. key 값이 "result" 인 데이터를 변수에 저장합니다

# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다
  base_list = key_list['baseList'] 

# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
  option_list = key_list['optionList']
  
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 fin_prdt_nm
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다. fin_prdt_cd
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.

  for key1 in base_list:
     for key2 in option_list:
        if key1['fin_prdt_cd'] == key2['fin_prdt_cd']:
            new_dict = {'저축금리': key2['intr_rate'],'저축 기간':key2['save_trm'],'저축금리유형':key2['intr_rate_type'],
                        '저축금리유형명' : key2['intr_rate_type_nm'],'최고 우대금리':key2['intr_rate2']}
  

# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.

  result_list = {'금리정보': [new_dict]}
  for key3 in base_list:
    result_list['금융상품명']=key3['fin_prdt_nm']
    result_list['금융회사명']=key3['kor_co_nm']

  return [result_list]
       
        
  # fin_prdt_nm	금융 상품명
  # kor_co_nm	금융회사 명


  # for dicts in option_list:
  #    dict_1 = {}
  #    dict_1['저축 금리'] = dicts['intr_rate']
  #    dict_1['저축 기간'] = dicts['save_trm']
  #    dict_1['저축금리유형'] = dicts['intr_rate_type']
  #    dict_1['저축금리유형명'] = dicts['intr_rate_type_nm']
  #    dict_1['최고 우대금리'] = dicts['intr_rate2']
  #    print(dict_1)

  # return dicts
  


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)