from sqlalchemy.orm import Session
from models.products import Products
from schemas.products import ProductGet, ProductsDetails, ProductReadDetails
from config.config import session_maker

class ProductDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def get_product(self, product_id: int):
        return self.db_session.query(Products).filter(Products.id == product_id).first()


    def get_all_products(self):
        return self.db_session.query(Products).all()


    def create_product(self, product: ProductsDetails):
        new_product = Products(**product.dict())
        self.db_session.add(new_product)
        self.db_session.commit()
        self.db_session.flush()
        # self.db_session.refresh(new_product)
        return ProductReadDetails(**new_product.__dict__)
    

def get_product_dal():
    with session_maker() as session:
        with session.begin():
            yield ProductDAL(session)    

