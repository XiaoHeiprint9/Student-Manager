from time import *
from Add_or_remove_users import Start_ADMIN_Password_verification
from json import *
from os import path
from Add_or_remove_students import look_student, add_student, remove_student


def Admin_UX_UI():
    #Start_ADMIN_Password_verification()
    print('************************************************')#14
    print('************************************************')
    print('************************************************')
    print('********欢迎使用学生信息管理系统(管理员)********')
    print('************************************************')
    print('************************************************')
    print('************************************************')
    current_dir = path.dirname(path.abspath(__file__))
    # 构建 users.json 文件的绝对路径
    users_file_path = path.join(current_dir, 'users.json')
    students = {}
    while True:
        print('请键入数字使用')
        print('1.录入')
        print('2.删除')
        print('3.查看')
        print('4.查看用户账户')
        print('5.添加用户账户')
        print('6.删除用户账户')
        print('7.退出')
        number = input('请输入数字：')
        if number  == '1':
            add_student()
        if number == '2':
            remove_student()
        if number == '3':
            look_student()
        if number == '4':
            try:
                with open(users_file_path, 'r', encoding="utf-8") as user_file:
                    data = load(user_file)
                    users = data.get("users", [])
                    if not users:
                        print("没有用户账户信息！")
                    else:
                        print("用户账户信息如下：")
                        for index, user in enumerate(users, start=1):
                            print(f"{index}. 用户名: {user['name']}, 密码: {user['password']}")
            except FileNotFoundError:
                print("用户文件不存在！")
        if number =='5':
            user1 = input("请输入新的用户名：")
            user_password = input("请输入新用户的密码：")
            user_data = {"name": user1, "password": user_password}  # 修复此行
            try:
                with open(users_file_path, 'r', encoding="utf-8") as user_file:
                    data = load(user_file)
            except FileNotFoundError:
                # 如果文件不存在，初始化一个空的字典
                data = {"users": [], "Administrator_users": []}
            # 将新的用户数据添加到 users 列表中
            data["users"].append(user_data)
            # 将修改后的数据写回 JSON 文件
            with open(users_file_path, 'w', encoding="utf-8") as user_file:
                dump(data, user_file, indent=4, ensure_ascii=False)
            print('新用户创建成功!')
        if number == '6':
            try:
                with open(users_file_path, 'r', encoding="utf-8") as user_file:
                    data = load(user_file)
            except FileNotFoundError:
                print("用户文件不存在！")
                continue
            
            users = data.get("users", [])
            if not users:
                print("没有用户可以删除！")
                continue
            
            print("现有用户：")
            for index, user in enumerate(users, start=1):
                print(f"{index}. {user['name']}")
            
            user_input = int(input("请输入要删除的用户的序号："))
            if 1 <= user_input <= len(users):
                del users[user_input - 1]
                data["users"] = users
                with open(users_file_path, 'w', encoding="utf-8") as user_file:
                    dump(data, user_file, indent=4, ensure_ascii=False)
                print("用户已删除！")
            else:
                print("无效的序号，请重新输入。")
        if number == '7':
            print('程序已退出！')
            exit()
