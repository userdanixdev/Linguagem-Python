# Essa pasta serve para criar features:
from uuid import UUID
import pytest
import asyncio
from store.db.mongo import db_client
from store.core.schemas.product import ProductIn

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mongo_client():
    return db_client.get()

@pytest.fixture(autouse=True)
async def clear_colletions(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        if collection_name.starswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many()

@pytest.fixture
def product_id()-> UUID:
    return UUID()


@pytest.fixture
def product_in(product_id):
    ProductIn(**product_data(),id=product_id) 

