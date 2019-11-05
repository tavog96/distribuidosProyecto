# from .app_implementation.consoleInterface.clientConsoleInterfaceController import clientConsoleController

# def star():
#     consoleGui = clientConsoleController()
#     consoleGui.startClient()

import json

strings = 'cadena de texto de prueba'
printable = json.dumps(strings)
print(printable)
print (strings)
print(json.loads(printable))