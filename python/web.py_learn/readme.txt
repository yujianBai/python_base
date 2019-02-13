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