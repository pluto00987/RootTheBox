'''
Created on Mar 15, 2012

@author: haddaway
'''
import logging #@UnusedImport
import tornado.websocket #@UnresolvedImport
from libs.SecurityDecorators import * #@UnusedWildImport
from libs.WebSocketManager import WebSocketManager

class WebsocketHandler(tornado.websocket.WebSocketHandler):
    
    def open(self): #@ReservedAssignment
        self.manager = WebSocketManager.Instance() #@UndefinedVariable
        self.manager.add_connection(self)
        
    def on_message(self, message):
        logging.warn("%s tried to send us [%s]!" % (self.request.remote_ip, message))
        if message == "load plox":
            self.manager.get_updates(self)
        
            
    def on_close(self):
        self.manager.remove_connection(self)