from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

def setup_db():
    "Creates database tables. Called if the database is not setup"
    
    engine = create_engine("mysql+mysqldb://root:Qamar@localhost/contacts", echo=True)
    #engine = create_engine("sqlite:///mydb.db", echo=True)
    
    models.Base.metadata.bind = engine
    models.Base.metadata.create_all()
    

def get_db_session():
    "Returns database session object"
    #engine = create_engine("mysql://username:password@localhost/db_name", echo=True)
    engine = create_engine("mysql+mysqldb://root:Qamar@localhost/contacts", echo=True)
    
    #Session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
    Session = sessionmaker(bind=engine)
    
    return Session()
