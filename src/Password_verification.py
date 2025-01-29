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
    print('正在删除系统...')
    sleep(3)
    # Print a message
    print('Done!')
    sleep(1)
    # Clear the screen
    system('cls')
    # Exit the program
    exit()


