from pydantic import BaseModel, Field, ConfigDict

class CreateProductDTO(BaseModel):
    id: int = Field(..., description="Product ID")
    name: str = Field(..., min_length=1, description="Product Name")
    price: float = Field(..., gt=0, description="Product Price")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Product 1",
                "price": 99.99
            }
        }
    )