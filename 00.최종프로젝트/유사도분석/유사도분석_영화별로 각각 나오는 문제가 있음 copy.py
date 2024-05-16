import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def find_similar_movies(selec_json_file, allmovie_json_file):
    # JSON 파일 로드
    selec_json = load_json(selec_json_file)
    allmovie_json = load_json(allmovie_json_file)

    # selec.json 파일에서 casts, genres 정보 추출
    selec_casts = [' '.join(movie['casts']) for movie in selec_json]
    selec_genres = [' '.join(movie['genres']) for movie in selec_json]

    # allmovie.json 파일에서 pk, casts, genres 정보 추출
    allmovie_pks = [movie['pk'] for movie in allmovie_json]
    allmovie_casts = [' '.join(movie['fields']['casts']) for movie in allmovie_json]
    allmovie_genres = [' '.join(movie['fields']['genres']) for movie in allmovie_json]

    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    selec_casts_tfidf = vectorizer.fit_transform(selec_casts)
    allmovie_casts_tfidf = vectorizer.transform(allmovie_casts)
    selec_genres_tfidf = vectorizer.fit_transform(selec_genres)
    allmovie_genres_tfidf = vectorizer.transform(allmovie_genres)

    # casts에 대한 코사인 유사도 계산
    casts_similarity_matrix = cosine_similarity(selec_casts_tfidf, allmovie_casts_tfidf)

    # genres에 대한 코사인 유사도 계산
    genres_similarity_matrix = cosine_similarity(selec_genres_tfidf, allmovie_genres_tfidf)

    similar_movies = {}

    # 각 selec 영화에 대해 유사한 영화 찾기
    for i, selec_movie in enumerate(selec_json):
        casts_similar_indices = casts_similarity_matrix[i].argsort()[:-11:-1]
        genres_similar_indices = genres_similarity_matrix[i].argsort()[:-11:-1]

        similar_movies[selec_movie['title']] = {
            'casts': [allmovie_pks[idx] for idx in casts_similar_indices],
            'genres': [allmovie_pks[idx] for idx in genres_similar_indices]
        }

    # JSON 파일로 저장
    save_json(similar_movies, 'usado.json')

    return similar_movies

# 함수 호출 및 출력
similar_movies = find_similar_movies("selec.json", "allmovie.json")
for selec_movie, similar_info in similar_movies.items():
    print(f"{selec_movie}:")
    print("   배우 기준 유사도 높은 영화:", similar_info['casts'])
    print("   장르 기준 유사도 높은 영화:", similar_info['genres'])
    print()
