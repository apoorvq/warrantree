import falcon

import carbon

import json

import middleware


class InfoResource(object):
	protection = middleware.ResourceProtection()
	@falcon.before(protection.process_request)
	def on_get(self, req, resp):
		info = carbon.Carbon()
		resp.body = info.getInfo()
		resp.status = falcon.HTTP_200

class RegisterResource(object):
	def on_post(self,req,resp):
		info = carbon.Carbon()
		if 'username' not in req.params or 'password' not in  req.params:
			raise falcon.HTTPBadRequest(
				'Username not provided or Password is Missing'
			)
		username = req.params.get('username')
		password = req.params.get('password')

		if info.userExists(username):
			raise falcon.HTTPBadRequest(
				'This username already exists please chose another username'
			)






api = falcon.API()
api.add_route('/info', InfoResource())
api.add_route('/register', RegisterResource())
