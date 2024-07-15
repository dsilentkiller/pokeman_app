import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from app.models.pokemon import Pokemon

async def fetch_and_store_pokemon_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=100")
        pokemons = response.json()["results"]

        async with AsyncSessionLocal() as session:
            for pokemon in pokemons:
                poke_response = await client.get(pokemon["url"])
                poke_data = poke_response.json()
                new_pokemon = Pokemon(
                    name=poke_data["name"],
                    image=poke_data["sprites"]["front_default"],
                    type=poke_data["types"][0]["type"]["name"]
                )
                session.add(new_pokemon)
            await session.commit()
