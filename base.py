from sqlalchemy import Column, String, Integer, BigInteger,ForeignKey, Table
from sqlalchemy.dialects.mysql import BIGINT as biginteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import config

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('product_id', biginteger(unsigned=True,zerofill=False), ForeignKey('product.id')),
    Column('category_id', biginteger(unsigned=True,zerofill=False), ForeignKey('category.id')),
    Column('store_id', biginteger(unsigned=True,zerofill=False), ForeignKey('store.id'))
)


class Product(Base):
        
    __tablename__ = 'product'
    id = Column(biginteger(unsigned=True,zerofill=False),primary_key=True)
    product = relationship("Category",
                             secondary=association_table,
                             back_populates="category")
    product_store = relationship("Store",
                        secondary=association_table,
                         back_populates="store")
    product_name = Column(String(150))
    nutriscore = Column(String(1))
    quantity = Column(String(220))
    store_name = Column(String(155))
    product_url = Column(String(155))
    category_name = Column(String(500))
    
class Category(Base):
        
    __tablename__ = 'category'
    id = Column(biginteger(unsigned=True,zerofill=False),primary_key=True)
    category = relationship("Product",
                             secondary=association_table,
                             back_populates="product")
    product_name = Column(String(150))
    category_name = Column(String(500))
    
class Store(Base):
        
    __tablename__ = 'store'
    id = Column(biginteger(unsigned=True,zerofill=False),primary_key=True)
    store = relationship("Product",
                             secondary=association_table,
                             back_populates="product_store")
    product_name = Column(String(150))
    store_name = Column(String(500))

