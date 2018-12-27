1.本质是socket，flask使用的是werkzeug

2.配置--使用类对象赋值，config.py
    使用：app.config.from_object("config.DevelopmentConfig")

3.路由系统--使用本质的add_url_rule实现，router

4.CBV基于类视图--使用views.MethodView实现，CBV-view

5.请求和响应，application.py

6.session,__session

7.闪现，背后实现就是session，用完即焚， flash_app

8.请求扩展，请求前和请求后操作，常用登陆验证和权限控制，请求前后缓存操作，request-extend

9.中间件，test_middleware.py

10.蓝图，代理模式的程序控制，app作为代理者，接收请求分发给蓝图处理，pro_flask