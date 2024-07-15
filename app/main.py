from fastapi import FastAPI
from app.api.pokemon import router as pokemon_router
from app.utils.pokemon import fetch_and_store_pokemon_data

app = FastAPI()


@app.on_event("startup")
async def startup():
    await fetch_and_store_pokemon_data()

app.include_router(pokemon_router, prefix="/api/v1")
