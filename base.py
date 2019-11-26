from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import config

Base = declarative_base()

association_table = Table('association', Base.metadata,
Column('product_id', Integer, ForeignKey('product.id')),
Column('category_id', Integer, ForeignKey('category.id'))
    )

class Parent(Base):
        
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    children = relationship("Parent",
                            secondary=association_table)

class Child(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                            secondary=association_table)