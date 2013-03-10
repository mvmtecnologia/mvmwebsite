'''
Created on 12/01/2013

@author: soliva
'''
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from webapp2 import RequestHandler

class HomePage(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/home.html', {}))


class Contato(db.Model):
    nome = db.StringProperty()
    email = db.EmailProperty()
    message = db.TextProperty()
    dataContato = db.DateProperty()
 


