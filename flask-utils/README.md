1.本质是socket，flask使用的是werkzeug

2.配置--使用类对象赋值，config.py
    使用：app.config.from_object("config.DevelopmentConfig")

3.路由系统--使用本质的add_url_rule实现，router

4.CBV基于类视图--使用views.MethodView实现，CBV-view

5.请求和响应，application.py

6.session,__session