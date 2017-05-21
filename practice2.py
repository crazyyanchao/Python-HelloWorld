
#--------------------python操作数据库--------------------
# Sqlite3 + SQLite
# Sqlite3是python的标准库，轻量级的关系型数据库
# Sqlite3是数据库SQLite的访问接口
# 移动或桌面应用
# createDB.py

# #!/usr/bin/env python
#
# import sqlite3
#
# # .db文件在当前目录下，自动创建
# conn = sqlite3.connect('china.db')
#
# # 获取数据库游标
# c = conn.cursor()
#
# # 执行创建表的操作
# c.execute('''CREATE TABLE category
#         (id int primary key ,sort int ,name text)''')
# c.execute('''CREATE TABLE book
#         (id int primary key ,
#         sort int,
#         name text,
#         price real,
#         category int,
#         FOREIGN KEY (category) REFERENCES category(id))''')
#
# # 保存
# conn.commit()
#
# # 关闭数据库连接
# conn.close()

#----------------------python操作MySQL-----------------------
