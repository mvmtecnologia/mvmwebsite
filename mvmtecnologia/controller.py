from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp._webapp25 import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Contato
import datetime   
"""
@author: matheus cardoso
@author: soliva

Copyright (C) 2013 MVM Tecnologia, Inc.

"""
 
class HomeHandler(RequestHandler):
    def get(self):
        #TODO:alterar isso quando for fazer o deploy em producaoo
        #self.response.out.write(template.render('pages/em-breve.html', {}))
        self.response.out.write(template.render('pages/home.html', {}))

   

class ContatoHandler(RequestHandler):
    emailHelper=None
          
    def post(self):
            if self.request.get('inputEmail'):
                self.emailHelper = self.request.get('inputEmail');
                
            contato = Contato(nome=self.request.get('inputName'),
                              email=self.emailHelper,
                              mensagem=self.request.get('comments'), 
                              dataContato=datetime.datetime.now().date())
            
            if contato.isValid():
                contato.put() 
                contato.enviarEmail()
        
                return  self.redirect('/')
            else:
                #TODO:melhorar isso.
                return  self.redirect('/')
                
           
        

application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/contato', ContatoHandler), ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
    
    
