import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def preprocess_data(data, is_allmovie=False):
    texts = []
    if is_allmovie:
        for movie in data:
            casts = movie['fields']['casts']
            genres = movie['fields']['genres']
            text = ' '.join(casts + genres)
            texts.append(text)
    else:
        for movie in data:
            casts = movie['casts']
            genres = movie['genres']
            text = ' '.join(casts + genres)
            texts.append(text)
    return texts


def calculate_similarity(selec_data, allmovie_data):
    selec_texts = preprocess_data(selec_data)
    allmovie_texts = preprocess_data(allmovie_data, is_allmovie=True)

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_selec = tfidf_vectorizer.fit_transform(selec_texts)
    tfidf_matrix_allmovie = tfidf_vectorizer.transform(allmovie_texts)

    similarity_matrix = linear_kernel(tfidf_matrix_selec, tfidf_matrix_allmovie)
    return similarity_matrix


def find_similar_movies(selec_file_path, allmovie_file_path):
    with open(selec_file_path, 'r', encoding='utf-8') as f:
        selec_data = json.load(f)

    with open(allmovie_file_path, 'r', encoding='utf-8') as f:
        allmovie_data = json.load(f)

    similarity_matrix = calculate_similarity(selec_data, allmovie_data)

    similar_movies = []
    for i, row in enumerate(similarity_matrix):
        similar_indices = row.argsort()[:-11:-1]
        similar_movie_info = []
        for idx in similar_indices:
            similar_movie_info.append({
                'title': allmovie_data[idx]['fields']['title'],
                'similarity_score': row[idx]
            })
        similar_movies.append(similar_movie_info)

    output_file_path = "usadowls.json"
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(similar_movies, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    selec_file_path = "selec.json"
    allmovie_file_path = "allmovie.json"
    find_similar_movies(selec_file_path, allmovie_file_path)
