web.py 的介绍
    简介：
        一个非常轻量级的python web框架，简单且强大

    环境搭建：
        install 一个包就行

    官网：webpy.org

web开发基础知识
    URL映射：
        URL完全匹配:
            /index
        URL模糊匹配:(正则表达式)
            /post/\d+
        URL带组匹配:(正则表达式带组)
            这种处理方式会将组中的的内容传递给处理函数
            /post/(\d+)

web.py 开发

    请求处理：
        web.input()
    请求头获取：
        web.ctx.env

响应处理： webpy_template.py
    模板文件读取：
        render.index("参数")
    结果数据获取：
        model.select("sql")
    URL跳转：
        web.seeother("/")

 安装web.py的时候遇到了一点小问题，
    pip install web.py的时候，提示utils model not fount
    网上找了资料大致意思是：web.py只有py2有，到了py3这个被bottle.py替代了。
    如果系统是多个py环境主要使用pip2 install web.py 命令。





