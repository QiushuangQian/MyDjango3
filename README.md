# MyDjango3
第九章

Session操作：
读写：
#获取k1的值，k1不存在则报错
request.session['k1']
#获取k1的值，k1不存在则设为空值
request.session.get['k1','']
request.session.setdefault('k1','')
#设置session的值，键为k1值为123
request.session['k1'] = 123
#删除Session中k1的数据
del request.session['k1']
#删除整个Session
request.session.clear()
#获取Session的键
request.session.keys()
#获取Session的值
request.session.values()
#获取Session的session_key(django_session字段session_key)
request.session.session_key
