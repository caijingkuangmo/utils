 flask路由有点特殊，用装饰器实现的
 
 第一步：执行app.route函数 
    def route(self, rule, **options):
        #rule = '/'
        #options  ->  methods=['GET', 'POST'], endpoint='n1'
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
执行结果：返回decorator函数，并在上面过程传入了参数实现闭包
        所有此时在视图函数的结果为  @decorator
 
第二步：@decorator  --> 执行decorator(index)函数
        在这个过程中，我们发现它执行了 self.add_url_rule这么一个函数
        它干了一件啥事了，就是把url和视图函数添加到映射表里
         
从上面的分析过程，我们可以得出：flask路由本质还是add_url_rule来实现的
所以我也可以不用装饰器来实现路由映射，直接用add_url_rule来实现路由映射从而和django类似的效果