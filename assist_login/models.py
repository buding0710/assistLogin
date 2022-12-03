from django.db import models

# Create your models here.


class Login_data(models.Model):
    browser_type_choice = (
        ('chrome', '谷歌浏览器'),
        ('firefox', '火狐浏览器'),
        ('internet explorer', 'IE浏览器'),
        ('MicrosoftEdge', 'Microsoft Edge'),
        ('Chrome_incognito_window', '谷歌浏览器隐身窗口'),
        ('Firefox_incognito_window', '火狐浏览器隐身窗口'),
        ('IE_incognito_window', 'IE浏览器隐身窗口'),
    )

    close_window_method_choice = (
        (0, '新增页签窗口打开'),
        (1, '关闭浏览器重新打开'),
    )

    login_name = models.CharField(max_length=255, unique=True,verbose_name='登录名')
    login_url = models.CharField(max_length=512, verbose_name='登录url')
    redirect = models.CharField(max_length=512, blank=True, null=True, default='', verbose_name='重定向url')
    username = models.CharField(max_length=128, verbose_name='登录用户名')
    password = models.CharField(max_length=128, verbose_name='登录密码')
    browser_type = models.CharField(choices=browser_type_choice, max_length=64, default='Chrome', verbose_name='浏览器类型')
    close_window_method = models.SmallIntegerField(choices=close_window_method_choice, default=0, verbose_name='打开窗口方式')
    user_role = models.CharField(max_length=256,  blank=True, null=True, default='', verbose_name='用户角色')
    quarter = models.CharField(max_length=256,  blank=True, null=True, default='', verbose_name='用户岗位')
    data_range = models.CharField(max_length=256,  blank=True, null=True, default='', verbose_name='数据范围')
    remark = models.CharField(max_length=1024,  blank=True, null=True, default='', verbose_name='备注')

    def __str__(self):
        return 'Login(login_name=%s,login_url=%s,redirect=%s,username=%s,password=%s,browser_type=%s,close_window_method=%s,user_role=%s,quarter=%s,data_range=%s,remark=%s' \
               %(self.login_name, self.login_url, self.redirect, self.username, self.password,self.get_browser_type_display(), self.get_close_window_method_display(), self.user_role, self.quarter, self.data_range, self.remark)

    class Meta:
        verbose_name = '登录数据'
        verbose_name_plural = '登录数据'