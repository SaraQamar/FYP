import db_code
from models import *

#if '__main__' == __name__:
    
db_code.setup_db()
    
db_session = db_code.get_db_session()
    
def p_db(name, num, email_id, phone_no):
      S = Person()
      S.id_number = num
      S.name = name
      S.email_id = email_id
      S.suophone_no = phone_no
      db_session.add(S)
      db_session.commit()




    
def e_db(name, e_type, e_from, datetime, duration):
      S = Email()
      S.name = name
      S.e_type = e_type
      S.e_from = e_from
      S.datetime = datetime
      S.duration = duration
      db_session.add(S)
      db_session.commit()
      #





    
def c_db(name, c_type, c_from, datetime, duration):
      S = Call()
      S.name = name
      S.e_type = c_type
      S.e_from = c_from
      S.datetime = datetime
      S.duration = duration
      db_session.add(S)
      db_session.commit()
      #
    
    
def m_db(name, m_type, m_from, datetime, duration):
      S = Msg()
      S.name = name
      S.e_type = m_type
      S.e_from = m_from
      S.datetime = datetime
      S.duration = duration
      db_session.add(S)
      db_session.commit()
      #




    


 
    
      
    
      
    
    
    
    

     
    
  


  

  