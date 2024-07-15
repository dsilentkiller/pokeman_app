from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.pokemon import Pokemon

router = APIRouter()

@router.get("/pokemons")
async def read_pokemons(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM pokemons")
    pokemons = result.scalars().all()
    return pokemons

@router.get("/pokemons/{pokemon_id}")
async def read_pokemon(pokemon_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(f"SELECT * FROM pokemons WHERE id = {pokemon_id}")
    pokemon = result.scalar_one_or_none()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# # Ensure you have a Pokemon model defined
# from app.models.pokemon import Pokemon

# router = APIRouter()


# @router.get("/pokemons")
# async def read_pokemons(db: AsyncSession = Depends(get_db)):
#     # Replace with your actual query
#     result = await db.execute("SELECT * FROM pokemons")
#     pokemons = result.scalars().all()
#     return pokemons


# @router.get("/pokemons/{pokemon_id}")
# async def read_pokemon(pokemon_id: int, db: AsyncSession = Depends(get_db)):
#     # Replace with your actual query
#     result = await db.execute(f"SELECT * FROM pokemons WHERE id = {pokemon_id}")
#     pokemon = result.scalar_one_or_none()
#     if not pokemon:
#         raise HTTPException(status_code=404, detail="Pokemon not found")
#     return pokemon
