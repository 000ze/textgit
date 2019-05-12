import pymysql
def connectdb():
    print('连接到 mysql服务器...')
    db=pymysql.connect('localhost','root','263312zx','TESTDB')
    print('连接上了...')
    return db
def createtable(db):
    cursor=db.cursor()
    cursor.execute('DROP TABLE IF EXISTS Student')
    sql='''CREATE TABLE Student(ID CHAR(10) NOT NULL,NAME CHAR(8) NOT NULL,Grade INT )'''
    cursor .execute (sql)
def insertdb(db):
    cursor=db.cursor()
    sql='''INSERT INTO Student
           VALUES('001','ca',70),
                 ('002','la',70),
                 ('003','ga',70),
                 ('004','pa',70)'''
    try:
        cursor.execute(sql)
        db.commit()
    except:
         print('error')


def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    # sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM Student"
    try:
        # 执行SQL语句
        # cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            # 打印结果
            print("ID: %s, Name: %s, Grade: %d" % \
                (ID, Name, Grade))
    except:
        print("Error: unable to fecth data")
def deletedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        print
        '删除数据失败!'
        # 发生错误时回滚
        db.rollback()

def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print
        '更新数据失败!'
        # 发生错误时回滚
        db.rollback()

def closedb(db):
    db.close()

def main():
    db = connectdb()  # 连接MySQL数据库
    # createtable(db)  # 创建表
    insertdb(db)  # 插入数据
    print('\n插入数据后:')
    querydb(db)
    deletedb(db)  # 删除数据
    print('\n删除数据后:')
    querydb(db)
    updatedb(db)  # 更新数据
    print('\n更新数据后:')
    querydb(db)
    closedb(db)  # 关闭数据库

if __name__ == '__main__':
    main()







