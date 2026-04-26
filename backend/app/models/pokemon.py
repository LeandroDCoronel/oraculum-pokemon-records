from sqlalchemy import Column, Integer

class UserPokemon(Base):
    __tablename__ = "user_pokemon"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer)
    level = Column(Integer)
    iv = Column(Integer)