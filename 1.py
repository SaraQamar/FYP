from direct.directbase.DirectStart import *
from direct.actor.Actor import Actor
from panda3d.core import * 
from pandac.PandaModules import * 
from direct.gui.DirectGui import * 
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject 
import random, sys, math

class Env(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        base.setFrameRateMeter(True)
        
        #
        self.balls = {}
        
        # load a environment
        cube = self.loader.loadModel("models/cube")
        cube.setPos(0, 0, 0)
        cube.reparentTo(self.render)
        cube.setScale(0.5, 0.5, 0.5)
        
         # cam
        self.cam.setPos(15, 15, 15)
        light = PointLight('light')
        self.render.setLight(self.cam.attachNewNode(light))
        self.cam.lookAt(cube)
        
        self.sphere = loader.loadModel("models/ball")
        self.sphere.reparentTo(render)
        self.sphere.setPos(5, 5, 5)
        self.sphere.setScale(.5)
        

    def addball(self):
        pos = Vec3(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))
        f = loader.loadModel("models/ball")
        f.setPos(pos)
        f.setScale(.3)
        f.reparentTo(render)
        f.setCollideMask(0)
        return pos    


    def drawLine(self,startPoint,endPoint,color,thickness):
        #if color is None: color = (100,100,100,100)
        #if thickness is None: thickness = .4
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
            for b in a:
                if b['type'] == 'incoming':
                    in_list.append(b)
        return in_list
        exit()        
                
            #print in_list
        
            
    def separate_out (self, calls =[]):
    #...data ...seperate outgoing
        oout_list = []
        for a in calls:
            for b in a:
                if b['type'] == 'outgoing':
                    oout_list.append(b);
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
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        a= aList1['duration']
                        b= aList2['duration']
                        a = a + b
                        aList1['duration'] = a
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
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        x= aList1['duration']
                        y= aList2['duration']
                        x = x + y
                        aList1['duration'] = x
                
                        j = aList1['key']
                        i = aList2['key']
                        i = j+i
                        aList1['key'] = i
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
                    if aList1['from']==aList2['from'] and aList1 !=aList2:
                        x= aList1['duration']
                        y= aList2['duration']
                        x = x + y
                        aList1['duration'] = x
                
                        j = aList1['key']
                        i = aList2['key']
                        i = j+i
                        aList1['key'] = i
                        p.remove(aList2)          
        return p
    
    
    
class Application(DirectObject):
    def __init__(self):
     e = Env()
     name = raw_input("Enter person name: ")
     
     contacts = [
                {'name': 'PersonA',
                'calls': [
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300 , 'key' : 'c'},
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100,  'key' : 'c'},
                        {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 150, 'key' : 'c'},
                        {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200,  'key' : 'c'},
                        {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30,  'key' : 'c'}
                    ],
                'messges': [
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300,  'key' : 'm'},
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100,  'key' : 'm'},
                        {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 150, 'key' : 'm'},
                        {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200,  'key' : 'm'},
                        {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30,  'key' : 'm'}
                    ],
                'emails': [
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300, 'key' : 'e'},
                        {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100, 'key' : 'e'},
                        {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 15, 'key' : 'e'},
                        {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200, 'key' : 'e'},
                        {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30, 'key' : 'e'}
                    ]
               
            },
                {
        
        'name': 'PersonB',
        'calls': [
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300, 'key' : 'c'},
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100, 'key' : 'c'},
                    {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 150,'key' : 'c'},
                    {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200, 'key' : 'c'},
                    {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30, 'key' : 'c'}
                ],
         'messges': [
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300, 'key' : 'm'},
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100, 'key' : 'm'},
                    {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 150,'key' : 'm'},
                    {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200, 'key' : 'm'},
                    {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30, 'key' : 'm'}
                ],
          'emails': [
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 2:30 PM', 'duration': 300, 'key' : 'e'},
                    {'type': 'incoming', 'from': '03331233454', 'datetime': '2012-01-31 5:30 PM', 'duration': 100, 'key' : 'e'},
                    {'type': 'outgoing', 'from': '03331233411', 'datetime': '2012-02-11 11:00 AM', 'duration': 150, 'key': 'e'},
                    {'type': 'outgoing', 'from': '03331233433', 'datetime': '2012-02-13 9:00 PM', 'duration': 200, 'key' : 'e'},
                    {'type': 'incoming', 'from': '03331233422', 'datetime': '2012-02-13 10:00 PM', 'duration': 30, 'key' : 'e'}
                ]
        }
        ]
    
     calls = []
     msg = []
     email = []
     
    
    
     d=0
     for v in contacts:
         for c in v:
        #........person name............
             if v['name'] == name:
                        
                 calls = v['calls'],
                 msg = v['messges'],
                 email = v['emails'],
                 d = 1
                        #rmv_cal_dub_in = []
     calls_in_list = e.separate_in(calls)
     rmv_cal_dub_in = e.durations(calls_in_list)
                            #..................
     calls_out_list = e.separate_out(calls)
     rmv_cal_dub_out = e.durations(calls_out_list)
                        #.................
     msg_in_list = e.separate_in(msg)
     rem_msg_dub_in = e. durations(msg_in_list)
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
             if (cmp(int(item['from']), int(o['from']))) == 0:
                        r = item 
                        g = o
                        center= (5,5,5)
                        pos= e.addball()  
                        k = item['key']
                        colour1 = e.colours(k)
                        #print colour1
                            #print colour1
                            #k = o['key']
                            #colourr2 = e.colours(k)
                        if item['duration'] <= 10:
                            d = 0.1
                        if item['duration'] > 10:
                            d = item['duration']
                            d = d/10
                            d = d*(0.1)
                        e.drawLine(center,pos,colour1,d)
                    
                           # if o['duration'] <= 10:
                            #    m = 0.1
                            #if o['duration'] > 10:
                             #   m = o['duration']
                              #  m = m/10
                               # m = m*(0.1)
                            #e.drawLine(center,pos,colourr2,m)
                        in_merge.remove(r)
                        outt.remove(g)
    
                 
                 #......for incoming use any other line seg........................
     for i in in_merge:
         center= (5,5,5) 
         pos= e.addball()  
         k = i['key']
         if i['duration'] <= 10:
             d = 0.1
         if i['duration'] > 10:
             d = i['duration']
             d = d/10
             d = d*(0.1)
                    
         colour2 = e.colours(k)
         e.drawLine(center,pos,colour2,d)
    
                 
                 #..........Use different style of line to draw outgoing
     for l in outt:
         center= (5,5,5) 
         pos= e.addball()  
         k = l['key']
         if l['duration'] <= 10:
             d = 0.8
         if l['duration'] > 10:
             d = l['duration']
             d = d/10
             d = d*(0.8)
                    
         colour3 = e.colours(k)
         e.drawLine(center,pos,colour3,d)



     if d ==0 :
         print("contact name does not exists")
       

w = Application()
run()