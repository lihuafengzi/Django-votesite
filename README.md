# 投票应用程序
[TOC]

## 项目描述
这是一个投票应用程序

它将由两部分组成：
- 一个让人们查看和投票的公共站点
- 一个让你能添加、修改和删除投票的管理站点

## 技术说明

前后端采用一体化的Python 3.7.9 + Django 3.1.2

### 环境安装
安装虚拟环境，指定Python版本和Django版本。
```bash
conda create -n datavisual37 python=3.7.9 Django=3.1.2
conda activate datavisual37
```
如果是想安装Django的开发版本
```bash
git clone https://github.com/django/django.git
pip install -e django/  
```
 -e 是指的本地项目路径. 

查看Django版本
```bash
python -m django --version
```
初始化项目
```bash
django-admin startproject mysite
```
这时候可以进入mysite项目，然后启动项目
```bash
cd mysite
python manage.py runserver
```
如果出现以下的提示信息，则证明环境和项目初始化成功了
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 30, 2020 - 09:57:39
Django version 3.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
现在，服务器正在运行，浏览器访问 https://127.0.0.1:8000/。你将会看到一个“祝贺”页面，随着一只火箭发射，服务器已经运行了。

![image-20201030100514022](assets/pic/image-20201030100514022.png)

如果需要更换端口，则在后面加上端口
```bash
python manage.py runserver 8080
```
如果要更换ip，则在端口前加上
```bash
python manage.py runserver 0:8000
```
其中，0 是 0.0.0.0 的简写。

在修改项目的文件内容后，runserver会自动重新加载Python代码。只有在新加的文件的时候，才需要重启服务器。

### 项目开发

在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。

- 应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。
- 项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就能专心写代码，而不是创建目录了。

我们将在你的 manage.py 同级目录下创建投票应用。这样它就可以作为顶级模块导入，而不是 mysite 的子模块。

现在在manage.py的同级目录下，执行如下命令，创建应用。




---

最后更新时间：2020-10-30
