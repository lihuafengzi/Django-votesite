# 投票应用程序
[TOC]

## 项目描述
这是一个投票应用程序

它将由两部分组成：
- 一个让人们查看和投票的公共站点
- 一个让你能添加、修改和删除投票的管理站点

完成本项目的目的，是为了学习Django。

## 技术说明

前后端采用一体化的Python 3.7.9 + Django 3.1.2


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
现在，服务器正在运行，浏览器访问 https://127.0.0.1:8000/。你将会看到一个"祝贺"页面，随着一只火箭发射，服务器已经运行了。

![image-20201030100514022](assets/pic/image-20201030100514022.png)

> 图片在GitHub上无法显示

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

后续的项目细节，请移步：https://docs.djangoproject.com/zh-hans/3.1/contents/

同时，我也在文档`doc/lesson-**.md`中记录了学习的过程。

---

最后更新时间：2020-10-30
