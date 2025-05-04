from time import *
from os import path
from Password_verification import Start_Password_verification
from Add_or_remove_users import Start_ADMIN_Password_verification, admin
from Branch_main_class import Admin_UX_UI
from Add_or_remove_students import look_student, add_student, remove_student

Start_Password_verification()

current_dir = path.dirname(path.abspath(__file__))
# 构建 students.json 文件的绝对路径
students_file_path = path.join(current_dir, 'students.json')

print('****************************************')
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
    try:
        number = int(input("请输入数字："))
    except ValueError:
        print("输入无效，请输入数字！")
        continue  # 跳过当前循环，继续下一次循环

    if number == 1:
        add_student()
    elif number == 2:
        remove_student()
    elif number == 3:
        look_student()
    elif number == 4:
        admin = Start_ADMIN_Password_verification()
        if admin:
            print("管理员登录成功！")
            Admin_UX_UI()
        else:
            print("管理员登录失败！")
    elif number == 5:  # 修复了这里的类型问题
        print('程序已退出！')
        exit()
    else:
        print("无效的选项，请输入 1 到 5 之间的数字！")