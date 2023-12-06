# API_TMDB

Atividade realizada na matéria de Desenvolvimento Web IV no IFPR.

```bash
# 1) Implementar usando requests do python:
- busca nome do gênero fornecido o id
- busca um filme pelo título
- busca artista pelo nome. 

# 2) Implementar API usando fastapi
- endpoint que retorna 5 filmes recomendados da semana (definidos em uma lista no python)
```

## Executando a API

```bash
# 1. criar ambiente virtual
python3 -m venv env
# 2. ativar ambiente virtual
source env/bin/activate
# 3. instalar dependências
pip install requirements.txt
# 4. iniciar FastApi
uvicorn main:app --reload
```
