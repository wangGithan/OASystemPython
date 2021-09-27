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

git branch -a    查看本地和远程的所有分支
git branch       查看本地分支
git diff localbranch remotebranch   查看本地分支和远程分支的差异 git diff master origin/master

不提交到git上的文件写在:.gitignore上面　　　　
如果已经提交过该文件则用:git rm --cached -r 文件名 来删除本地的缓存，然后commit push     git rm --cached -r employee/__pycache__

提交修改并推送远程的步骤
第一步：查看当前的git仓库状态，可以使用git status
第二步：把更新的代码添加到暂存区 git add *
第三步：将暂存区的更新提交到本地仓库区 git commit -m "更新说明"
第四步：先git pull,拉取远程仓库所有分支更新并合并到本地。 git pull = git fetch + git merge
第五步：将本地分支的更新全部推送到远程仓库。 git push origin master
第六步．再次使用git status查看当前的git仓库状态，已经没有改动，证明更新成功

拉取
查看状态  git status
将某个远程主机的更新全部取回本地仓库 git fetch origin master
可以看到拉取过来的内容的历史记录  git log origin/master --decorate --color
拉取过来的内容从本地仓库合并到工作目录中 git merge origin/master

*wokspace->add->*index(缓存区)->commit->*Repository(本地仓库)->push->*Remote(远程仓库)
*Remote(远程仓库)->fetch/clone->*Repository(本地仓库)->merge/checkout->*workspace
*Remote->pull->*wokspace
git checkout命令用于切换分支或恢復工作树文件
// 放弃单个文件修改,注意不要忘记中间的"--",不写就成了检出分支了!
git checkout -- filepathname
// 放弃所有的文件修改
git checkout .
git参考: https://www.cnblogs.com/runnerjack/p/9342362.html


