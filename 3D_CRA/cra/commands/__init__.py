from filteR import *
from exporT import *
from imporT import *
from displaY import *
#from ..ui import UserInterfaceEnv
import shlex

class CommandManipulation():
    def __init__(self, app_Object):
        self.input = []
        self.command = ""
        self.argument = ""
        self.cli = app_Object
        self.app_Obj = app_Object
        self.filt = Filter(self.app_Obj)
        #self.glw = Glow()
        self.imp = Import()
        self.exp = Export()
        self.disp = Display(self.app_Obj)

    def Parse(self, textEntered):
        self.input = shlex.split(textEntered)
        self.command = self.input[0]
        self.argument1 = self.input[1]
        self.argument2 = self.input[2]
        self.CallModule()

    def CallModule(self):
        if self.command == "Filter":
            self.filt.filter(self.argument1)
        #elif self.command == "Glow":
         #   self.glw.glow(self.argument1)
        elif self.command == "Import":
            self.imp.import1(self.argument1, self.argument2)
        elif self.command == "Export":
            self.exp.export1(self.argument1, self.argument2)
        elif self.command == "Show":
            self.disp.show(self.argument1)


        


        

        
