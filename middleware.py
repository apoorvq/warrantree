import falcon

import json

class ResourceProtection(object):
    def process_request(self,req,resp,params):
        if not req.auth:
            description = ('Hey you know what there is a thing called username and password')
            raise falcon.HTTPUnauthorized(falcon.HTTP_401,
            'You need to sign in my friend',
            description
            )
