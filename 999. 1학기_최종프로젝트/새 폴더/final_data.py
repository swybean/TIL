import requests
import json

API_KEY = '64695226b53683160cd45e55e7453b18'

# 장르 ID와 한글 장르명 매핑
genre_mapping = {
    28: '액션',
    12: '모험',
    16: '애니메이션',
    35: '코미디',
    80: '범죄',
    99: '다큐멘터리',
    18: '드라마',
    10751: '가족',
    14: '판타지',
    36: '역사',
    27: '공포',
    10402: '음악',
    9648: '미스터리',
    10749: '로맨스',
    878: 'SF',
    10770: 'TV 영화',
    53: '스릴러',
    10752: '전쟁',
    37: '서부'
}

# 1 ~ 50 페이지 top_rate 영화 출력
for n in range(1, 51):
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko&region=KR&page={n}'
    response = requests.get(url)
    data = response.json()['results']
    real = {}

    # 'results' 값에서 id를 이용해 어떤 ott에 있는지 확인
    for a in data:
        if 'id' in a:
            a['movie_id'] = a.pop('id')

        real['model'] = ''
        real['pk'] = a['movie_id']
        real['fields'] = {}
        real['fields']['casts'] = []

        url1 = f"https://api.themoviedb.org/3/movie/{a['movie_id']}/watch/providers?api_key={API_KEY}&language=ko&region=KR"
        response1 = requests.get(url1)
        data1 = response1.json()
        url2 = f"https://api.themoviedb.org/3/movie/{a['movie_id']}/credits?api_key={API_KEY}&language=ko&region=KR"
        response2 = requests.get(url2)
        data2 = response2.json()
        for actor in data2['cast']:
            real['fields']['casts'].append(actor['name'])
            if len(real['fields']['casts']) == 5:
                break

        if 'KR' in data1['results']:
            if 'flatrate' in data1['results']['KR']:
                for b in data1['results']['KR']['flatrate']:
                    if b['provider_id'] == 8:
                        real['model'] = 'movies.Netflix'
                        real['fields']["genres"] = [genre_mapping.get(genre_id, '') for genre_id in a["genre_ids"]]
                        real['fields']["overview"] = a["overview"]
                        real['fields']["popularity"] = a["popularity"]
                        real['fields']["release_date"] = a["release_date"]
                        real['fields']["title"] = a["title"]
                        real['fields']["vote_average"] = a["vote_average"]
                        real['fields']["vote_count"] = a["vote_count"]
                        real['fields']["poster_path"] = a["poster_path"]
                        if 'provider_id' in real['fields']:
                            real['fields']['provider_id'].append(8)
                        else:
                            real['fields']['provider_id'] = [8]
                        with open('netflix.json', 'a', encoding='utf-8') as f:
                            json.dump(real, f, ensure_ascii=False, indent=4)
                            f.write(',')
                            f.write('\n')
                    if b['provider_id'] == 337:
                        real['model'] = 'movies.Disney'
                        real['fields']["genres"] = [genre_mapping.get(genre_id, '') for genre_id in a["genre_ids"]]
                        real['fields']["overview"] = a["overview"]
                        real['fields']["popularity"] = a["popularity"]
                        real['fields']["release_date"] = a["release_date"]
                        real['fields']["title"] = a["title"]
                        real['fields']["vote_average"] = a["vote_average"]
                        real['fields']["vote_count"] = a["vote_count"]
                        real['fields']["poster_path"] = a["poster_path"]
                        if 'provider_id' in real['fields']:
                            real['fields']['provider_id'].append(337)
                        else:
                            real['fields']['provider_id'] = [337]
                        with open('disney.json', 'a', encoding='utf-8') as f:
                            json.dump(real, f, ensure_ascii=False, indent=4)
                            f.write(',')
                            f.write('\n')
                    if b['provider_id'] == 97:
                        real['model'] = 'movies.Watcha'
                        real['fields']["genres"] = [genre_mapping.get(genre_id, '') for genre_id in a["genre_ids"]]
                        real['fields']["overview"] = a["overview"]
                        real['fields']["popularity"] = a["popularity"]
                        real['fields']["release_date"] = a["release_date"]
                        real['fields']["title"] = a["title"]
                        real['fields']["vote_average"] = a["vote_average"]
                        real['fields']["vote_count"] = a["vote_count"]
                        real['fields']["poster_path"] = a["poster_path"]
                        if 'provider_id' in real['fields']:
                            real['fields']['provider_id'].append(97)
                        else:
                            real['fields']['provider_id'] = [97]
                        with open('watcha.json', 'a', encoding='utf-8') as f:
                            json.dump(real, f, ensure_ascii=False, indent=4)
                            f.write(',')
                            f.write('\n')
