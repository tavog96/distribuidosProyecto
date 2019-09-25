from .app_implementation.consoleInterface.clientConsoleInterfaceController import clientConsoleController

def star():
    consoleGui = clientConsoleController()
    consoleGui.startClient()