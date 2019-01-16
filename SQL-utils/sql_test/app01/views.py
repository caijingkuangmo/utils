from django.shortcuts import render, HttpResponse
from app01 import models
from django.db import connection


# Create your views here.

def db_search(request, *args, **kwargs):

    return HttpResponse("search ok")







def db_init(request, *args, **kwargs):
    cursor = connection.cursor()
    sql_list = [
        '''
        INSERT INTO app01_classlist (caption)
        VALUES
            ('三年二班'),
            ('一年三班'),
            ('三年一班');
        ''',
        '''
        INSERT INTO app01_teacher (tname)
        VALUES
            ('波多'),
            ('苍空'),
            ('饭岛');
        ''',
        '''
        INSERT INTO app01_student (sname, gender, class_obj_id)
        VALUES
            ('钢蛋', 1, 1),
            ('铁锤', 1, 1),
            ('山炮', 0, 2);
        ''',
        '''
        INSERT INTO app01_course (cname, teacher_id)
        VALUES
            ('生物', 1),
            ('体育', 1),
            ('物理', 2);
        ''',
        '''
        INSERT INTO app01_score (student_id, course_id, number)
        VALUES
            (1, 1, 60),
            (1, 2, 59),
            (2, 2, 100);
        ''',
    ]
    for sql in sql_list:
        cursor.execute(sql)
    return HttpResponse("init ok")

def db_create(request, *args, **kwargs):
    return HttpResponse("create ok")

def db_update(request, *args, **kwargs):
    return HttpResponse("update ok")