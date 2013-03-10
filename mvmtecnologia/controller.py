from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp._webapp25 import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Contato
import datetime

class HomePage(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/home.html', {}))


class ContatoPage(RequestHandler):
    def get(self): 
        self.response.out.write(template.render('pages/contato.html', {}))
    
    def post(self):
            contato = Contato(nome=self.request.get('nome'),email=self.request.get('email'),
                              message=self.request.get('message'),dataContato=datetime.datetime.now().date())
            contato.save() 
            self.response.out.write(template.render('pages/contato.html', {}))
            #enviar email
            
            #message=  mail.EmailMessage('mvmtecnologia@appspot.gserviceaccount.com', to='mvmtecnologia@gmail.com',
            #subject=self.request.get('nome'), body=self.request.get('message'))
            #message.Send()
        
        

class ProdutoServicoPage(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/produtos-servicos.html', {}))



application = webapp.WSGIApplication(
                                     [('/', HomePage),
                                      ('/contato', ContatoPage),
                                      ('/produtos-servicos', ProdutoServicoPage),
                                      
                                      
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
    
    