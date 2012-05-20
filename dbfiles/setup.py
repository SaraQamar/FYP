import db_code
from models import *
from datetime import *

db_code.setup_db()
db_session = db_code.get_db_session()


def p_db(name, num, email_id, phone_no):
      S = Person()
      S.id_number = num
      S.name = name
      S.email_id = email_id
      S.phone_no = phone_no
      db_session.add(S)
      db_session.commit()
      
r = db_session.query(Person).count() 
if (not r):
    (p_db('PersonA', 1, 'azx', '0989877123'))  
    (p_db('PersonB', 2, 'zxc', '03331233454'))
    (p_db('PersonC', 3, 'sdf', '03331233494'))
    (p_db('PersonD', 4, 'poi', '03331233474'))
    (p_db('PersonE', 5, 'rty', '03331233451'))
    (p_db('PersonF', 6, 'qwe', '03337233452'))
    (p_db('PersonG', 7, 'dfg', '03335213456'))
    (p_db('PersonH', 8, 'kjh', '03335933458'))
    (p_db('PersonI', 9, 'kjh', '03338233459'))
    (p_db('PersonJ', 10, 'lpo', '03337233452'))
    (p_db('PersonK', 11, 'kli', '03337233456'))
    (p_db('PersonL', 12, 'mnb', '03337233466'))

    

def e_db(name, e_type, e_from, datetime, duration):
      S = Email()
      S.name = name
      S.e_type = e_type
      S.e_from = e_from
      S.datetime = datetime
      S.duration = duration
      db_session.add(S)
      db_session.commit()
      
r = db_session.query(Email).count() 
if (not r):
      
    (e_db('PersonD', 'incoming', '0989877123', datetime(2012, 01 ,11, 1, 30, 01), 25))
    (e_db('PersonD', 'incoming', '0989877123', datetime(2012, 01, 21, 2, 30, 02), 27))
    (e_db('PersonL', 'incoming', '0989877123', datetime(2012, 01, 31, 3, 30, 03), 28))
    (e_db('PersonK', 'incoming', '0989877123', datetime(2012, 01, 31, 4, 30, 04), 29))
    (e_db('PersonJ', 'incoming', '0989877123', datetime(2012, 01, 31, 5, 30, 05), 22))
    (e_db('PersonI', 'incoming', '03331233454', datetime(2012, 02, 3, 6, 30, 06), 12))
    (e_db('PersonH', 'incoming', '03331233454', datetime(2012, 03, 31, 7, 30, 07), 30))
    (e_db('PersonF', 'incoming', '03331233454', datetime(2012, 06, 1, 10, 30, 10), 60))
    (e_db('PersonD', 'incoming', '03331233454', datetime(2012, 01, 1, 11, 30, 11), 70))
    (e_db('PersonB', 'incoming', '03331233494', datetime(2012, 02, 1, 12, 30, 12), 80))
    (e_db('PersonC', 'incoming', '03331233451', datetime(2012, 03, 1, 13, 30, 13), 20))
    (e_db('PersonA', 'incoming', '03331233494', datetime(2012, 4, 1, 14, 30, 14), 10))
    (e_db('PersonD', 'incoming', '03331233454', datetime(2012, 5, 1, 15, 30, 15), 25))
    (e_db('PersonD', 'incoming', '03332233494', datetime(2012, 2, 1, 16, 30, 16), 27))
    (e_db('PersonL', 'incoming', '03331233494', datetime(2012, 01, 2, 17, 30, 17), 28))
    (e_db('PersonK', 'incoming', '03334233654', datetime(2012, 01, 3, 18, 30, 18), 29))
    (e_db('PersonJ', 'incoming', '03335233454', datetime(2012, 01, 4, 19, 30, 19), 22))
    (e_db('PersonI', 'incoming', '03331233474', datetime(2012, 01, 5, 20, 30, 10), 12))
    (e_db('PersonH', 'incoming', '03331233474', datetime(2012, 01, 6, 21, 30, 0), 30))
    (e_db('PersonG', 'incoming', '03331233474', datetime(2012, 01, 7, 22, 30, 23), 40))
    (e_db('PersonE', 'incoming', '03339233456', datetime(2012, 01, 8, 23, 30, 24), 50))
    (e_db('PersonF', 'incoming', '03339233454', datetime(2012, 01, 9, 4, 30, 15), 60))
    (e_db('PersonD', 'incoming', '03338233459', datetime(2012, 01, 10, 1, 30, 19), 70))
    (e_db('PersonB', 'incoming', '03337233458', datetime(2012, 01, 11, 2, 30, 17), 80))
    (e_db('PersonC', 'incoming', '03331233451', datetime(2012, 01, 12, 3, 30, 23), 20))
 
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
r = db_session.query(Call).count() 
if (not r):
    (c_db('PersonD', 'incoming', '0989877123', datetime(2012, 01, 11, 1, 3, 01), 25))
    (c_db('PersonD', 'incoming', '0989877123', datetime(2012, 01, 12, 3, 30, 23), 27))
    (c_db('PersonL', 'incoming', '0989877123', datetime(2012, 01, 11, 2, 30, 17), 28))
    (c_db('PersonK', 'incoming', '03331233454', datetime(2012, 01, 10, 1, 30, 19), 29))
    (c_db('PersonJ', 'incoming', '03335233454', datetime(2012, 01, 8, 23, 30, 24), 22))
    (c_db('PersonI', 'incoming', '03331233454', datetime(2012, 01, 7, 22, 30, 23), 12))
    (c_db('PersonH', 'incoming', '03331233454', datetime(2012, 01, 6, 21, 30, 0), 30))
    (c_db('PersonG', 'incoming', '03331233474', datetime(2012, 01, 5, 20, 30, 10), 40))
    (c_db('PersonE', 'incoming', '03331233474', datetime(2012, 01, 4, 19, 30, 19), 50))
    (c_db('PersonF', 'incoming', '03331233474', datetime(2012, 01, 3, 18, 30, 18), 60))
    (c_db('PersonD', 'incoming', '03338233459', datetime(2012, 01, 2, 17, 30, 17), 70))
    (c_db('PersonB', 'incoming', '03337233458', datetime(2012, 12, 1, 16, 30, 16), 80))
    (c_db('PersonC', 'incoming', '03336233457', datetime(2012, 11, 3, 15, 30, 15), 20))
    (c_db('PersonA', 'incoming', '03335233456', datetime(2012, 10, 3, 14, 30, 14), 10))
    (c_db('PersonD', 'incoming', '03332333494', datetime(2012, 10, 3, 14, 30, 14), 27))
    (c_db('PersonL', 'incoming', '03333733474', datetime(2012, 11, 3, 15, 30, 15), 28))
    (c_db('PersonK', 'incoming', '03334833654', datetime(2012, 12, 1, 16, 30, 16), 29))
    (c_db('PersonJ', 'incoming', '03335933454', datetime(2012, 01, 2, 17, 30, 17), 22))
    (c_db('PersonI', 'incoming', '03336633451', datetime(2012, 01, 3, 18, 30, 18), 12))
    (c_db('PersonH', 'incoming', '03337533452', datetime(2012, 01, 4, 19, 30, 19), 30))
    (c_db('PersonG', 'incoming', '03331233451', datetime(2012, 01, 6, 21, 30, 6), 40))
    (c_db('PersonE', 'incoming', '03339333456', datetime(2012, 01, 7, 22, 30, 23), 50))
    (c_db('PersonF', 'incoming', '03339233454', datetime(2012, 01, 8, 23, 30, 24), 60))
    (c_db('PersonD', 'incoming', '03338233459', datetime(2012, 01, 10, 1, 30, 19), 70))
    (c_db('PersonB', 'incoming', '03337233458', datetime(2012, 01, 9, 2, 30, 15), 80))	
    (c_db('PersonC', 'incoming', '03331233451', datetime(2012, 01, 11, 2, 30, 17), 20))
    (c_db('PersonA', 'incoming', '03331233494', datetime(2012, 01, 12, 3, 30, 23), 10) )    
    
    
