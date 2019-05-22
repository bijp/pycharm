password={'admin':'123321','user':'123456'}
input_errornuam=3
userName=input('请输入用户名：').strip()
while True:
    if userName not in password:
        userName = input('请输入用户名：').strip()
        continue
    psw=input('当前用户是：{},请输入密码：'.format(userName)).strip()
    if (userName,psw) in password.item():
        print('欢迎用户：{}，登录成功！'.format(userName))
        break
    else:
        input_errornuam-=1
        if input_errornuam==0:
            print('今天3次机会结束，请明天再试！')
            break
        print('密码错误，你还有{}此机会，请再次输入！'.format(input_errornuam))