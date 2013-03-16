'''
Created on 12/01/2013

@author: soliva
'''
from google.appengine.ext import db

class Contato(db.Model):
    nome = db.StringProperty()
    email = db.EmailProperty()
    message = db.TextProperty()
    dataContato = db.DateProperty()

    def isValid(self):
        if self.nome and self.email and self.message and self.dataContato:
            return True
        else: False
        


