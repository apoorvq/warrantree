from Savoir import Savoir
import bcrypt
import json



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


    def bin2hex(self,binn):
        import string
        sonuc = binn.encode('hex')
        return sonuc

    def getInfo(self):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.getinfo()

    def listStreamKeyItems(self,streamID, key, verbose, count, start, localOrdering):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.liststreamkeyitems(streamID,key,verbose,count,start,localOrdering)


    def listPermissions(self,name):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.listpermissions(name)

    def validateAddress(address):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        return api.validateaddress(address)

    def getAdminAddress(self):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        values = self.listPermissions("admin")
        print values
        for index, item in enumerate(values):
            print item['address']
            validationInfo = api.validateaddress(item['address'])
            if validationInfo['ismine']:
                return item['address']



    def createUser(self,username,password,name):
        api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)
        hashed = bcrypt.hashpw(password,bcrypt.gensalt())
        dct = {'USER_NAME':username, 'PASSWORD_HASH':hashed}
        print dct
        address = self.getAdminAddress()
        print address
        txd = api.publishfrom(address,'users_details',username,self.bin2hex(json.dumps(dct)))
        print txd
