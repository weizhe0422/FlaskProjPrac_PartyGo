from flask import Blueprint
from user.models import User

user_page = Blueprint('user_page',__name__)

@user_page.route('/login')
def log_in():
    user = User(name='WeiZhe',email='WeiZhe@gmail.com',password='123456')
    user.save()
    
    return "Hello {}, your email is {}!".format(user.name,user.email)
    #return "this is login page"