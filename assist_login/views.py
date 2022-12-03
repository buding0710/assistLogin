import MySQLdb
from django.shortcuts import render, redirect
from .logining import Logining
from .models import Login_data


ip = ''
# 信息列表处理函数
def index(request):
    browser_type_choice = Login_data().browser_type_choice
    close_window_method_choice = Login_data().close_window_method_choice
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM assist_login_login_data")
        login_data = cursor.fetchall()
        # print(login_data)
    global ip
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    print("ip : ", ip)
    return render(request, 'assist_login/index.html', {'login_data': login_data, 'browser_type_choice': browser_type_choice, 'close_window_method_choice': close_window_method_choice})

# 信息新增处理函数
def add(request):
    if request.method == 'GET':
        browser_type_choice = Login_data().browser_type_choice
        close_window_method_choice = Login_data().close_window_method_choice
        # print(browser_type_choice)
        # print(close_window_method_choice)
        return render(request, 'assist_login/add.html', {'browser_type_choice': browser_type_choice, 'close_window_method_choice': close_window_method_choice})
    else:
        login_name = request.POST.get('login_name')
        login_url = request.POST.get('login_url')
        redirect1 = request.POST.get('redirect')
        username = request.POST.get('username')
        password = request.POST.get('password')
        browser_type = request.POST.get('browser_type', 'chrome')
        close_window_method = request.POST.get('close_window_method', 0)
        user_role = request.POST.get('user_role')
        quarter = request.POST.get('quarter')
        data_range = request.POST.get('data_range')
        remark = request.POST.get('remark')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO assist_login_login_data (login_name, login_url, redirect, username, password, browser_type, close_window_method, user_role, quarter, data_range, remark) "
                           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [login_name, login_url, redirect1, username, password, browser_type, close_window_method, user_role, quarter, data_range, remark])
            conn.commit()
        return redirect('../')

# 信息修改处理函数
def edit(request):
    if request.method == 'GET':
        browser_type_choice = Login_data().browser_type_choice
        close_window_method_choice = Login_data().close_window_method_choice
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM assist_login_login_data where id =%s", [id])
            login_data = cursor.fetchone()
        return render(request, 'assist_login/edit.html', {'login_data': login_data, 'browser_type_choice': browser_type_choice, 'close_window_method_choice': close_window_method_choice})
    else:
        id = request.POST.get("id")
        login_name = request.POST.get('login_name', '')
        login_url = request.POST.get('login_url', '')
        redirect1 = request.POST.get('redirect', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        browser_type = request.POST.get('browser_type', '')
        close_window_method = request.POST.get('close_window_method', '')
        user_role = request.POST.get('user_role', '')
        quarter = request.POST.get('quarter', '')
        data_range = request.POST.get('data_range', '')
        remark = request.POST.get('remark', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE assist_login_login_data set login_name=%s, login_url=%s, redirect=%s, username=%s, password=%s, browser_type=%s, close_window_method=%s, user_role=%s, quarter=%s, data_range=%s, remark=%s where id =%s",
                           [login_name, login_url, redirect1, username, password, browser_type, close_window_method, user_role, quarter, data_range, remark, id])
            conn.commit()
        return redirect('../')

# 信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM assist_login_login_data WHERE id =%s", [id])
        conn.commit()
    return  redirect('../')

# 信息登录处理函数
def login(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root1", db="assist", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM assist_login_login_data where id =%s", [id])
        login_data = cursor.fetchone()
    print(login_data)
    global ip
    Logining(login_data, clientip=ip).a163_com()
    return redirect('../')