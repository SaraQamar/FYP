import sys
sys.path.append('../db')
from ..db.db_code import get_db_session
from ..db.models import *
#import insert
from commands import *
dbsession = get_db_session()
cx = 1
class Display():
    def __init__(self, cli_Object):
        self.e = cli_Object
        self.count = 0
    def show(self, parm):
        e = self.e
        self.dbsession = get_db_session()
        V = self.dbsession.query(Person).count()         
        e.cx = (V/10) + 4
       # e.cube.setScale(e.cx, 3, 1)
        #if rname == 'ALL' :
        for v in self.dbsession.query(Person).all():
                  self.count = self.count + 1
                  name1 = v.name
                  center = e.centerA(name1, self.count)
                  
                  d=0
                  calls = self.dbsession.query(Call).filter(Person.name == name1 )
                  msg = self.dbsession.query(Msg).filter(Person.name == name1)
                  email = self.dbsession.query(Email).filter(Person.name ==  name1)
                  d = 1
                        #rmv_cal_dub_in = []
                  calls_in_list = e.separate_in(calls)
                  rmv_cal_dub_in = e.durations(calls_in_list)
                       #..................
                  calls_out_list = e.separate_out(calls)
                  rmv_cal_dub_out = e.durations(calls_out_list)
                        #.................
                  msg_in_list = e.separate_in(msg)
                  rem_msg_dub_in = e.durations(msg_in_list)
                    #.................
                  msg_out_list = e.separate_out(msg)
                  rem_msg_dub_out = e.durations(msg_out_list) 
                        #...................
                  mail_in_list = e.separate_in(email)
                  rem_mail_dub_in = e.durations(mail_in_list)
                
                            #.......................
                  mail_out_list = e.separate_out(email)
                  rem_mail_dub_out = e.durations(mail_out_list)
                            #.....merge all incomming_outgoing..set duration
                  in_list = []
                  in_list.append(rmv_cal_dub_in)
                  in_list.append(rem_msg_dub_in)
                  in_list.append(rem_mail_dub_in)
                 
                  in_merge = in_list
                  in_merge = e.merge(in_list)
                 
                 
                        #......................
                  out_list = []
                  out_list.append(rmv_cal_dub_out)
                  out_list.append(rem_msg_dub_out)
                  out_list.append(rem_mail_dub_out)
                  z = out_list
                  outt = e.merge_out(z)
     
     
                      #..........represent incoming outgoing both.............
                
                  r =[]
                  g = []
                  for item in in_merge:
                      for o in outt:
                         if (cmp(int(item.e_from), int(o.e_from))) == 0:
                                        r = item 
                                        g = o
                                        NUM = item.name
                                     
                                        pos= e.addball(NUM)  
                                        k = item.e_key
                                        colour1 = e.colours(k)
                                        len = len + 1
                       
                                        if item.duration <= 10:
                                            d = 0.1
                                        if item.duration > 10:
                                            d = item.duration
                                            d = d/10
                                            d = d*(0.1)
                                        e.drawLine(center,pos,colour1,d)
                                        #....................................
                    
                           # if o['duration'] <= 10:
                            #    m = 0.1
                            #if o['duration'] > 10:
                             #   m = o['duration']
                              #  m = m/10
                               # m = m*(0.1)
                            #e.drawLine(center,pos,colourr2,m)
                            #..................................
                                        in_merge.remove(r)
                                        outt.remove(g)
    
                 
                 #......for incoming use any other line seg........................
                  for i in in_merge:
                       
                        NUM = i.name
                        pos= e.addball(NUM)  
                        k = i.key
                        if i.duration <= 10:
                            d = 0.1
                        if i.duration > 10:
                            d = i.duration
                            d = d/10
                            d = d*(0.1)
                    
                        colour2 = e.colours(k)
                        e.drawLine(center,pos,colour2,d)
    
                 
                 #..........Use different style of line to draw outgoing
                  for l in outt:
                  
                    NUM = l.name
                    pos= e.addball(NUM)  
                    k = l.key
                    if l.duration <= 10:
                        d = 0.8
                    if l.duration > 10:
                        d = l.duration
                        d = d/10
                        d = d*(0.8)
                    
                    colour3 = e.colours(k)
                    e.drawLine(center,pos,colour3,d)
                    
