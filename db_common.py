import records

# 获取数据库
db = records.Database('mysql+pymysql://ttkkcc126com:T9bd73mvT@119.29.193.147:3306/ttkkcc126com')
# 查询

# 得到所有数据
# print(rows.all())
# for v in rows:
#     print(v['col1'])
#     print(v['col2'])
    
    
'''
# 得到所有数据
print(rows.all())
# 字典形式展示
print(rows.all(as_dict=True))
# 获取第一个
print(rows.first())
# 以字典形式获取第一个
print(rows.first(as_dict=True))
# 排序字典
print(rows.first(as_ordereddict=True))
# 查询唯一的一个
print(rows.one())
'''

'''
#连接各种数据库
#PostgreSQL
# default
db = records.Database('postgresql://scott:tiger@localhost/mydatabase')
# psycopg2
db = records.Database('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
# pg8000
db = records.Database('postgresql+pg8000://scott:tiger@localhost/mydatabase')


#MySQL
# default
db = records.Database('mysql://scott:tiger@localhost/foo')
# mysqlclient (a maintained fork of MySQL-Python)
db = records.Database('mysql+mysqldb://scott:tiger@localhost/foo')
# PyMySQL
db = records.Database('mysql+pymysql://scott:tiger@localhost/foo')

#Oracle
db = records.Database('oracle://scott:tiger@127.0.0.1:1521/sidname')
db = records.Database('oracle+cx_oracle://scott:tiger@tnsname')

#Microsoft SQL Server
# pyodbc
db = records.Database('mssql+pyodbc://scott:tiger@mydsn')
# pymssql
db = records.Database('mssql+pymssql://scott:tiger@hostname:port/dbname')

#SQLite
# for a relative file path
db = records.Database('sqlite:///foo.db')
# for a absolute file path 
# UNIX/MAC
db = records.Database('sqlite:////absolute/path/to/foo.db')
# Windows
db = records.Database('sqlite:///C:\\path\\to\\foo.db')
# Windows using raw string
db = records.Database(r'sqlite:///C:\path\to\foo.db')
# for a memory database
db = records.Database('sqlite://')
'''