#coding=utf-8
import MySQLdb
import random

if __name__=='__main__':
    db = MySQLdb.connect('localhost','root','yeyememe','craw')
    # cursor = db.cursor()
    # cursor.execute("SELECT VERSION()")
    # data = cursor.fetchone()
    # print data
    # db.close()
    try:
        cursor = db.cursor()
        sql = 'insert into question(title,content,user_id,created_date,comment_count) values ("XXX","XXX",1,now(),0)'
        cursor.execute(sql)
        qid=cursor.lastrowid
        db.commit()
        print qid
    except Exception,e:
        print e
        db.rollback()
    db.close()
