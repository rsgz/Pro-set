@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
F: && cd F:\0-git-pro\Pro-set
echo ==========注意============
echo ****** 你需要 clash global模式+系统代理 ******
echo ****** 执行了下面命令：******
echo git add .
echo git commit -m "xxx"
echo git push origin main
echo ==========命令参考============
echo *** 下载项目 ***
echo 本地没有项目就克隆项目 git clone https://github.com/rsgz/Pro-set.git
echo 本地已经有了项目就 拉取最新的 git pull origin main
echo *** 代理设置 ***
echo 查看代理 git config --global --get https.proxy
echo 设置代理 git config --global https.proxy http://proxyuser:proxypassword@proxy.server.com:port
echo 取消代理 git config --global --unset https.proxy
echo *** 仓库地址设置 ***
echo 查看当前远程仓库 git remote -v
echo 设置远程仓库地址 git remote set-url origin https://github.com/rsgz/Pro-set.git
echo *** 邮箱用户名设置 ***
echo 设置用户名 git config --global user.name "rsgz"
echo 设置邮箱 git config --global user.email "2966261184@qq.com"
echo 查看当前仓库
echo git config user.name
echo git config user.email
echo 查看全局用户名和邮箱
echo git config --global user.name
echo git config --global user.email
echo 查看所有配置
echo git config --list
echo ======================
set /p info=请输入main分支改动信息:
git add .
git commit -m %info%
git push origin main
pause