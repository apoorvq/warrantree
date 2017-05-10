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

    def __init__(self,api):
        self.api = Savoir(rpcuser,rpcpasswd,rpchost,rpcport,chainname)



    def bin2hex(self,binn):
        import string
        sonuc = binn.encode('hex')
        return sonuc

    def getInfo(self):
        return self.api.getinfo()

    def getPeerInfo(self):
        return self.api.getPeerInfo()

    def getNewAddress(self):
        return self.api.getnewaddress()

    """ Sends one or more assets to address, returning the txid. In Bitcoin Core, the amount field is the quantity of
      the bitcoin currency. For Carbon.Chain, an {"asset":qty, ...} object can be used for amount, in which each asset
      is an asset name, ref or issuance txid, and each qty is the quantity of that asset to send (see native assets).
      Use "" as the asset inside this object to specify a quantity of the native blockchain currency. See also
      sendassettoaddress for sending a single asset and sendfromaddress to control the address whose funds are used. """

    def sendtoAddress(self,address,amount,comment,commentTo):
        return self.api.sendtoaddress(address,amount,comment,commentTo)


    """ Outputs a list of available API commands inlcuding Carbon.Chain Specific Commands """
    def help(self):
        return self.api.help()

    """ Adds to the atomic exchange transaction in hexstring given by a previous call to createrawexchange or
     * appendrawexchange. This adds an offer to exchange the asset/s in output vout of transaction txid for qty units
     * of asset, where asset is an asset name, ref or issuance txid. The txid and vout should generally be taken from
     * the response to preparelockunspent or preparelockunspentfrom. Multiple items can be specified within the fourth
     * parameter to request multiple assets. Returns a raw hexadecimal transaction in the hex field alongside a
     * complete field stating whether the exchange is complete (i.e. balanced) or not. If complete, the transaction can
     * be transmitted to the network using sendrawtransaction. If not, it can be passed to a further counterparty, who
     * can call decoderawexchange and appendrawexchange as appropriate.
 """
    def appendRawExchange(self,hexString,txId,vout,extra):
        return self.api.appendrawexchange(hexString,txId,vout,extra)

    """ Adds a metadata output to the raw transaction in tx-hex given by a previous call to createrawtransaction. The
     * metadata is specified in data-hex in hexadecimal form and added in a new OP_RETURN transaction output. The
     * transaction can then be signed and transmitted to the network using signrawtransaction and sendrawtransaction.
     *
    """
    def appendRawMetadata(self,txHex,dataHex):
        return self.api.appendrawmetadata(txHex,dataHex)


    def combineUnspent(self,addresses,minConf,minInputs,maxInputs,maxTime):
        return self.api.combineunspent(addresses,minConf,minInputs,maxInputs,maxTime)

    def sendRawTransaction(self,hex,allowHighFees):
        return self.api.sendrawtransaction(hex,allowHighFees)

    def singMessage(self,address,message):
        return self.api.signmessage(address,message)

    def verifyMessage(self,address,signature,message):
        return self.api.verifymessage(address,signature,message)



    def createRawExchange(self,txId,vOut,extra):
        return self.api.createrawexchange(txId,vOut,extra)

    def decodeRawExchange(self,hexString,verbose):
        return self.api.decoderawexchange(hexString,verbose)

    def createRawSendFrom(self,fromAddress,addresses,data,action):
        return self.api.createrawsendfrom(fromAddress,addresses,data,action)

    def disableRawTransaction(self,hexString):
        return self.api.disablerawtransaction(hexString)

    def importAddress(self,address,label,rescan):
        return self.api.importaddress(address,label,rescan)

    def getAddressBalances(self,address,minConf,includeLocked):
        return self.api.getaddressbalances(address,minConf,includeLocked)

    def getAddresses(self,vebose):
        return self.api.getaddresses(verbose)

    def getAddressTransaction(self,address,txId,verbose):
        return self.api.getaddresstransaction(address,txId,verbose)

    def getAssetBalances(self,account,minConf,includeWatchOnly,includeLocked):
        return self.api.getassetbalances(account,minConf,includeWatchOnly,includeLocked)

    def getTotalBalances(self,minConf,includeWatchOnly,includeLocked):
        return self.api.getassetbalances(minConf,includeWatchOnly,includeLocked)

    def getWalletTransaction(self,txId,includeWatchOnly,verbose):
        return self.api.getwallettransaction(txid,includeWatchOnly,verbose)


    def grant(self,addresses,permissions,nativeamount,comment,commentTo,startBlock,endBlock):
        return self.api.grant(addresses,permissions,nativeamount,comment,commentTo,startBlock,endBlock)

    def grantFrom(fromAddress,toAddress,permissions,nativeamount,startBlock,endBlock,comment,commentTo):
        return self.api.grantfrom(fromAddress,toAddress,permissions,nativeamount,startBlock,endBlock,comment,commentTo)


    def issue(self,address,name,qty,units,nativeamount,custom):
        return self.api.issue(address,name,qty,units,nativeamount,custom)


    def issueFrom(self,fromAddress,toAddress,name,qty,units,nativeamount,custom):
        return self.api.issuefrom(fromAddress,toAddress,name,qty,units,nativeamount,custom)


    def listAddressTransactions(self,address,count,skip,verbose):
        return self.api.listaddresstransactions(addres,count,skip,verbose)


    def listAssets(self,asset):
         return self.api.listassets(asset)

    def listWalletTransactions(self,count,skip,includeWatchOnly,verbose):
        return self.api.listwallettransactions(count,skip,includeWatchOnly,verbose)


    def prepareLockUnspent(self,assetsToLock,lock):
        return self.api.preparelockunspent(assetsToLock,lock)


    def prepareLockUnspentFrom(self,fromAddress,assetsToLock,lock):
        return self.api.preparelockunspentfrom(fromAddress,assetsToLock,lock)

    def revoke(self,addresses,permissions,nativeamount,comment,commentTo):
        return self.api.revoke(addresses,permissions,nativeamount,comment,commentTo)


    def revokeFrom(self,fromAddress,toAddress,permissions,nativeamount,comment,commentTo):
        nativeamount = self.findDefaultMinimumPerOutput(nativeamount)
        return self.api.revokefrom(fromAddress,toAddress,permissions,nativeamount,comment,commentTo)

    def findDefaultMinimumPerOutput(self,nativeamount):
        if nativeamount is None:
            blockchainParams = self.getBlockChainParams()
            nativeamount = blockchainParams['minimum-per-output']
            return nativeamount
        else:
            return nativeamount


    def getBlockChainParams():
        self.api.getblockchainparams()



    def sendAssetFrom(self,fromAddress,toAddress,asset,qty,nativeamount,comment,commentTo):
        nativeamount = self.findDefaultMinimumPerOutput(nativeamount)
        return self.api.sendassetfrom(fromAddress,toAddress,asset,qty,nativeamount,comment,commentTo)


    def sendAssetToAddress(self,address,asset,qty,nativeamount,comment,commentTo):
        nativeamount = self.findDefaultMinimumPerOutput(nativeamount)
        return self.api.sendassettoaddress(address,asset,qty,nativeamount,comment,commentTo)

    def sendFromAddress(self,fromAddress,toAddress,amount,comment,commentTo):
        return self.api.sendfromaddress(fromAddress,toAddress,amount,comment,commentTo)


    def sendWithMetaData(self,address,amount,dataHex):
        return self.api.sendwithmetadata(address,amount,nativeamount)

    def sendWithMetaDataFrom(self,fromAddress,toAddress,amount,dataHex):
        return self.api.sendwithmetadatafrom(fromAddress,toAddress,amount,dataHex)

    def createRawTransaction(self,inputs,addresses):
        return self.api.createrawtransaction(inputs,addresses)

    def decodeRawTransaction(self,hexString):
        return self.api.decoderawtransaction(hexString)

    def getBlock(self,hashe,formate):
        return self.api.getblock(hashe,formate)

    def getRawTransaction(self,txId,verbose):
        return self.api.getrawtransaction(txId,verbose)

    def getTxOut(self,txId,vOut,unConfirmed):
        return self.api.gettxout(txId,vOut,unConfirmed)


    def listStreamKeyItems(self,streamID, key, verbose, count, start, localOrdering):
        return self.api.liststreamkeyitems(streamID,key,verbose,count,start,localOrdering)


    def listStreamItems(self,streamID,verbose,count,start,localOrdering):
        return self.api.liststreamitems(streamID,verbose,count,start,localOrdering)

    def listStreamKeys(self,streamID,key,verbose,count,start,localOrdering):
        return self.api.liststreamkeys(streamID,key,verbose,count,start,localOrdering)

    def listStreamPublishers(self,streamID,address,verbose,count,start,localOrdering):
        return self.api.listStreamPublishers(streamID,address,verbose,count,start,localOrdering)

    def listStreamPublisherItems(self,streamID,address,verbose,count,start,localOrdering):
        return self.api.liststreampublisheritems(streamID,address,verbose,count,start,localOrdering)



    def listPermissions(self,name):
        return self.api.listpermissions(name)

    def validateAddress(address):
        return self.api.validateaddress(address)

    def getAdminAddress(self):
        values = self.listPermissions("admin")
        print values
        for index, item in enumerate(values):
            print item['address']
            validationInfo = self.api.validateaddress(item['address'])
            if validationInfo['ismine']:
                return item['address']

    def createUserAddress(self,username):
        """ Change this to self_ """
        addr = self.api.getnewaddress()
        dct = {'USER_NAME':username, 'ADDRESS':addr}
        print dct
        address = self.getAdminAddress()
        txd = self.api.publishfrom(address, 'users_addresses',username,self.bin2hex(json.dumps(dct)))
        print txd
        return addr

    def createUserDetails(self,username,name,email):
        dct = {'USER_NAME':username,'NAME':name, 'EMAIL': email}
        admin_address = self.getAdminAddress()
        txd = self.api.publishfrom(admin_address,'users_details',username,self.bin2hex(json.dumps(dct)))
        return txd

    def createUserSession(username):
        dct = {'USER_NAME': username, 'SESSION_ID':'random_string', 'SESSION_IP':req.remote_addr}
        admin_address = self.getAdminAddress()
        txd = self.api.publishfrom(admin_address,'users_sessions',username,self.bin2hex(json.dumps(dct)))
        return txd


    def createUser(self,username,password,name):
        hashed = bcrypt.hashpw(password,bcrypt.gensalt())
        dct = {'USER_NAME':username, 'PASSWORD_HASH':hashed}
        print dct
        admin_address = self.getAdminAddress()
        print admin_address
        txd = self.api.publishfrom(admin_address,'users_details',username,self.bin2hex(json.dumps(dct)))
        print txd
        return txd

    def getTxOutData(self,txId,vout):
        return self.api.gettxoutdata(txId,vout)

    def publish(self,streamID,key,dataHex):
        return self.api.publish(streamID,key,dataHex)


    def listUnspent(minConf,maxConf,addresses):
        return self.api.listunspent(minConf,maxConf,addresses)
