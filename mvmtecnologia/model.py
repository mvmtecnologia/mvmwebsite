
from google.appengine.api import mail
from google.appengine.ext import db
import logging
'''
@author: matheus cardoso
@author: soliva
'''
"""
 Copyright (C) 2013 MVM Tecnologia, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
  http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 """
 
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
            logging.info('enviando email..')
            mail.send_mail(sender="contato@mvmtecnologia.com.br",
            to=self.email,
            subject="Contato MVMTecnologia",
            body='''Muito obrigado por entrar em contato conosco,
                    em breve estaremos retornando.
                 ''')    
            
            
            
            
