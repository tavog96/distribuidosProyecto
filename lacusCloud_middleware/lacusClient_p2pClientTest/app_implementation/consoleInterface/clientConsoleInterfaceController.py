from ...app_core.useCases.getRemoteResourceList import getLocalResourceList
from ...app_implementation.common.configFileController import configFileController
from ...app_infrastructure.resourceManagement.resourceDirectoryManagement import resourceDirectoryManager
from ...app_infrastructure.networkManagement.restClient import restClientController

class clientConsoleController:

    consoleCursor = []

    def __init__(self):
        super().__init__()

    def startClient(self):
        self.consoleCursor.append('distribuidosApp')
        self.initialInput()
        pass

    def initialInput (self):
        active = True
        msg = False
        while active:
            option = self.printConsoleCursor(msg)
            msg=False
            ### loking for options here :v

            if (option=='help'):
                option = 'ignore'
                self.printHelp(['connect', 'local', 'exit', 'help'])
                pass

            if (option=='exit'):
                option = 'ignore'
                active = False

            if (option == 'connect'):
                option = 'ignore'
                remoteIP = input('Insert the remote host IP (000,000,000,000):')
                ####    Asign IP to server obj here
                self.consoleCursor.append(remoteIP)
                self.remoteServerMenu()

            if (option == 'local'):
                option = 'ignore'
                self.consoleCursor.append('local')
                self.localServerMenu()

            #### Finally
            if (option!='ignore'):
                msg = 'Incorrect command, type "help" for more information'
        self.consoleCursor=self.consoleCursor[:-1]

 
    def remoteServerMenu (self):
        active = True
        msg = False
        while active:
            option = self.printConsoleCursor(msg)
            msg=False
            ### loking for options here :v

            if (option=='help'):
                option = 'ignore'
                self.printHelp(['resourcer', 'disconnect', 'help'])
                pass
            
            if (option=='resources'):
                option = 'ignore'
                ############ print remote resources here
                pass

            if (option=='disconnect'):
                option = 'ignore'
                active = False

            #### Finally
            if (option!='ignore'):
                msg = 'Incorrect command, type "help" for more information'
        self.consoleCursor=self.consoleCursor[:-1]


    def localServerMenu (self):
        active = True
        msg = False
        while active:
            option = self.printConsoleCursor(msg)
            msg=False
            ### loking for options here :v

            if (option=='help'):
                option = 'ignore'
                self.printHelp(['resources', 'exit', 'help'])
                pass
            
            if (option=='resources'):
                option = 'ignore'
                ############ print remote resources here
                pass

            if (option=='exit'):
                option  = 'ignore'
                active = False

            #### Finally
            if (option!='ignore'):
                msg = 'Incorrect command, type "help" for more information'
        self.consoleCursor=self.consoleCursor[:-1]

    def printConsoleCursor(self, msg=False):
        cursor2print = ''
        for cursorPart in self.consoleCursor:
            cursor2print = cursor2print + cursorPart+'/'
        cursor2print = cursor2print[:-1]
        if (msg!=False):
            cursor2print = cursor2print+'('+msg+')'
        cursor2print = cursor2print+':'
        return input(cursor2print)

    def printHelp (self, options =  False):
        msgOptions= "[HELP INFO] Here's a list of all avaible options keywords at this module: "
        for option in options:
            msgOptions = msgOptions+option+','
        if (len(options)>0):
            msgOptions = msgOptions[:-1]
        print (msgOptions)