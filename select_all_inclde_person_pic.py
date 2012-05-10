from db_code import get_db_session
from models import *
import insert
from direct.actor.Actor import Actor
from panda3d.core import * 
from pandac.PandaModules import * 
from direct.gui.DirectGui import * 
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject 
from panda3d.core import Vec3
from direct.gui.OnscreenText import OnscreenText
from pandac.PandaModules import TextNode
import random, sys, math
dbsession = get_db_session()
cx = 1
class Env(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        base.setFrameRateMeter(True)
        base.setBackgroundColor(0,0,0)
        
        self.cam.setPos(66, -100, 22)
        light = PointLight('light')
        self.render.setLight(self.cam.attachNewNode(light))
        self.cam.lookAt(8, -10, 2)
        self.i = 1
        self.sy = 1
        self.sx = 1
        self.sz = 1
        self.addx =1
        self.addy =1
        self.addz =1
        
        
    def center(self, prsn_name , m):
        if (m < 5):
            self.i = self.i + 1
            X = 'Person_pics/' + prsn_name + '.jpeg' 
	    tex = loader.loadTexture(X)
	    self.sphere = loader.loadModel("models/ball1.egg")
	    self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
	    self.sphere.setTexture(tex, 1)
            
            self.sphere.reparentTo(render)
            self.sphere.setCollideMask(0)
            gx = self.sx
            y = self.sy
            z = self.sz
            pos = (gx,y,z)
            self.addx =gx
            self.addy =y
            self.addz =z
            self.sphere.setPos(1, self.sy, 1)
            self.sphere.setScale(1)
            self.sy = -14*(self.i)
            
            
        else :
       
            x = m/5 
            j = m%5
            if ( j == 0):
                self.sy = 1
                self.i = 1
            else :
                self.sy = -14*(self.i)
                
               
            self.sx = 40*(x)
            X = 'Person_pics/' + prsn_name + '.jpeg' 
	    tex = loader.loadTexture(X)
	    self.sphere = loader.loadModel("models/ball1.egg")
	    self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
	    self.sphere.setTexture(tex, 1)
            self.sphere.reparentTo(render)
            self.sphere.setCollideMask(0)
            gx = self.sx
            y = self.sy
            z = self.sz
            self.addx =gx
            self.addy =y
            self.addz =z
            
            pos = (gx, y, 1)
            self.sphere.setPos(pos)
            #self.sphere.setScale(.9)
            self.i = self.i + 1
            self.sphere.setScale(1)
        text = prsn_name
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        newTextNodePath = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        newTextNodePath.setPos(gx, y, (z + 2))
        newTextNodePath.setColor(0, 0, 255,1)
        newTextNodePath.setScale(.5)
        return pos
        
          
    def addball(self, NUM):
	X =  "Person_pics/" + NUM + '.jpeg' 
	tex = loader.loadTexture(X)
	f = loader.loadModel("models/ball1.egg")
        f.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        a = random.uniform((-8 + (self.addx)), (8 + self.addx))
        b = random.uniform((-8 + (self.addy)), (8 + self.addy))
        c = random.uniform((-8 + (self.addz)), (8 + self.addz))
        pos = Vec3(a,b,c)
        f.setTexture(tex, 1)
        f.setPos(pos)
        f.setScale(.8)
        f.reparentTo(render)
        f.setCollideMask(0)
        text = NUM
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        newTextNodePath = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        newTextNodePath.setPos(a,b,(c + 0.6))
        newTextNodePath.setColor(255, 0, 0,1)
        newTextNodePath.setScale(.5)
        return pos    


    def drawLine(self,startPoint,endPoint,color,thickness):
        linesegs = LineSegs("lines")
        linesegs.setColor(color)
        linesegs.setThickness(thickness)
        linesegs.moveTo(startPoint)
        linesegs.drawTo(endPoint)   
        node = linesegs.create(False) 
        nodePath = render.attachNewNode(node)
        
    def separate_in (self, callss):
        #...data ...seperate incomming 
        in_list = []
        for a in callss:
        
	  if a.e_type == 'incoming':
                   
                 in_list.append(a)
        return in_list
        exit()        
    
    def separate_out (self, callss):
    #...data ...seperate outgoing
        oout_list = []
        for a in callss:
              if a.e_type == 'outgoing':
                    oout_list.append(a)
                   
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
        elif a == 'ec':
            coloursss = (255,20,147,1)
            return coloursss
        elif a == 'cm':
            coloursss = (0,0,255,1)
            return coloursss   
        elif a == 'mc':
            coloursss = (0,0,255,1)
            return coloursss
        elif a == 'me':
            coloursss = (255,0,0,1)
            return coloursss 
        elif a == 'em':
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
            
        
    def durations (self, inn_list):
      
         for aList1 in inn_list:
	   if inn_list is not None :
                for aList2 in inn_list:
		  
                  if aList1.e_from == aList2.e_from and aList1 != aList2:
                        a= aList1.duration
                        b= aList2.duration
                        a = a + b
                        aList1.duration = a
                      
                        #inn_list.delete(aList2)
                        if inn_list is not None :
			  inn_list = inn_list.remove(aList2)
                        
        
         return inn_list  
     
     
    def merge (self, a=[]):
        L1 = a
        L2 = []
        for l in L1:
	  if l is not None :
            for j in l:
                L2.append(j)
        a = L2
        for aList1 in a:
                for aList2 in a:  
                    if aList1.e_from == aList2.e_from and aList1 !=aList2:
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
                  
    def merge_out (self, p):
        L1 = p
        L2 = []
        for l in L1:
            for j in l:
                L2.append(j)
        p = L2
        for aList1 in p:
                for aList2 in p:  
                    if aList1.e_from == aList2.e_from and aList1 !=aList2:
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
    
    
  
class Application(DirectObject):
    def __init__(self):
        e = Env()
        count = 0
        self.dbsession = get_db_session()
        V = self.dbsession.query(Person).count()         
        e.cx = (V/10) + 4
       # e.cube.setScale(e.cx, 3, 1)
        #if rname == 'ALL' :
        for v in self.dbsession.query(Person).all():
                  count = count + 1
                  name1 = v.name
                  center = e.center(name1, count)
                  
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

     
     


                  if d ==0 :
                        print("contact name does not exists")
       

w = Application()
run()