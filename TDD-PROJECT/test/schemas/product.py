from uuid import UUID
from test import product_data
from pydantic import ValidationError
from store.core.schemas.product import ProductIn
import pytest

def test_schemas_return_succes():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 pro Max"
    assert isinstance(product.id,UUID)

def test_schemas_return_raise():
    data = {'name':'Iphone 14 pro Max','quantity':10,'price':8.500}

    with pytest.raises(ValidationError) as erros
        ProductIn.model_validate(data)

    assert err.value.errors()[0]        