# Notification App

## Steps to use
1. Install the requirement using 
	>pip install -r requirements.txt
2. To initiate flask server
	>python app.py

Server will be initiated on the localhost:5000

## Constraints
* Mode of Communication is restricted to 3 types :
	* EMAIL
	* SMS
	* PORTAL TRIGGER

> Any Change in this will require changes in the Class

* The Notification Categories needs to be initialized during runtime with any combination of these 3 modes of communication 

## Design Pattern Followed

Classes :

* **NotificationEngine**
	* Singleton
	* Abstract

*This class captures all the common utilities for the different modes of communication. This is an abstract class where the child class needs to store communication related details(eg. Connection Endpoint)*

* **NotificationCategory**
	* Observer 

*This class helps creating new categories for sending out notification and attaching the relevant modes of communication and thus enabling observer pattern*

* **Notification_Driver_Main**
	* Singleton

*This class drives the whole process of notification triggers by maintaining maps for the NotificationEngine and NotificationCategory Objects*


![Class Diagram](https://github.com/Silvercaty/NotificationApp/blob/master/DesignDiagram/NotificationClassStructure.png)
	
