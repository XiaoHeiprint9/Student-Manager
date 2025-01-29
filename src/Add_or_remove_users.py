from time import sleep
from os import system
import json
# with open('users.json','w'):
#     pass
# # 定义JSON对象
# data = {
#     "users": [
#         {"name": "Alice", "password": "123456"},
#         {"name": "Bob", "password": "114514"}
#     ]
# }

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
                print('正在进入系统...')
                sleep(3)
                # Return from the function
                return 0

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
    system('cls')
    # Exit the program
    exit()