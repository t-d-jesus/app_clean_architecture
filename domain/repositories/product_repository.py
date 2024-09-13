from abc import ABC, abstractmethod
from domain.entities.product import Product

class ProductRepository(ABC):
    
    @abstractmethod
    async def add(self, product: Product) -> int:
        pass

    @abstractmethod
    async def find_by_id(self, product_id: int) -> Product:
        pass