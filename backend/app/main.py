from fastapi import FastAPI
from app.api.routes import pokemon, health

app = FastAPI(
    title="Oraculum Pokemon Records API",
    version="1.0.0",
    description="API personal para registro y análisis de Pokémon"
)

# 🔹 Rutas
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(pokemon.router, prefix="/pokemons", tags=["Pokemons"])


# 🔹 Root
@app.get("/")
def root():
    return {"message": "Oraculum Pokemon Records API is running 🚀"}