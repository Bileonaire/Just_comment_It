import models
import datetime
from models import User, Admin, Moderator, comments


def signup():
    """creates user account"""
    username = input("Input username: ")
    password = input("Input password: ")
    confirm_password = input("Confirm password: ")
    if confirm_password != password:
        print ("error: passwords do not match")
    else:
        role = 'norm_user'
        comment =''
        last_seen = ''
        new_user = User(username,password,role,comment,last_seen)
        user_details= new_user.__dict__
        models.users.append(user_details)
        print(models.users)
        print ("Signup Successfull",user_details["username"],user_details["role"])

def login():
    """Authenticates login"""
    print("--------LOGIN----------")
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in models.users:
        if user['username'] == username and user['password'] == password:
            user['last_seen'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            print ("Login Successfull",user["username"],user["role"],"Logged in at:", user['last_seen'])
        else:
            print("Username or password invalid")
            
signup()
login()