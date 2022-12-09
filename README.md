# assistLogin辅助登录
## 系统说明
本程序适用于局域网内远程辅助登录，主要使用django和selenium搭建
本程序使用到selenium远程控制，需先建立主机与子机的注册连接
## 操作步骤
1/selenium-server-standalone-X.XX.jar和浏览器driver需要放在同一目录下
2/主机运用管理员权限，打开命令行，进入到selenium server所在的路径，运行：java -jar selenium-server-standalone-3.141.59.jar -role hub -port 5566，
http://localhost:5566/grid/console网页可查看是否成功
3/子机运用管理员权限，打开命令行，到selenium server所在的路径，运行：java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://主机IP:5566/grid/register/ -port 5577
4/子机访问http://主机IP:8080/assist_login/
![image](https://user-images.githubusercontent.com/83357789/205450345-4f7f00aa-f479-490e-a029-b4a515880aba.png)
