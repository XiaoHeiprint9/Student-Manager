import json
from time import sleep
from os import system, path

logo = """
 /$$      /$$               /$$                /$$$$$$$          
| $$$    /$$$              | $$               | $$__  $$         
| $$$$  /$$$$ /$$$$$$  /$$$$$$$ /$$$$$$       | $$  \ $$/$$   /$$
| $$ $$/$$ $$|____  $$/$$__  $$/$$__  $$      | $$$$$$$| $$  | $$
| $$  $$$| $$ /$$$$$$| $$  | $| $$$$$$$$      | $$__  $| $$  | $$
| $$\  $ | $$/$$__  $| $$  | $| $$_____/      | $$  \ $| $$  | $$
| $$ \/  | $|  $$$$$$|  $$$$$$|  $$$$$$$      | $$$$$$$|  $$$$$$$
|__/     |__/\_______/\_______/\_______/      |_______/ \____  $$
                                                        /$$  | $$
                                                       |  $$$$$$/
                                                        \______/
██╗  ██╗██╗ █████╗  ██████╗ ██╗  ██╗███████╗██╗
╚██╗██╔╝██║██╔══██╗██╔═══██╗██║  ██║██╔════╝██║
 ╚███╔╝ ██║███████║██║   ██║███████║█████╗  ██║
 ██╔██╗ ██║██╔══██║██║   ██║██╔══██║██╔══╝  ██║
██╔╝ ██╗██║██║  ██║╚██████╔╝██║  ██║███████╗██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝"""
print(logo)

# 获取当前文件的目录
current_dir = path.dirname(path.abspath(__file__))
# 构建 users.json 文件的绝对路径
users_file_path = path.join(current_dir, 'users.json')
with open(users_file_path, 'w'):
    pass
# 定义 JSON 对象

udata = {
    "users": [
        {"name": "Alice", "password": "123456"},
        {"name": "Bob", "password": "114514"}
    ],
    "Administrator_users": [
        {"admin_username": "Admin", "admin_password": "admin"}
    ]
}

# 将 JSON 对象写入文件
with open(users_file_path, 'w', encoding='utf-8') as file:
    json.dump(udata, file, ensure_ascii=False, indent=4)

# 打开 users.json 文件并加载数据
with open(users_file_path, 'r') as file:
    data = json.load(file)

# 定义一个函数以启动密码验证流程
def Start_Password_verification():
    # 设置密码尝试次数为 3
    Number_Of_Password_Trials = 3
    # 当密码尝试次数大于 0 时
    while Number_Of_Password_Trials > 0:
        # 获取用户输入的用户名和密码
        user_input = input("请输入用户名: ")
        password_input = input("请输入密码: ")

        # 遍历数据中的用户
        for user in data['users']:
            
            # 如果用户名和密码匹配
            if user['name'] == user_input and user['password'] == password_input:
                # 打印信息并暂停 3 秒
                print('用户信息正确')
                sleep(3)
                # 打印信息并暂停 3 秒
                print('正在进入系统...')
                sleep(3)
                # 返回函数
                return 0

        # 减少密码尝试次数
        Number_Of_Password_Trials -= 1
        # 打印信息和剩余尝试次数
        print('用户名或密码错误')
        print('请重试!')

    # 打印信息并暂停 3 秒
    print('密码错误次数过多')
    sleep(3)
    # 打印信息并暂停 3 秒
    print('正在删除系统...')
    sleep(3)
    # 打印完成信息
    print('Done!')
    sleep(1)
    # 清屏
    system('cls')
    # 退出程序
    exit()