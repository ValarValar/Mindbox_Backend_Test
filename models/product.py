from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship

__all__ = ("Product",)

from models.relations import ProductCategoryLink


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)

    categories: List["Category"] = Relationship(back_populates="products", link_model=ProductCategoryLink)
