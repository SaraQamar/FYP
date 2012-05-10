#import direct.directbase.DirectStart
from db_code import get_db_session
from models import *
import insert
from direct.interval.IntervalGlobal import *
from panda3d.core import *
from pandac.PandaModules import * 
from direct.gui.DirectGui import *
from direct.showbase.ShowBase import *
from direct.showbase.DirectObject import * 
from panda3d.core import Vec3
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task
from math import sin, cos, pi
import sys , math 
dbsession = get_db_session()
cx = 1
class Env(ShowBase):
  def __init__(self):
    ShowBase.__init__(self)
        
    base.setBackgroundColor(0, 0, 0)    
    base.setFrameRateMeter(True)               
    #self.cam.setPos ( 0, 0, 45) 
    self.cam.setPos (30, -60, 102)
    self.cam.lookAt(0,0,0)
    light = PointLight('light')
    self.render.setLight(self.cam.attachNewNode(light))
    self.sizescale = 0.5 # camer set
    self.centr = (0,0,0)
    self.disty = 2
    self.distx = 2
    self.depth = 1 # increase via input
    self.c = 0 #to check center pos
    
  def center(self, prsn_name):
    X = 'Person_pics/' + prsn_name + '.jpeg'
    self.sphere = loader.loadModel("models/ball1.egg")
    tex = loader.loadTexture(X)
    self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
    self.sphere.setTexture(tex, 1)
    self.sphere.setPos(self.centr)
    self.sphere.reparentTo(render)
    self.sphere.setScale(5 * self.sizescale)
    text = prsn_name
    newTextNode = TextNode('text') # Create a new TextNode
    newTextNode.setText(text) # Set the TextNode text
    newTextNode.setAlign(TextNode.ACenter) # Set the text align
    newTextNode.setWordwrap(3.0) # Set the word wrap
    text_generate = newTextNode.generate() # Generate a NodePath
    newTextNodePath = render.attachNewNode(text_generate)
    newTextNodePath.setPos(self.centr[0], self.centr[1], self.centr[2] + 2)
    newTextNodePath.setColor(255, 0, 0, 1)
    newTextNodePath.setScale(3)
    
 
  def addball(self, NUM, i):# set numbr of childs
    X = 'Person_pics/' + NUM + '.jpeg'
    tex = loader.loadTexture(X)   
    f = loader.loadModel("models/ball1.egg")
    f.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
    f.setTexture(tex, 1)
    f.setScale(4 * self.sizescale)
   
    if (i%6 == 0) :
	self.distx = self.distx * 2
	self.disty = self.disty * 2
	
    if (self.centr == (0, 0, 0)):
      
      if self.c == 0:
	self.distx = self.distx * self.depth
	self.disty = self.disty * self.depth
	self.c = 1
      k = self.distx * (math.sin(int(i) * 45 ))
      y = self.disty * (math.cos(int(i) * 45 ))
      
     # if (self.depth > 2) :
	#if i==2:
	 # k = ((self.distx) * (math.sin(int(i) * 45 ))) * math.sin(180)
	  #y = ((self.disty) * (math.cos(int(i) * 45 ))) * math.cos(180)
	#if i==4:
	#  k = (self.distx) * (math.sin(360 ))
	 # y = (self.disty) * (math.cos(360)) 
	   
	
      
		
    if (self.centr != (0, 0, 0)):
	x = (self.centr[0]) 
	z = (self.centr[1])
	
	k = x + ((x/ (self.depth * 2)) * (z/ (self.depth * 2) )) * (math.sin(int(i) * 45 ))
	y = z + ((x/  (self.depth * 2)) * (z/  (self.depth * 2))) * (math.cos(int(i) * 45 ))
	
	  
	if (k >=0 and k<=1.9)or (y>=0 and y<=1.9) or (k <=0 and k>= -1.9) or (y <=0 and y>= -1.9) :
	  k = x + ((x/ (self.depth * 4)) * (z/ (self.depth * 4) )) * (math.sin(int(i) * 45 ))
	  y = z + ((x/  (self.depth * 4)) * (z/  (self.depth * 4))) * (math.cos(int(i) * 45 ))
	  
	if ((k - x)> x)or((y - z) > z) or (-(k - x)> x)or(-(y - z) > z):
	  k = x + ((x/ (self.depth * 3)) * (z/ (self.depth * 3) )) * (math.sin(int(i) * 45 ))
	  y = z + ((x/  (self.depth * 3)) * (z/  (self.depth * 3))) * (math.cos(int(i) * 45 ))
	  
	if ((y-z)< 1.5 and (y-z)>= 0) or ((k-x)< 1.5 and (k-x)>=0):
	  k = x + ((x/(self.depth/2)) * (z/(self.depth/2))) * (math.sin(int(i) * 45 ))
	  y = z + ((x/(self.depth/2)) * (z/(self.depth/2))) * (math.cos(int(i) * 45 ))
	
	  
	if ((y-z)> -1.5 and (y-z)<= 0) or ((k-x)> -1.5 and (k-x)<=0):
	  k = x + ((x/(self.depth/2)) * (z/(self.depth/2))) * (math.sin(int(i) * 45 ))
	  y = z + ((x/(self.depth/2)) * (z/(self.depth/2))) * (math.cos(int(i) * 45 ))
	 
	
    f.setPos(k, y, y)
    f.reparentTo(render)
    
    
    text = NUM
    newTextNode = TextNode('text') # Create a new TextNode
    newTextNode.setText(text) # Set the TextNode text
    newTextNode.setAlign(TextNode.ACenter) # Set the text alig
    newTextNode.setWordwrap(6.0) # Set the word wrap
    text_generate = newTextNode.generate() # Generate a NodePath
    newTextNodePath = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
    newTextNodePath.setPos(k,y,(y + 1))
    newTextNodePath.setColor(255, 0, 0,1)
    newTextNodePath.setScale(2)
    return (k, y, y)   
  
  
  def drawLine(self,startPoint,endPoint,color,thickness):
        if startPoint is None: startPoint = (1, 1, 1)
        linesegs = LineSegs("lines")
        linesegs.setColor(color)
        linesegs.setThickness(thickness)
        linesegs.moveTo(startPoint)
        linesegs.drawTo(endPoint)   
        node = linesegs.create(False) 
        nodePath = render.attachNewNode(node)
        
  def separate_in (self, calls):
        #...data ...seperate incomming 
        in_list = []
        for a in calls:
                if a.e_type == 'incoming':
                    in_list.append(a)
        return in_list
        exit()        
                
            #print in_list
        
            
  def separate_out (self, calls =[]):
    #...data ...seperate outgoing
        oout_list = []
        for a in calls:
	  if a.e_type == 'outgoing':
                    oout_list.append(a);
        return oout_list
        exit()
            #print out_list
            
  def colours (self, a):
        if a == 'c':
            coloursss = (0,147,255,1)
            return coloursss            
        elif a == 'm':
            coloursss = (0,255,0,1)
            return coloursss 
        elif a == 'e':
            coloursss = (0,255,180,1)
            return coloursss         
        elif a == 'ce':
            coloursss = (255,20,147,1)
            return coloursss 
        elif a == 'cm':
            coloursss = (0,0,255,1)
            return coloursss             
        elif a == 'me':
            coloursss = (255,0,0,1)
            return coloursss             
        elif a == 'cme':
            coloursss = (0,180,255,1)
            return coloursss  
        elif a == 'ecm':
            coloursss = (128,0,128,1)
            return coloursss 
        else :
            coloursss = (0,255,255,1)
            return coloursss 
            
            
  def durations (self, inn_list=[]):
         for aList1 in inn_list:
                for aList2 in inn_list:
                    if aList1.e_from == aList2.e_from and aList1 !=aList2:
                        a= aList1.duration
                        b= aList2.duration
                        a = a + b
                        aList1.duration = a
                        inn_list.remove(aList2)
         return inn_list  
     
     
  def merge (self, a=[]):
        L1 = a
        L2 = []
        for l in L1:
            for j in l:
                L2.append(j)
        a = L2
        for aList1 in a:
                for aList2 in a:  
                    if aList1.e_from==aList2.e_from and aList1 !=aList2:
                        x= aList1.duration
                        y= aList2.duration
                        x = x + y
                        aList1.duration = x
                
                        j = aList1.key
                        i = aList2.key
                        i = j+i
                        aList1.key = i
                        a.remove(aList2)          
        return a 
                  
  def merge_out (self, p=[]):
        L1 = p
        L2 = []
        for l in L1:
            for j in l:
                L2.append(j)
        p = L2
        for aList1 in p:
                for aList2 in p:  
                    if aList1.e_from==aList2.e_from and aList1 !=aList2:
                        x= aList1.duration
                        y= aList2.duration
                        x = x + y
                        aList1.duration = x
                
                        j = aList1.key
                        i = aList2.key
                        i = j+i
                        aList1.key = i
                        p.remove(aList2)          
        return p
    
  def display (self, name_l):
     
   self.dbsession = get_db_session()
   V = self.dbsession.query(Person).count()          
   calls =[]
   msg = []
   email = []
   d=0
   for i in name_l:
     for k in i :
	#for v in contacts:
         #for c in v:
	  #if v['name'] == k :
		 #calls = v['calls'],
                 #msg = v['messges'],
                 #email = v['emails'],
     
      calls = self.dbsession.query(Call).filter(Person.name == k )
      msg = self.dbsession.query(Msg).filter(Person.name == k)
      email = self.dbsession.query(Email).filter(Person.name ==  k)
      d = 1 
   
      calls_in_list = self.separate_in(calls)
      rmv_cal_dub_in = self.durations(calls_in_list)
                            #..................
      calls_out_list = self.separate_out(calls)
      rmv_cal_dub_out = self.durations(calls_out_list)
                        #.................
      msg_in_list = self.separate_in(msg)
      rem_msg_dub_in = self.durations(msg_in_list)
                            #.................
      msg_out_list = self.separate_out(msg)
      rem_msg_dub_out = self.durations(msg_out_list) 
                        #...................
                        
      mail_in_list = self.separate_in(email)
      rem_mail_dub_in = self.durations(mail_in_list)
                            #.......................
      mail_out_list = self.separate_out(email)
      rem_mail_dub_out = self.durations(mail_out_list)
                            #.....merge all incomming_outgoing..set duration
                            
      in_list = []
      in_list.append(rmv_cal_dub_in)
      in_list.append(rem_msg_dub_in)
      in_list.append(rem_mail_dub_in)
      in_merge = in_list
      in_merge = self.merge(in_list)
                 
                 
                        #......................
      out_list = []
      out_list.append(rmv_cal_dub_out)    
      out_list.append(rem_msg_dub_out)
      out_list.append(rem_mail_dub_out)
      z = out_list
      outt = self.merge_out(z)     
     
                      #..........represent incoming outgoing both.............
      r =[]
      g = []
      D = []
      P = []
      K = 1
      for item in in_merge:
	    for o in outt:
		if (cmp(int(item.e_from), int(o.e_from))) == 0:
                        r = item
                        g = o
                        NUM = item.name
                        ps= self.addball(NUM, K)#.............................................................................................
                        K = K + 1
                        k = item.key
                        colour1 = self.colours(k)
                       
                        if item.duration <= 10:
                            d = 0.1
                        if item.duration > 10:
                            d = item.duration
                            d = d/10
                            d = d*(0.1)
                        self.drawLine(self.centr,ps,colour2,d) 
                        D.append(r)
                        P.append(ps)
                        # if o['duration'] <= 10:
                            #    m = 0.1
                            #if o['duration'] > 10:
                             #   m = o['duration']
                              #  m = m/10
                               # m = m*(0.1)
                            #e.drawLine(center,pos,colourr2,m)
                        in_merge.remove(r)
                        outt.remove(g)
               
               
      for i in in_merge:
         
         NUM = i.name
         ps= self.addball(NUM, K)
         K = K + 1
	 k = i.key
         if i.duration <= 10:
             d = 0.1
         if i.duration > 10:
             d = i.duration
             d = d/10
             d = d*(0.1)
         r = i.name          
         colour2 = self.colours(k)
         self.drawLine(self.centr,ps,colour2,d)
         D.append(r)
         P.append(ps)
         
      for l in outt:
         
         NUM = l.name
         ps = self.addball(NUM, K)
         K = K + 1
         k = l.key
         if l.duration <= 10:
             d = 0.8
         if l.duration > 10:
             d = l.duration
             d = d/10
             d = d*(0.8)
         r = l.name
         D.append(r)
         colour3 = self.colours(k)
         self.drawLine(self.centr,ps,colour3,d)
         P.append(ps)
      dictionary = dict(zip(D, P))
      return dictionary 
                      
      if d == 0 :
         print("contact name does not exists")
     
    
  def time (self, name_lst, d ):
    
      b = []
      n = []
      for i in name_lst:
	 name_list = [{ i : name_lst[i] }]
	
	 
	 for p in range(d):
	      
	      self.centr = name_lst[i]
	    #  self.r =  - 1
	      self.center(i)
	      b = self.display(name_list)
	      
		
	      self.time(b, p)
	      
      
class Application(DirectObject):
  def __init__(self):
     e = Env()
     ps = Vec3(0, 0, 0)
     n = raw_input("Enter person name: ")
     depth = raw_input("Enter times: ")
     name_list = [{n:ps}]
     e.depth = int(depth)
     nl = []
     e.center(n)
     nl = e.display(name_list)
     depth = int(depth) - 1
     
     e.time(nl, depth)
     
      
w = Application()
run()



    
    
