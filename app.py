from flask import Flask,render_template,request
from notification.Notification_Driver_Main import Notification_Driver_Main

import logging

app = Flask(__name__)


@app.route('/admin', methods = ['GET'])
def admin_UI():
    return render_template('admin.html',category_list = obj.get_categories())


@app.route('/admin', methods = ['POST'])
def admin_POST():
    obj.GenerateNotification(request.form['Category'], request.form['TriggerNotificationMsg'])
    return render_template('homepage.html', response_message = ' Successfuly Notification Sent')

@app.route('/subscriber', methods = ['POST'])
def subscriber_POST():
    obj.Subscribe(name = request.form['UserName'], email = request.form['UserEmail'], phone = request.form['UserPhone'], naggaro_portal_id = request.form['UserPortal'], subscribe_list = request.form.getlist('subscriptions'))
    return render_template('homepage.html', response_message = ' User Added and Subscribed')

@app.route('/subscriber', methods = ['GET'])
def subscriber_UI():
    return render_template('subscriber.html',category_list = obj.get_categories())

@app.route('/addCategories',methods = ['POST'])
def addCategories_POST():
    obj.addCategory(request.form['TriggerName'], request.form.getlist('mode'))
    return render_template('homepage.html', response_message = ' Category added')


@app.route('/addCategories',methods = ['GET'])
def addCategories_UI():
    return render_template('addCategories.html',modes_of_commnunication = obj.get_Modes_of_Communication())

@app.route('/')
def render_homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    obj = Notification_Driver_Main.getDriver()
    # obj.addCategory('EVENT', ['EMAIL', 'PORTAL'])
    # obj.addCategory('HOLIDAY', ['PORTAL'])
    # obj.Subscribe(name='Gaurav', email='gauravarora011@gmail.com', phone='7508819230',
    #               naggaro_portal_id='123', subscribe_list=['EVENT','HOLIDAY'])
    # obj.Subscribe(name='Nikhil', email='banwari@test.com', phone='9667519930',
    #               naggaro_portal_id='139174', subscribe_list=['EVENT'])
    # obj.GenerateNotification('EVENT','woohoo')
    app.run()