import chain
import falcon

class Carbon:


    def getInfo(self):
        step_one = chain.Chain(self)
        return unicode(step_one.getInfo())

    def getUserAddress(self,username):
        step_one = chain.Chain(self)
        try:
            user_records = unicode(step_one.listStreamKeyItems('users_addresses',username,True,1,-1,True))
            if len(user_records)





    def userExists(self,username):
        step_one = chain.Chain(self)
        users_details = unicode(step_one.listStreamKeyItems('users_details', username, True, 1, -1, True))
        print "User: " + users_details
        length_of_the_user = len(users_details)
        print length_of_the_user
        if  length_of_the_user > 2:
            print 'User already exist'
            return True
        else:
            print 'User Does not Exist'
            return False

    def createUser(self,username,password,name):
        step_one = chain.Chain(self)
        return unicode(step_one.createUser(username,password,name))

    def createUserAddress(self,username):
        step_one = chain.Chain(self)
        return unicode(step_one.createUserAddress(username))

    def createUserDetails(self,username,name,email):
        step_one = chain.Chain(self)
        return unicode(step_one.createUserDetails(username,name,email))

    def getAdminAddress():
        step_one = chain.Chain(self)
        return unicode(step_one.lisPermissions(name))

    def grantPermision(self,username,permissions):
        step_one = chain.Chain(self)
        try:
            """
            Do Something Here
            """
            if self.userExists(username):
                addres = self.getUserAddress





    def getDataFromDataItem(self,dataItem):
        step_one = chain.Chain(self)
        if type(dataItem) is str:
            dataHex = dataItem
            return True
        else:
            vout = dataItem['vout']
            txId = dataItem['txid']
            datahex = unicode(step_one.getTxOutData(txId,vout))
            return False
