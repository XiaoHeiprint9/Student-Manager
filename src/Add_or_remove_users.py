from time import sleep
from os import system
from  platform import system
import json
admin = False
# 定义一个清屏函数
def clear_screen():
    # Determine the current operating system
    if system() == "Windows":
        # If it's a Windows system, execute the clear screen command
        system('cls')
    else:
        # If it's not a Windows system, execute the clear screen command
        system('clear')
# Define a function to modify the value of the global variable admin

def modify_global():
    # Declare admin as a global variable
    global admin
    # Set the value of admin to True
    admin = True

"""
with open('users.json','w'):
    pass
# 定义JSON对象
data = {
    "users": [
        {"name": "Alice", "password": "123456"},
        {"name": "Bob", "password": "114514"}
    ],
    "Administrator_users": [
        {"admin_username": "Admin", "admin_password": "admin"}
    ]
}
"""

# # 将JSON对象写入文件
# with open('users.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4) 27 2
with open('users.json', 'r') as ad_file:
    data = json.load(ad_file)

def Start_ADMIN_Password_verification():
    # Set the number of password trials to 3
    Number_Of_Password_Trials = 3
    # While the number of password trials is greater than 0
    while Number_Of_Password_Trials > 0:
        # Get the user input for username and password
        aduser_input = input("请输入管理员用户名: ")
        adpassword_input = input("请输入管理员密码: ")

        # Loop through the users in the data
        for admin_user in data['Administrator_users']:
            
            # If the username and password match
            if admin_user['admin_username'] == aduser_input and admin_user['admin_password'] == adpassword_input:
                # Print a message and sleep for 3 seconds
                print('用户信息正确')
                sleep(3)
                # Print a message and sleep for 3 seconds
                modify_global()
                admin == True
                # Return from the function
                return True

        # Decrement the number of password trials
        Number_Of_Password_Trials -= 1
        # Print a message and the number of remaining trials
        print('用户名或密码错误')
        print('请重试!')

    # Print a message and sleep for 3 seconds
    print('密码错误次数过多')
    sleep(3)
    # Print a message and sleep for 3 seconds
    print('退出系统...')
    sleep(3)
    # Print a message
    print('Done!')
    sleep(1)
    # Clear the screen
    clear_screen()
    # Exit the program
    exit()
    if admin == True:
            pass
    else:
            pass