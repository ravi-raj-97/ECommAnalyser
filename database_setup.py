import sys
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
DecBase = declarative_base()
class Sites(DecBase):

	__tablename__='sites'

	s_id = Column(String(5), primary_key=True)
	site_name = Column(String(10), nullable=False)

class Categories(DecBase):

	__tablename__='categories'

	c_id = Column(String(5), primary_key=True)
	cat_name = Column(String(25), nullable=False)

class Subcategories(DecBase):

	__tablename__='subcategories'

	sc_id = Column(String(5),primary_key=True)
	subcat_name = Column(String(25),nullable=False)

class Items(DecBase):

	__tablename__='items'

	item_id = Column(String(5), primary_key=True)
	item_name = Column(String(25), nullable=False)
	s_id = Column(String(5), ForeignKey('sites.s_id'), primary_key=True)
	c_id = Column(String(5), ForeignKey('categories.c_id'), primary_key=True)
	sc_id = Column(String(5), ForeignKey('subcategories.sc_id'), primary_key=True)
	no_viewed = Column(Integer)
	sites = relationship(Sites)
	categories = relationship(Categories)
	subcategories = relationship(Subcategories)

class Sales(DecBase):

	__tablename__='sales'

	s_id = Column(String(5), ForeignKey('sites.s_id'), primary_key=True)
	c_id = Column(String(5), ForeignKey('categories.c_id'), primary_key=True)
	sc_id = Column(String(5), ForeignKey('subcategories.sc_id'), primary_key=True)
	item_id = Column(String(5), ForeignKey('items.item_id'), primary_key=True)
	price = Column(Integer)
	no_sold = Column(Integer)
	sites = relationship(Sites)
	categories = relationship(Categories)
	items = relationship(Items)
	subcategories = relationship(Subcategories)

	 
class Rating(DecBase):

	__tablename__='rating'

	s_id = Column(String(5),  ForeignKey('sites.s_id'), primary_key=True)
	c_id = Column(String(5),  ForeignKey('categories.c_id'), primary_key=True)
	sc_id = Column(String(5), ForeignKey('subcategories.sc_id'), primary_key=True)
	item_id = Column(String(5),  ForeignKey('items.item_id'), primary_key=True)
	no_stars = Column(Integer)
	sites = relationship(Sites)
	categories = relationship(Categories)
	items = relationship(Items)
	subcategories = relationship(Subcategories)


engine = create_engine(
'sqlite:///ecommanalyser.db')

DecBase.metadata.create_all(engine)
