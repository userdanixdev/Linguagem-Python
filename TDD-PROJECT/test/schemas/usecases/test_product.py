from test.schemas.usecases.product import ProductUsecase


async def test_usecases_should_return_success(product_in):
    result = await ProductUsecase.create(body=product_in)

    assert isinstance(result, ProductOut)