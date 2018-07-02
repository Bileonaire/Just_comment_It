import models
import datetime
from models import User, Admin, Moderator, Comments


def signup():
    """creates user account"""
    username = input("Input username: ")
    password = input("Input password: ")
    confirm_password = input("Confirm password: ")

    while confirm_password != password:
        print ("error: passwords do not match")
        password = input("Input password: ")
        confirm_password = input("Confirm password: ")

    else:
        role = 'norm_user'
        comment =''
        last_seen = ''
        new_user = User(username,password,role,comment,last_seen)
        user_details= new_user.__dict__
        models.users.append(user_details)
        print(models.users)
        print ("Signup Successfull",user_details["username"],user_details["role"])
username =''
role=''
def login():
    """Authenticates login"""
    print("--------LOGIN----------")
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in models.users:
        if user['username'] == username and user['password'] == password:
            user['last_seen'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            print ("Login Successfull",user["username"],user["role"],"Logged in at:", user['last_seen'])
            username = user["username"]
            role = user['role']
            # return role
            return username
        else:
            print("Username or password invalid")

def add_comment():
    """ Comments"""
    comment_id = 1
    print("--------Create comment----------")
    author = username
    message = input("Enter comment: ")
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    new_comment = Comments(comment_id,author,message,time_stamp)
    comment= new_comment.__dict__
    models.comments.append(comment)
    print ("Comment", comment)


action = input("Type A to signup, B to login: ")
if action == "A":
    signup()
    action = input("Type A to signup, B to login: ")
    if action == "A":
        signup()
    login()
login()

add_comment()


login()


# norm_user = input("Type A to add comment, B to edit comment: ")admin =  input("Type A to add comment, B to edit comment, C to delete comment: ")
# moderator =  input("Type A to add comment, B to edit comment, C to delete comment: ")