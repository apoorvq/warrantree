import chain


class Carbon:


    def getInfo(self):
        step_one = chain.Chain()
        return unicode(step_one.getInfo())

    def userExists(username):
        step_one = chain.Chain()
        return unicode(step_one.listStreamKeyItems('user_details', username, true, 1, -1, true))

    def createUser(username,password,name):
        step_one = chain.Chain()
        return unicode(step_one.createUser(username,password,name))

    def getAdminAddress():
        step_one = chain.Chain()
        return unicode(step_one.lisPermissions(name))
