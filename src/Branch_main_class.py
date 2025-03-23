from time import *
from Password_verification import Start_Password_verification
from Add_or_remove_users import Start_ADMIN_Password_verification,admin
from json import *

Start_ADMIN_Password_verification()

print('************************************************')#14
print('************************************************')
print('************************************************')
print('********欢迎使用信息学生管理系统(管理员)********')
print('************************************************')
print('************************************************')
print('************************************************')
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
        students1 = input('请输入学生姓名：')
        students2 =input('请输入学号：')
        print('录入成功！')
        students.setdefault(students1,students2)
    if number == '2':
        # 使用 enumerate() 函数给列表中的每个元素标上序号
        for index, item in enumerate(students, start=1):
            print(f"{index}. {item}")
        user_input = int(input("请输入要删除的学生的序号："))
        # 计算对应的索引并删除列表中的元素
        if 1 <= user_input <= len(students):
            del students[user_input - 1]
            print("已删除 {user_input} 。")
        else:
            print("无效的序号，请重新输入。")
        # 输出删除后的列表
        print("删除后的列表：")
        for index, item in enumerate(students, start=1):
            print(f"{index}. {item}")
        if students == None:
            print('系统内无学生信息！')
    if number == '3':
        for index, (name, student_id) in enumerate(students.items(), start=1):
            print(f"{index}. 姓名：{name}, 学号：{student_id}")
    if number == '4':
        try:
            with open("users.json", "r", encoding="utf-8") as user_file:
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
            with open("users.json", "r", encoding="utf-8") as user_file:
                data = load(user_file)
        except FileNotFoundError:
            # 如果文件不存在，初始化一个空的字典
            data = {"users": [], "Administrator_users": []}
        # 将新的用户数据添加到 users 列表中
        data["users"].append(user_data)
        # 将修改后的数据写回 JSON 文件
        with open("users.json", "w", encoding="utf-8") as user_file:
            dump(data, user_file, indent=4, ensure_ascii=False)
        print('新用户创建成功!')
    if number == '6':
        try:
            with open("users.json", "r", encoding="utf-8") as user_file:
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
            with open("users.json", "w", encoding="utf-8") as user_file:
                dump(data, user_file, indent=4, ensure_ascii=False)
            print("用户已删除！")
        else:
            print("无效的序号，请重新输入。")
    if number == '7':
        print('程序已退出！')
        exit()
