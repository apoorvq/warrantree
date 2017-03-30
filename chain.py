from Savoir import Savoir
import bcrypt



class Chain:
    global rpcuser
    rpcuser = 'multichainrpc'
    global rpcpasswd
    rpcpasswd = 'this-is-insecure-change-it'
    global rpchost
    rpchost = '192.168.99.100'
    global rpcport
    rpcport = '8000'
    global chainname
    chainname = 'DockerChain'


    def getInfo(self):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.getinfo()

    def listStreamKeyItems(streamID, key, verbose = True, $count = 10, start = -10, localOrdering = False):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        api.liststreamkeyitems(streamID,key,verbose,count,start,localOrdering)
        if api.count > 0:
            return True
        else:
            return False

    def listPermissions(name):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.listpermissions(name)

    def createUser(username,password,name):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        hashed = bcrypt.hashpw(password,bcrypt.gensalt())
        dct = {'USER_NAME':username, 'PASSWORD_HASH':hashed}
        api.publishfrom()
