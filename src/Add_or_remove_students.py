from os import path
from json import *

current_dir = path.dirname(path.abspath(__file__))
# 构建 users.json 文件的绝对路径
students_file_path = path.join(current_dir, 'students.json')
"""
with open(students_file_path,'w'):
    pass
"""
sdata = {
    "students": []
}

# with open(students_file_path, 'w', encoding='utf-8') as student_file:
#     dump(data, sf, ensure_ascii=False, indent=4)

def look_student():
    try:
        with open(students_file_path, 'r', encoding="utf-8") as students_file:
            data = load(students_file)
            students = data.get("students", [])
            if not students:
                print("没有学生信息！")
            else:
                print("学生信息如下：")
                for index, student in enumerate(students, start=1):
                    print(f"{index}. 姓名: {student['name']}, 学号: {student['Student_ID']}")
    except FileNotFoundError:
        print("文件不存在！")
        return 0

def add_student():
    student1 = input("请输入学生姓名：")
    student2 = input("请输入学号：")
    student_data = {"name": student1, "Student_ID": student2}  # 学生数据
    try:
        # 尝试读取文件内容
        with open(students_file_path, 'r', encoding="utf-8") as student_file:
            data = load(student_file)
    except FileNotFoundError:
        # 如果文件不存在，初始化一个空的字典
        data = {"students": []}

    # 将新的学生数据添加到 students 列表中
    data["students"].append(student_data)

    # 将修改后的数据写回 JSON 文件
    with open(students_file_path, 'w', encoding="utf-8") as student_file:
        dump(data, student_file, indent=4, ensure_ascii=False)

    print('录入成功!')

def remove_student():
    try:
        with open(students_file_path, 'r', encoding="utf-8") as student_file:
            data = load(student_file)
    except FileNotFoundError:
        print("学生文件不存在！")
        return 0
    students = data.get("students", [])
    if not students:
        print("没有学生可以删除！")
        return 0

    print("学生列表：")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")
            
    user_input = int(input("请输入要删除的学生的序号："))
    if 1 <= user_input <= len(students):
        del students[user_input - 1]
        data["students"] = students
        with open(students_file_path, 'w', encoding="utf-8") as student_file:
            dump(data, student_file, indent=4, ensure_ascii=False)
        print("学生已删除！")
    else:
        print("无效的序号，请重新输入。")