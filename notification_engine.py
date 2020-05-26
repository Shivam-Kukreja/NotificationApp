from abc import ABCMeta, abstractmethod

class NotificationEngine(metaclass=ABCMeta):


    def __init__(self, name: str):
        self.name = name

    _INSTANCE = None

    @classmethod
    def singleton(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = cls.create_singleton()
        return cls._INSTANCE

    @classmethod
    @abstractmethod
    def create_singleton(cls):
        pass

    @abstractmethod
    def trigger_notification():
        pass

class Email_NotificationEngine(NotificationEngine):

    def __init__(self):
        super().__init__('Email Notification Class')

    @classmethod
    def create_singleton(cls):
        return Email_NotificationEngine()

    def trigger_notification(self, users,text):
        email_subscription=[]
        for u in users:
            email_subscription.append(u.email)
        print("For users subscribed {}".format(email_subscription))
        print("Email has been Triggered")
        print("Template Message: {}".format(text))

class SMS_NotificationEngine(NotificationEngine):

    def __init__(self):
        super().__init__('SMS Notification Class')

    @classmethod
    def create_singleton(cls):
        return SMS_NotificationEngine()

    def trigger_notification(self,users,text):
        sms_subscription=[]
        for u in users:
            sms_subscription.append(u.phone)
        print("For users subscribed {}".format(sms_subscription))
        print("SMS has been Triggered")
        print("Template Message: {}".format(text))

class Portal_NotificationEngine(NotificationEngine):

    def __init__(self):
        super().__init__('Portal Notification Class')

    @classmethod
    def create_singleton(cls):
        return Portal_NotificationEngine()

    def trigger_notification(self,users,text):
        portal_subscription=[]
        for u in users:
            portal_subscription.append(u.naggaro_portal_id)
        print("For users subscribed {}".format(portal_subscription))
        print("Portal Notification has been Triggered")
        print("Template Message: {}".format(text))