import pytest
from unittest.mock import AsyncMock
from application.usecases.create_product import CreateProductUseCase
from application.dto.create_product_dto import CreateProductDTO
from domain.entities.product.product import Product

@pytest.mark.asyncio
async def test_create_product_success():
    mock_product_repository = AsyncMock()
    mock_product_repository.add.return_value = 1  # Simulates the return of the repository
    
    create_product_usecase = CreateProductUseCase(mock_product_repository)
    product_data = CreateProductDTO(id=1, name="Test Product", price=100.0)

    result = await create_product_usecase.execute(product_data)
    
    mock_product_repository.add.assert_called_once()
    
    assert result == 1