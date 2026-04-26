from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.deps import get_db
from app.services.pokeapi_client import get_pokemon_data
from app.schemas.pokemon import PokemonCreate
from app.services.pokemon_logic import classify_iv, recommendation

router = APIRouter()

# ---------------- REGISTER ----------------
@router.post("/register")
def register_pokemon(
    pokemon_id: int,
    level: int,
    iv: int,
    db: Session = Depends(get_db)
):
    # Guardar en DB
    db.execute(
        text("""
        INSERT INTO user_pokemon (pokemon_id, level, iv)
        VALUES (:pokemon_id, :level, :iv)
        """),
        {
            "pokemon_id": pokemon_id,
            "level": level,
            "iv": iv
        }
    )
    db.commit()

    return {
        "message": "Pokemon registrado",
        "pokemon_id": pokemon_id,
        "level": level,
        "iv": iv
    }

# ---------------- ALL ----------------
@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM user_pokemon ORDER BY id DESC")
    ).fetchall()

    return [dict(r._mapping) for r in result]

# ---------------- POKEDEX ----------------
@router.get("/pokedex")
def get_pokedex(db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT up.id, up.pokemon_id, ps.name, up.level, up.iv
        FROM user_pokemon up
        JOIN pokemon_species ps ON ps.id = up.pokemon_id
        ORDER BY up.id DESC
    """)).fetchall()

    return [dict(r._mapping) for r in result]

