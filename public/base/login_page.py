from public.common.base_obj import base_frame


# 页面对象（PO) 登录页面
class LoginPage(base_frame):

    
    username_loc = ('id=userName')
    passwd_loc = ('id=password')
    btn_loc = ('id=login-btn')
    error_text_loc = ('class=font-16')


    def username(self, text):
        self.send_keys(self.username_loc, text)

    def password(self, text):
        self.send_keys(self.passwd_loc, text)

    def click_login_btn(self):
        self.click(self.btn_loc)

    def error_text(self):
        self.get_text(self.error_text_loc)

    def pro(self, username, passwd):
        self.username(username)
        self.password(passwd)
        self.click_login_btn()


