import models
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

signup()

# def login():
#     """controlls login """
#     username = input("Input username: ")
#     password = input("Input password: ")
#     u_name = User.user_details[username]
#     if password == u_name[0] and u_name[1] == 'norm_user':
#         print('logged in as normal user')
#         norm_user = User(username, password)
#         norm_user.add_comment(username)
    
#     elif u_name[0] == password and u_name[1] == 'moderator':
#         print('logged in as moderator')
#         mod_user = Moderator()

#     elif u_name[0] == password and u_name[1] == 'admin':
#         print('logged in as admin')
#         admin_user = Admin()
#     else:
#         print('wrong username or password')