import falcon

import carbon

import json

import middleware


class InfoResource(object):
	def on_get(self, req, resp):
		info = carbon.Carbon()
		resp.body = info.getInfo()
		resp.status = falcon.HTTP_200

class RegisterResource(object):
	"""
	More Documentation Needed Here
	"""
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
		name = username
		user = info.createUser(username,password,name)
		print user
		useraddress = info.createUserAddress(username)
		print useraddress
		"""
		Granting send and recieve permissions to user.
		"""

		permissions = "send,receive"

		user_permission = info.

		print permissions


class GetDataFromImages(object):

	def on_post(self,req,resp):
		info = carbon.Carbon()

		if (req.)



api = falcon.API(middleware=[


])


api.add_route('/info', InfoResource())
api.add_route('/register', RegisterResource())
