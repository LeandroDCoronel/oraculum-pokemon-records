# 🧠 Oraculum Pokémon Records

API personal para registrar, analizar y visualizar tu colección de Pokémon.

## 🚀 Features

- Registrar Pokémon con nivel e IV
- Clasificación automática de IV
- Recomendaciones estratégicas
- Pokédex personalizada (JOIN con especies reales)
- Integración con PokéAPI (cache local en PostgreSQL)

## 🛠️ Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- PokéAPI

## 📡 Endpoints

### Registrar Pokémon
POST /pokemons/register

### Ver todos
GET /pokemons/all

### Pokédex (con nombres reales)
GET /pokemons/pokedex

## ▶️ Run local
uvicorn app.main:app --reload

## v1.0 - Backend funcional listo
Siguiente: Frontend (Next.js) + UI tipo Pokédex
