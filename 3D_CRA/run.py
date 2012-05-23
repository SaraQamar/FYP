from panda3d.core import *
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import Vec3
from pandac.PandaModules import TextNode
import random
from direct.gui.OnscreenText import *
from direct.showbase.DirectObject import DirectObject
from cra.ui import *
from cra.commands import *
cx = 1
class Application(UserInterfaceEnv, DirectObject):
    def __init__(self):
        self.cmd = CommandManipulation(self)
        UserInterfaceEnv.__init__(self, self.cmd)
        base.setBackgroundColor(0,0,0)
        self.i = 1
        self.sy = 1
        self.sx = 1
        self.sz = 1
        self.addx =1
        self.addy =1
        self.addz =1
        self.model = False
        self.text = False
        self.link = False
        self.person = True
        self.balls = {}
        
        
    def centerA(self, prsn_name , m):
        if (m < 5):
            self.i = self.i + 1
            X = 'cra/textures/' + prsn_name + '.jpeg'
            tex = loader.loadTexture(X)
            self.sphere = loader.loadModel("cra/models/ball1.egg")
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
            X = 'cra/textures/' + prsn_name + '.jpeg'
            tex = loader.loadTexture(X)
            self.sphere = loader.loadModel("cra/models/ball1.egg")
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

    def centerF(self, prsn_name):
        if self.model == True and self.text == True:
            self.sphere.remove()
            self.newTextNodePath1.remove()
        X = "cra/textures/"+prsn_name + '.jpeg'
        tex = loader.loadTexture(X)
        self.sphere = loader.loadModel("cra/models/ball1.egg")
        self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        self.sphere.setTexture(tex, 1)
        self.sphere.reparentTo(render)
        self.sphere.setPos(1, 1, 1)
        self.sphere.setScale(2.5)
        text = prsn_name
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        self.newTextNodePath1 = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        self.newTextNodePath1.setPos(1, 1, 2)
        self.newTextNodePath1.setColor(255, 0, 0,1)
        self.newTextNodePath1.setScale(.8)

    def addball(self, NUM):
        #pos = Vec3(random.uniform(-7, 7), random.uniform(-7, 7), random.uniform(-7, 7))
        if self.model == True and self.text == True:
            self.f.remove()
            self.newTextNodePath2.remove()
        a = random.uniform(-7, 7)
        b = random.uniform(-7, 7)
        c = random.uniform(-7, 7)
        pos = Vec3(a,b,c)
        tex = loader.loadTexture("cra/textures/e.jpeg")
        self.f = loader.loadModel("cra/models/ball1.egg")
        self.f.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        self.f.setTexture(tex, 1)
        self.f.setPos(pos)
        self.f.setScale(1.5)
        self.f.reparentTo(render)
        self.f.setCollideMask(0)
        text = NUM
        newTextNode = TextNode('text') # Create a new TextNode
        newTextNode.setText(text) # Set the TextNode text
        newTextNode.setAlign(TextNode.ACenter) # Set the text align
        newTextNode.setWordwrap(6.0) # Set the word wrap
        text_generate = newTextNode.generate() # Generate a NodePath
        self.newTextNodePath2 = render.attachNewNode(text_generate) # Attach the NodePath to the render tree
        self.newTextNodePath2.setPos(a,b,(c + 0.3))
        self.newTextNodePath2.setColor(255, 0, 0,1)
        self.newTextNodePath2.setScale(.6)
        return pos

    def drawLine(self,startPoint,endPoint,color,thickness):
        if self.link == True:
            self.nodePath.remove()    
        linesegs = LineSegs("lines")
        linesegs.setColor(color)
        linesegs.setThickness(thickness)
        linesegs.moveTo(startPoint)
        linesegs.drawTo(endPoint)
        node = linesegs.create(False)
        self.nodePath = render.attachNewNode(node)
        #self.nodePath.setShader()

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

w = Application()
w.run()