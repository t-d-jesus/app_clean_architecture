from domain.repositories.product_repository import ProductRepository
from application.dto.create_product_dto import CreateProductDTO
from domain.entities.product.product import Product

class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, data: CreateProductDTO):
        new_product = Product(id=data.id, name=data.name, price=data.price)
        return await self.product_repository.add(new_product)