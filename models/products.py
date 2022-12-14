from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from config.config import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    title = Column(String)
    price = Column(Integer)
    size = Column(Integer)
    description = Column(String)
    image_url = Column(String)