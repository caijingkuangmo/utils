不难发现IndexView.as_view(name='index')的执行结果还是一个函数
我们看as_view里源码：
    请求到来前：
        1.定义 返回 内部自定义的一个view函数对象
                def view(*args, **kwargs):
                    self = view.view_class(*class_args, **class_kwargs)
                    return self.dispatch_request(*args, **kwargs)
        2.给view函数套装饰器
                if cls.decorators:
                    view.__name__ = name
                    view.__module__ = cls.__module__
                    for decorator in cls.decorators:
                        view = decorator(view)
        3.给view绑定各种属性：视图类，别名，请求方法
            view.view_class = cls
            view.__name__ = name
            view.methods = cls.methods
     
    请求到来时：
        执行view函数，实例IndexView视图类对象，执行dispatch_request方法
        在dispatch_request函数干了一件啥事了，获取请求里的method，然后去视图对象里getattr映射，并执行该方法