def m_db(name, m_type, m_from, datetime, duration):
      S = Msg()
      S.name = name
      S.e_type = m_type
      S.e_from = m_from
      S.datetime = datetime
      S.duration = duration
      db_session.add(S)
      db_session.commit()
      
r = db_session.query(Msg).count() 
if (not r):      
    (m_db('PersonA', 'incoming', '03331233451', datetime(2012, 01, 12, 3, 30, 23), 25))
    (m_db('PersonD', 'incoming', '0989877123', datetime(2012, 01, 11, 2, 30, 17), 27))
    (m_db('PersonL', 'incoming', '03331233454', datetime(2012, 01, 9, 23, 30, 15), 28))
    (m_db('PersonK', 'incoming', '03331233454', datetime(2012, 01, 10, 1, 30, 19), 29))
    (m_db('PersonJ', 'incoming', '03335933454', datetime(2012, 01, 8, 23, 30, 24), 22))
    (m_db('PersonI', 'incoming', '03331233474', datetime(2012, 01, 7, 22, 30, 23), 12))
    (m_db('PersonH', 'incoming', '03331233474', datetime(2012, 01, 6, 21, 30, 6), 30))
    (m_db('PersonG', 'incoming', '03331233474', datetime(2012, 01, 4, 19, 30, 19), 40))
    (m_db('PersonE', 'incoming', '03339333456', datetime(2012, 01, 3, 18, 30, 18), 50))
    (m_db('PersonF', 'incoming', '03339233454', datetime(2012, 12, 1, 16, 30, 16), 60))
    (m_db('PersonD', 'incoming', '03338233459', datetime(2012, 10, 31, 14, 30, 14), 70))
    (m_db('PersonC', 'incoming', '03331233451', datetime(2012, 01, 4, 19, 30, 19), 20))
    (m_db('PersonA', 'incoming', '03335213456', datetime(2012, 01, 4, 19, 30, 19), 10))      
    
 
    
    

     
    
  


  

  