

#正常场景——登录成功
scuess_data = {"user":"18610430456","pwd":"liqi_0827"}
#异常场景——用户名为空，用户名和密码都为空
#同类型报错，即定位一样 可以放在一起
wrong_data = [
    {"user":"","pwd":"","check":"账号不能为空"},
    {"user":"","pwd":"liqi_0827","check":"账号不能为空"},

]
#异常场景——用户不存在
wrong_user_format = {"user":"1123123","pwd":"qwefssgsfdh2343","check":"用户不存在"}


# {"user": "18610430456", "pwd": "", "check": "密码不能为空"}
