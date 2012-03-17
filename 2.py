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
        
        # to handler collisions
        #self.traverser = CollisionTraverser()
        #self.rayHandler = CollisionHandlerQueue()
        
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


    def drawLine(self,startPoint,endPoint,color=None,thickness=None):
        if color is None: color = (100,100,100,100)
        if thickness is None: thickness = .4
        linesegs = LineSegs("lines")
        linesegs.setColor(color)
        linesegs.setThickness(thickness)
        linesegs.moveTo(startPoint)
        linesegs.drawTo(endPoint)   
        node = linesegs.create(False) 
        nodePath = render.attachNewNode(node)
        
   

class Application(DirectObject):
    def __init__(self):
     e = Env()
     center =(5,5,5)
     list_count = 10
     for i in range(list_count):
        #.................. 
       position = e.addball()
       
       #e.drawLine(center,position,(0,0,0,0),.8)
       e.drawLine(center,position,(0,255,0,1),.8)
     

w = Application()
run()