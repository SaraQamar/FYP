#from direct.directbase.DirectStart import *
from panda3d.core import *
from pandac.PandaModules import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
import random


class UserInterfaceEnv(ShowBase):
    def __init__(self):
        cmnd = "Nothing yet..."
        self.commandBox = ""
        ShowBase.__init__(self)
        self.title = self.__addtitle__("Type your commands here:")
        self.inst1 = self.__addinstructions__(0.95, "You have entered:")
        self.inst2 = self.__addinstructions__(0.90, cmnd)
        self.cmndArea = self.__addarea__()
        #self.accept('enter', self.attemptDisplay)
        base.setFrameRateMeter(True)


    # Function to put instructions on the screen.
    def __addinstructions__(self, pos, msg):
        return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

    # Function to put title on the screen.
    def __addtitle__(self, text):
        return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                   pos=(-1.3,-0.65), align=TextNode.ALeft, scale = .07)

        # Function to add command line are
    def __addarea__(self):
        # Username textbox where you type in your username
        p = Vec3(-1.3, 0.0, -0.75)
        self.commandBox = DirectEntry(text = "" , width = 40,  pos = p, scale=.07, command=self.__settext__,
                        extraArgs=[self], focus=1, numLines = 3)

    #callback function to set  text
    def __settext__(self, textEntered, dummy):
        self.inst2.setText(textEntered)
        self.commandBox.enterText('')

#clear the text
# focusInCommand=__cleartext__(self),
#def __cleartext__(self):
#	self.commandBox.enterText('')



w = UserInterfaceEnv()
run()
