from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship

__all__ = ("Category",)

from models.relations import ProductCategoryLink


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)

    products: List["Product"] = Relationship(back_populates="categories", link_model=ProductCategoryLink)