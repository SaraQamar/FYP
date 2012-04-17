from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

Base = declarative_base()   #all model classes inherit from this class


class Person(Base):
    __tablename__ = 'persons'
    id_number = Column(Integer(30), primary_key=True)
    name = Column(String(25))
    email_id = Column(Unicode(40))
    phone_no = Column(Unicode(40))

class Email(Base):
    __tablename__ = 'emails'
    
    ids = Column(Integer (25), primary_key=True, autoincrement=True)
    
    name = Column(Unicode(30), ForeignKey(Person.name))
    e_type = Column(Unicode (30))
    e_from = Column(Unicode (20) )
    datetime = Column(Unicode (30) )
    duration = Column(Integer(8))
    key = Column(String(4) , default = 'e')
   
    
    person = relationship(Person , backref=backref('emails'))
    
    
class Call(Base):
    __tablename__ = 'calls'
    
    ids = Column(Integer (25), primary_key=True, autoincrement=True)
    
    name = Column(String(30), ForeignKey(Person.name))
    e_type = Column(Unicode (20))
    datetime = Column(Unicode (20))
    duration = Column(Integer(8))
    key = Column(String(4) , default = 'c')
    e_from =  Column( Unicode(20))
    
    person = relationship(Person , backref=backref('calls'))
    
    
class Msg(Base):
    __tablename__ = 'msgs'
    
    ids = Column(Integer (25), primary_key=True, autoincrement=True)
   
    name = Column(String(30), ForeignKey(Person.name))
    e_type = Column(Unicode (20))
    datetime = Column(Unicode(25) )
    duration = Column(Integer(8))
    key = Column(String(4) , default = 'm')
    e_from =  Column(Unicode (20))
    
    person = relationship(Person , backref=backref('msgs'))
    