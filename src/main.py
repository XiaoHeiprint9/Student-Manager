from time import *
from Password_verification import Start_Password_verification
from Add_or_remove_users import Start_ADMIN_Password_verification,admin

Start_Password_verification()

print('****************************************')#14
print('****************************************')
print('****************************************')
print('********欢迎使用信息学生管理系统********')
print('****************************************')
print('****************************************')
print('****************************************')
students = {}
while True:
    print('请键入数字使用')
    print('1.录入')
    print('2.删除')
    print('3.查看')
    print('4.添加/删除用户账户(需要管理员授权)')
    print('5.退出')
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
            print(f"{index}. 姓名: {name}, 学号: {student_id}")
    if number =='4':
        admin = Start_ADMIN_Password_verification()
        if admin == True:
            print("管理员登录成功！")
        else:
            print("管理员登录失败！")
    if number == '5':
        print('程序已退出！')
        exit()
