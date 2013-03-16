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

    def post(self):
            contato = Contato(nome=self.request.get('inputName'), email=self.request.get('inputEmail'),
                              message=self.request.get('comments'), dataContato=datetime.datetime.now().date())
            if contato.isValid():
                contato.save() 
            
            return  self.redirect('/')
            # enviar email
            
            # message=  mail.EmailMessage('mvmtecnologia@appspot.gserviceaccount.com', to='mvmtecnologia@gmail.com',
            # subject=self.request.get('nome'), body=self.request.get('message'))
            # message.Send()
        

application = webapp.WSGIApplication(
                                     [('/', HomePage),
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
    
    
