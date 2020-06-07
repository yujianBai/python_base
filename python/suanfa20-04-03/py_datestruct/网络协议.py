# auth Bernard
# date 2020-04-20

"""
浏览器输入一个url 中间经历的过程
    回答问题的角度， 中间涉及了那些过程？
    包含了那些网络协议
    每个协议都干了什么？

          tcp三次              Nginx 转发到多态服务器          django/Falsk
dns查询-> tcp握手-> http请求-> 方向代理nginx-> uwsgi/gunicom-> web app响应 -> tcp挥手
(先查dns缓存, 获取ip)  应用                    WSGI(兼容web框架)              tcp四次挥手

dns查询步骤?


TCP三次握手：
    三次握手、 状态转换， 用wireshark 抓包更直观
    抓包之前先通过浏览器F12，找到网站的IP地址

TCP/ UPD区别：
    面向链接、 可靠地， 基于字节流
    无连接、 不可靠， 面向报文


网络分层：
    物理层
    链路层
    网络层
    传输层
    应用层

HTTP协议常考题：

    HTTP请求的组成
        状态行
        请求头
        消息主体

    HTTP响应：
        状态行
        响应头
        相应正文

        命令行 curl 工具
        pip install httpie
    HTTP协议有哪些部分组成？ 使用抓包工具查看
"""

""" httpie 使用

(venv) baiyj@baiyj-Lenovo-G470:~$ http -f POST baidu.com hello=world -v

请求头： POST / HTTP/1.1

             Accept: */*
             Accept-Encoding: gzip, deflate
             Connection: keep-alive
请求头：      Content-Length: 11
             Content-Type: application/x-www-form-urlencoded; charset=utf-8
             Host: baidu.com
             User-Agent: HTTPie/2.1.0

消息主体： hello=world



响应行： HTTP/1.1 200 OK   (http版本 和 状态码)
            Accept-Ranges: bytes
            Cache-Control: max-age=86400
            Connection: Keep-Alive
            Content-Length: 81
响应头：      Content-Type: text/html
            Date: Mon, 20 Apr 2020 10:18:05 GMT
            ETag: "51-47cf7e6ee8400"
            Expires: Tue, 21 Apr 2020 10:18:05 GMT
            Last-Modified: Tue, 12 Jan 2010 13:48:00 GMT
            Server: Apache

            <html>
响应正文：    <meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
            </html>
"""

"""
状态码：
    1××， 服务器收到请求， 需要请求者继续执行操作
    2××， 成功， 操作被成功接收处理
    3××， 重定向， 需要进一步操作完成请求, 301永久重定向， 302临时重定向
    4××， 客户端错误, 400请求错误， 403 forbiden
    5××， 服务器内部错误, 500
"""

"""
HTTP GET/ POST区别：
    常见的HTTP方法： 
      restful风格的前后端分离：
        get 获取
        post 创建
        put 更新
        delete 删除
    
    GET vs POST
        restful 语义上一个是获取， 一个是创建
        get是幂等的， post是非幂等的
        get请求参数是放在url（明文）， 长度限制； post放在请求体， 更安全。
    幂等性：
        幂等方法是无论调用多少次都得到同样的结果
        非幂等的方法， 需要在服务端实现
        
    什么是http长连接：
        Http persistent connection, Http 1.1
        短连接： 建立链接... 传输数据... 关闭链接（链接的建立和关闭开销大）
        长连接： Connection: keep-alive 保持TCP 连接不断开
        
        如何区分不同的HTTP请求呢？
            Conntent-Length | TranserEncoding:chunked
            
    cookie 和session区别：
        Http是无状态的， 如何识别用户？
            Session一般是 服务器生成后给客户端（通过url参数或者 cookie）
            Cookie 是实现session的一种机制， 通过http cookie字段实现
            Session通过在服务器保存sessionid识别用户， cookie存储在客户端
"""

"""
回顾：
    请求和响应的组成
    常用HTTP方法和幂等性
    长连接： session; cookie
"""
