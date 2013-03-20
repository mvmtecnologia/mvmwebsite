'''
Created on 12/01/2013
@author: matheus cardoso
@author: soliva
'''
from google.appengine.api import mail
from google.appengine.ext import db
import logging

class Contato(db.Model):
    '''
    classe responsavel em representar o
    contato feito pelo cliente
    '''
    nome = db.StringProperty()
    email = db.EmailProperty()
    mensagem = db.TextProperty()
    dataContato = db.DateProperty()

    
    def isValid(self):
        if self.nome and self.email and self.mensagem and self.dataContato:
            return True
        else: False
     
    
    def enviarEmail(self):
            logging.info('enviando email')
            mail.send_mail(sender="mvmtecnologia@gmail.com",
            to="solivavinicius@gmail.com>",
            subject="Contato MVMTecnologia",
            body=self.mensagem)    
            
            
            
            