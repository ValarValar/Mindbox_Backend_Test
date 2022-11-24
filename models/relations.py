from typing import Optional

from sqlmodel import Field, SQLModel

__all__ = ("ProductCategoryLink",)


class ProductCategoryLink(SQLModel, table=True):
    product_id: Optional[int] = Field(
        default=None, foreign_key="product.id", primary_key=True
    )
    category_id: Optional[int] = Field(
        default=None, foreign_key="category.id", primary_key=True
    )
