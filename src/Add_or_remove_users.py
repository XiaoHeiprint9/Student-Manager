from time import sleep
from os import system, path
import json

# 全局变量
admin = False

def modify_global():
    # 声明 admin 为全局变量
    global admin
    # 设置 admin 为 True
    admin = True

# 获取当前文件所在目录
current_dir = path.dirname(path.abspath(__file__))
# 构建 users.json 文件的绝对路径
users_file_path = path.join(current_dir, 'users.json')

# 初始化用户数据
def initialize_users_file():
    # 如果文件不存在，创建并初始化
    if not path.exists(users_file_path):
        data = {
            "Administrator_users": [
                {"admin_username": "admin", "admin_password": "123456"}
            ]
        }
        with open(users_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("已创建初始用户文件。")

# 管理员密码验证
def Start_ADMIN_Password_verification():
    # 初始化用户文件
    initialize_users_file()

    # 尝试加载用户数据
    try:
        with open(users_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("用户文件不存在！")
        return False
    except json.JSONDecodeError:
        print("用户文件格式错误！")
        return False

    # 检查是否有管理员账户信息
    if 'Administrator_users' not in data or not data['Administrator_users']:
        print("用户文件中没有管理员账户信息！")
        return False

    # 设置密码尝试次数
    Number_Of_Password_Trials = 3
    while Number_Of_Password_Trials > 0:
        aduser_input = input("请输入管理员用户名: ")
        adpassword_input = input("请输入管理员密码: ")

        # 验证管理员账户
        for admin_user in data['Administrator_users']:
            if admin_user.get('admin_username') == aduser_input and admin_user.get('admin_password') == adpassword_input:
                print('用户信息正确')
                sleep(3)
                modify_global()
                return True

        # 减少尝试次数
        Number_Of_Password_Trials -= 1
        print('用户名或密码错误')
        print(f'请重试! 剩余尝试次数：{Number_Of_Password_Trials}')

    print('密码错误次数过多')
    sleep(3)
    print('退出系统...')
    sleep(3)
    system('cls')
    exit()