from panda3d.core import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import *
from pandac.PandaModules import TextNode
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3
import random
from commands import *

class UserInterfaceEnv(ShowBase):
    def __init__(self, cmnd_Object):
        ShowBase.__init__(self)
        self.cmnd = cmnd_Object
        self.n = 0
        cmnd = ""
        self.commandBox = ""
        self.store = ["","","",""]
        self.title1 = self.AddTitle(-0.65, "Type your commands here:")
        self.title2 = self.AddTitle(0.90, "You have entered:")
        self.instArea = self.AddInstructions(0.82, cmnd)
        self.cmndArea = self.AddArea()
        base.setFrameRateMeter(True)

        

         # cam
        self.cam.setPos(15, -30, 22)
        light = PointLight('light')
        self.render.setLight(self.cam.attachNewNode(light))
        self.cam.lookAt(0,0,0)
        #self.cam.setPos(66, -100, 22)
        #light = PointLight('light')
        #self.render.setLight(self.cam.attachNewNode(light))
        #self.cam.lookAt(8, -10, 2)
    # Function to put instructions on the screen.
    def AddInstructions(self, pos, msg):
        return OnscreenText(text=msg , style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

    # Function to put title on the screen.
    def AddTitle(self, pos, text):
        return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                   pos=(-1.3, pos), align=TextNode.ALeft, scale = .08)

        # Function to add command line are
    def AddArea(self):
        # Username textbox where you type commmands
        p = Vec3(-1.3, 0.0, -0.75)
        self.commandBox = DirectEntry(text = "" , width = 40,  pos = p, scale=.07, command=self.SetText,
                        extraArgs=[self], focus=1, numLines = 3)

    #callback function to set  text
    def SetText(self, textEntered, dummy):
        self.commandBox.enterText('')
        self.commandBox.setFocus()
        oldText = self.instArea.getText()
        self.cmnd.Parse(textEntered)
        if self.person == False:
            self.instArea.setText(oldText + textEntered +" does not exist.\n- - - - - - - - - - - - - - - - - - - - - -\n" )
        if self.person == True:
            self.instArea.setText(oldText + textEntered +"\n- - - - - - - - - - - - - - - - - - - - - -\n" )
        self.store[self.n] = textEntered
        self.n += self.n
        self.commandBox.accept('arrow_up', self.GetHistory, [-1] )

    #function to maintain history
    def GetHistory(self, a):
            self.commandBox.enterText(self.store[self.n])
            self.n -= self.n
    
