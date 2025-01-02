import json
with open('users.json','w'):
    pass
# 定义JSON对象
data = {
    "users": [
        {"name": "Alice", "password": "123456"},
        {"name": "Bob", "password": "114514"}
    ]
}

# 将JSON对象写入文件
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

