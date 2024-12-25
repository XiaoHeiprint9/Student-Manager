import json
from time import sleep
from os import system

# 打开 users.json 文件并加载数据
with open('users.json', 'r') as file:
    data = json.load(file)

# 定义一个函数以启动密码验证过程
def Start_Password_verification():
    # 设置密码尝试次数为3
    Number_Of_Password_Trials = 3
    # 当密码尝试次数大于0时
    while Number_Of_Password_Trials > 0:
        # 获取用户输入的用户名和密码
        user_input = input("请输入用户名: ")
        password_input = input("请输入密码: ")

        # 遍历数据中的用户
        for user in data['users']:
            
            # 如果用户名和密码匹配
            if user['name'] == user_input and user['password'] == password_input:
                # 打印消息并休眠3秒
                print('用户信息正确')
                sleep(3)
                # 打印消息并休眠3秒
                print('正在进入系统...')
                sleep(3)
                # 从函数返回
                return  

        # 减少密码尝试次数
        Number_Of_Password_Trials -= 1
        # 打印消息
        print('用户名或密码错误')
        print('请重试')

    # 打印消息并休眠3秒
    print('密码错误次数过多')
    sleep(3)
    # 打印消息并休眠3秒
    print('正在删除系统...')
    sleep(3)
    # 打印消息
    print('Done!')
    sleep(1)
    # 清除屏幕
    system('cls')
    # 退出程序
    exit()

"""
# 原始代码
import json
from time import sleep
from os import system

# Open the users.json file and load the data
with open('users.json', 'r') as file:
    data = json.load(file)

# Define a function to start the password verification process
def Start_Password_verification():
    # Set the number of password trials to 3
    Number_Of_Password_Trials = 3
    # While the number of password trials is greater than 0
    while Number_Of_Password_Trials > 0:
        # Get the user input for username and password
        user_input = input("请输入用户名: ")
        password_input = input("请输入密码: ")

        # Loop through the users in the data
        for user in data['users']:
            
            # If the username and password match
            if user['name'] == user_input and user['password'] == password_input:
                # Print a message and sleep for 3 seconds
                print('用户信息正确')
                sleep(3)
                # Print a message and sleep for 3 seconds
                print('正在进入系统...')
                sleep(3)
                # Return from the function
                return  

        # Decrement the number of password trials
        Number_Of_Password_Trials -= 1
        # Print a message and the number of remaining trials
        print('用户名或密码错误')
        print(f'你还有{Number_Of_Password_Trials}机会')

    # Print a message and sleep for 3 seconds
    print('密码错误次数过多')
    sleep(3)
    # Print a message and sleep for 3 seconds
    print('正在删除系统...')
    sleep(3)
    # Print a message
    print('Done!')
    sleep(1)
    # Clear the screen
    system('cls')
    # Exit the program
    exit()

"""