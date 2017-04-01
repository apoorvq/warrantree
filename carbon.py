import chain


class Carbon:


    def getInfo(self):
        step_one = chain.Chain()
        return unicode(step_one.getInfo())

    def userExists(self,username):
        step_one = chain.Chain()
        return unicode(step_one.listStreamKeyItems('users_details', username, True, 1, -1, True))

    def createUser(self,username,password,name):
        step_one = chain.Chain()
        return unicode(step_one.createUser(username,password,name))

    def getAdminAddress():
        step_one = chain.Chain()
        return unicode(step_one.lisPermissions(name))
