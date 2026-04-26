from pydantic import BaseModel

class PokemonCreate(BaseModel):
    pokemon_id: int
    level: int
    iv: int