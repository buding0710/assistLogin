# Generated by Django 3.1 on 2022-12-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assist_login', '0002_auto_20201229_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_data',
            name='browser_type',
            field=models.CharField(choices=[('chrome', '谷歌浏览器'), ('firefox', '火狐浏览器'), ('internet explorer', 'IE浏览器'), ('MicrosoftEdge', 'Microsoft Edge'), ('Chrome_incognito_window', '谷歌浏览器隐身窗口'), ('Firefox_incognito_window', '火狐浏览器隐身窗口'), ('IE_incognito_window', 'IE浏览器隐身窗口')], default='Chrome', max_length=64, verbose_name='浏览器类型'),
        ),
    ]
