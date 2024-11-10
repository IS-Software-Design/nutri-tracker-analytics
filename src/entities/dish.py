from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.entities.base import Base


class Dish(Base):
    __tablename__ = 'Dish'

    dish_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    total_calories = Column(Float, nullable=False)
    total_proteins = Column(Float, nullable=False)
    total_fats = Column(Float, nullable=False)
    total_carbs = Column(Float, nullable=False)
    ispublic = Column(Boolean, nullable=False)
    owner_id = Column(Integer, ForeignKey("User.user_id"), nullable=True)

    owner = relationship("User", back_populates="user_dishes")
    products = relationship("DishProduct", back_populates="dishes")