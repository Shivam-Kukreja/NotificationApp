from notification.user_data import User_Data
from notification.notification_engine import Email_NotificationEngine,Portal_NotificationEngine,SMS_NotificationEngine
from notification.notification_categories import NotificationCategory

class Notification_Driver_Main:
   __instance = None
   Categories_to_InstanceMap = {}
   Notification_Engine_Map = {}

   @staticmethod
   def getDriver():
      if Notification_Driver_Main.__instance == None:
         Notification_Driver_Main.Notification_Engine_Map['EMAIL'] = Email_NotificationEngine.singleton()
         Notification_Driver_Main.Notification_Engine_Map['SMS'] = SMS_NotificationEngine.singleton()
         Notification_Driver_Main.Notification_Engine_Map['PORTAL'] = Portal_NotificationEngine.singleton()
         Notification_Driver_Main()
      return Notification_Driver_Main.__instance

   def __init__(self):
      if Notification_Driver_Main.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Notification_Driver_Main.__instance = self

   def addCategory(self,Category_Name,Modes_for_Communication):
      new_category_instance = NotificationCategory(Category_Name)
      for m in Modes_for_Communication:
          new_category_instance.attach_engine(Notification_Driver_Main.Notification_Engine_Map[m])
      Notification_Driver_Main.Categories_to_InstanceMap[Category_Name] = new_category_instance

   def Subscribe(self,name,email,phone,naggaro_portal_id,subscribe_list):
       new_user = User_Data(name,email,phone,naggaro_portal_id)
       print("New User Created")
       for s in subscribe_list:
          Notification_Driver_Main.Categories_to_InstanceMap[s].subscribe(new_user)
          print("User subscribed to ->" + s)

   @staticmethod
   def get_categories():
      return Notification_Driver_Main.Categories_to_InstanceMap.keys()

   @staticmethod
   def get_Modes_of_Communication():
      return Notification_Driver_Main.Notification_Engine_Map.keys()

   def GenerateNotification(self,category_name,text):
      Notification_Driver_Main.Categories_to_InstanceMap[category_name].send_notification(text)