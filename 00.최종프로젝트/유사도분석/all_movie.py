import requests
import json

API_KEY = '7c11fe750835c7c0b4c2bb32573c709f'

# 중복된 영화를 확인하기 위한 set
seen_movies = set()

# OTT 정보를 저장할 파일
ott_file = 'allmovie.json'

# 장르 정보를 저장할 딕셔너리
genre_dict = {}

# 장르 정보 가져오기
def get_genre_name(genre_id):
    if genre_id in genre_dict:
        return genre_dict[genre_id]
    else:
        genre_response = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko")
        if genre_response.status_code == 200:
            genre_data = genre_response.json()['genres']
            for genre_data in genre_data:
                genre_dict[genre_data['id']] = genre_data['name']
            return genre_dict.get(genre_id, '')
        else:
            print("장르 정보를 가져오는데 문제가 발생했습니다.")
            return ''

# 1 ~ 50 페이지 top_rate 영화 출력
for n in range(1, 51):
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko&region=KR&page={n}'
    response = requests.get(url)
    data = response.json()['results']

    for movie in data:
        # 영화 정보 가져오기
        movie_id = movie['id']
        movie_title = movie['title']

        # 중복된 영화인지 확인
        if movie_id in seen_movies:
            continue
        
        # 영화 정보 API 호출
        ott_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={API_KEY}&language=ko&region=KR"
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko&region=KR"
        ott_response = requests.get(ott_url)
        credits_response = requests.get(credits_url)
        
        ott_data = ott_response.json()
        credits_data = credits_response.json()

        # OTT 정보 가져오기
        ott_providers = ott_data.get('results', {}).get('KR', {}).get('flatrate', [])
        ott_ids = [provider['provider_id'] for provider in ott_providers]

        # 넷플릭스, 디즈니, 왓챠에 해당하는 OTT 정보만 저장
        filtered_ott_ids = [id for id in ott_ids if id in [8, 337, 97]]

        # 배우 정보 가져오기
        casts = [actor['name'] for actor in credits_data.get('cast', [])[:5]]

        # provider_id가 빈 리스트면 저장하지 않음
        if not filtered_ott_ids:
            continue

        # 영화 정보 저장
        movie_info = {
            'model': 'movies.movie',
            'pk': movie_id,
            'fields': {
                'title': movie_title,
                'casts': casts,
                'genres': [get_genre_name(genre_id) for genre_id in movie.get('genre_ids', [])],
                'overview': movie.get('overview', ''),
                'popularity': movie.get('popularity', 0),
                'release_date': movie.get('release_date', ''),
                'vote_average': movie.get('vote_average', 0),
                'vote_count': movie.get('vote_count', 0),
                'poster_path': movie.get('poster_path', ''),
                'provider_id': filtered_ott_ids
            }
        }

        # 파일에 저장
        with open(ott_file, 'a', encoding='utf-8') as f:
            json.dump(movie_info, f, ensure_ascii=False, indent=4)
            f.write(',')
            f.write('\n')

        # 중복 확인을 위해 pk 값 저장
        seen_movies.add(movie_id)
