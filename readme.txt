python manage.py runserver
frontend:
npm run dev    启动vue服务器
npm run build  编译vue文件


http://127.0.0.1:8000/admin/login/?next=/admin/
http://127.0.0.1:8000/login/login_form/
http://127.0.0.1:8000/users/

框架搭建过程参考:https://cloud.tencent.com/developer/article/1576599

1.查看所有分支
git branch -a （看看是否连接上远程的git）
2.创建分支
git branch xxx（为你的分支起名字）
3.切换分支
git checkout xxx（切换到你创建的分支，xxx为你要切换分支的名字）
4.添加修改代码到缓存（注意最后的"."前面有个空格）
git add .
5.添加提交代码的备注
git commit -m "xxx"（xxx为本次提交代码的备注）
6.提交代码到指定的分支
git push origin xxx （xxx为要提交代码的分支名称）
7.如果git push这个步骤出现了错误，是因为是git服务器中的你提交的文件不在本地代码目录中，可以通过如下命令进行代码合并，然后在使用第6步
git pull --rebase origin xxx（xxx为要提交代码的分支名称）






