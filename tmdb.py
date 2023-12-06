from fastapi import FastAPI
import requests

app = FastAPI()

# Chave de API para acessar a API externa
api_key = 'f20c25f20101234d078c5009af594ef8'

# Lista de gêneros de filmes
genres = [
    {'id': 28, 'name': 'Ação'},
    # ... (restante dos gêneros)
    {'id': 37, 'name': 'Faroeste'}
]

def get_json(endpoint, params=None):
    """Faz uma solicitação HTTP e retorna o resultado em JSON."""
    url = f"{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Lança uma exceção se a solicitação falhar
    return response.json()

def get_genero_by_id(id):
    """Retorna o nome do gênero pelo ID fornecido."""
    ids = id if isinstance(id, list) else [id]
    return [genre['name'] for genre in genres if genre['id'] in ids]

def get_movie(movie: str):
    """Busca um filme pelo título."""
    movie_title_lower = movie.lower()
    data = get_json(
        "https://api.themoviedb.org/3/search/movie",
        f"?query={movie_title_lower}&include_adult=true&language=en-US&sort_by=vote_count.desc"
    )

    results = data['results']
    movie_info = []

    for result in results:
        result_movie_title = result['original_title']
        if movie_title_lower in result_movie_title.lower():
            movie_info.append({
                'title': result['original_title'],
                'id': result['id'],
                'popularity': result['popularity']
            })

    return movie_info

# ... (restante do código)

# Adicione documentação para a API
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return RedirectResponse(url="/docs")

# Adicione documentação para a API
@app.get("/", include_in_schema=False)
async def custom_swagger_ui():
    return RedirectResponse(url="/docs")
