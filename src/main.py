from time import *
from os import path
from Password_verification import Start_Password_verification
from Add_or_remove_users import Start_ADMIN_Password_verification,admin
from Branch_main_class import Admin_UX_UI
from Add_or_remove_students import look_student, add_student, remove_student

Start_Password_verification()

current_dir = path.dirname(path.abspath(__file__))
# 构建 users.json 文件的绝对路径
students_file_path = path.join(current_dir, 'students.json')

print('****************************************')#14
print('****************************************')
print('****************************************')
print('********欢迎使用学生信息管理系统********')
print('****************************************')
print('****************************************')
print('****************************************')
while True:
    print('请键入数字使用')
    print('1.录入')
    print('2.删除')
    print('3.查看')
    print('4.添加/删除用户账户(需要管理员授权)')
    print('5.退出')
    number = input('请输入数字：')
    if number  == '1':
        add_student()
    if number == '2':
        remove_student()
    if number == '3':
        look_student()
    if number =='4':
        admin = Start_ADMIN_Password_verification()
        if admin == True:
            print("管理员登录成功！")
            Admin_UX_UI()
        else:
            print("管理员登录失败！")
    if number == '5':
        print('程序已退出！')
        exit()
