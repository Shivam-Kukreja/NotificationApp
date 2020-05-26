import logging

class NotificationCategory:

    def __init__(self,type):
        self.type = type
        self.user_list = []
        self.engines = []

    def attach_engine(self,NotificationEngine):
        self.engines.append(NotificationEngine)

    def subscribe(self,user):
        self.user_list.append(user)
        logging.info('User Succesfully Subscribed')

    def send_notification(self,text):
        for engine in self.engines:
            engine.trigger_notification(self.user_list,text)