from lacus_middleware.lacus_client.implementation.client import Client


ipLocal = input('set the local IP for the client:')
ipTracker = input('set the tracker server IP location:')
nodeMode = input('Is this client working as a node (TRUE / FALSE):')

clientController = False

if (nodeMode == 'true' or nodeMode=='True' or nodeMode == 'TRUE'):
    clientController = Client(ipLocal, ipTracker, True)
else:
    clientController = Client(ipLocal, ipTracker)

exitflag = False

if (clientController == False):
    exitflag = True
    print("Error: Unable to start client, nodeMode not inserted properly.")

while (not exitflag):
    command = input('select a command:')

    if (command == 'login'):
        user = input ('username:')
        password = input('password:')
        if (clientController.login(user, password)):
            print('Login succesfully')
        else:
            print ("Error executing command")

    if (command == 'register'):
        user = input ('username:')
        password = input('password:')
        if (clientController.register(user, password)):
            print('Register succesfully')
        print ("Error executing command")

    if (command == 'share'):
        filepath = input ('filepath:')
        clientController.shareResource(filepath)

    if (command == 'list'):
        resources = clientController.getResourceList()
        if (resources!= False):
            print (str(resources))
        else:
            print ("Error executing command")

    if (command == 'download'):
        uid = input('Resource UID:')
        clientController.downloadResource(uid)


    if (command == 'exit'):
        exitflag = True

    print ('enabled commands: login, register, share, list, download')

