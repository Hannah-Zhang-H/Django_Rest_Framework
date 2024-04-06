1. 创建主程序和app：
这次用的是terminal，不是鼠标点击的
(base) hanhan@MacBook-Pro-73 Django_Rest_Framework % django-admin startproject mysite
(base) hanhan@MacBook-Pro-73 Django_Rest_Framework % cd mysite
(base) hanhan@MacBook-Pro-73 mysite % django-admin startapp movies


2. 在mysite/settings.py 中设置rest framework并注册app
 'rest_framework',
  'movies.apps.MoviesConfig',

3. 在movies/models.py创建model，hold住movie的所有data

4. 做migrations创建 class Moviedata model的数据库表
python manage.py makemigrations
python manage.py sqlmigrate movies 0001
python manage.py migrate

5. 这里不创建form，而是创建一个super user
(.venv) (base) hanhan@MacBook-Pro-73 DjangoRestFramework % python manage.py createsuperuser
22015651    22015651


6. 如果在terminal 输入 python manage.py runserver时出错，则采取一下措施：
这样做是因为在conda环境下可能会出现一些检测不到已安装的rest framework的问题。
-----------------------------------------------------------------------------------------------------------------
python -m venv myenv 是一个命令，用于使用 Python 自带的 venv 模块创建一个名为 myenv 的虚拟环境。让我解释一下每个部分的含义：

python: 这是用于执行 Python 解释器的命令。在这里，它告诉操作系统使用 Python 解释器来执行后续的命令。
-m venv: 这是一个参数，告诉 Python 解释器要运行的模块是 venv，它是 Python 自带的用于创建虚拟环境的模块。
myenv: 这是你为虚拟环境选择的名称。在这个命令中，你创建了一个名为 myenv 的虚拟环境。
为什么要创建虚拟环境呢？虚拟环境是一个独立的 Python 环境，其中包含了一个特定项目所需的所有库和依赖项。这样做的好处是可以在不影响全局 Python 环境的情况下，在同一台计算机上管理多个项目，并确保它们使用的库版本不会互相冲突。

因此，通过运行 python -m venv myenv，你在当前目录下创建了一个名为 myenv 的虚拟环境，你可以在其中安装和管理项目所需的所有库和依赖项。
-----------------------------------------------------------------------------------------------------------------
python -m venv myenv
-------------------------------------------
Win：myenv\Scripts\activate
Mac/Linux: source myenv/bin/activate
-------------------------------------------
pip install django
pip install djangorestframework
-------------------------------------------
然后再次运行python manage.py runserve 来启动server

6 ---- 补充：
下次要用的话：
cd 到根目录: cd /Users/hanhan/PycharmProjects/Django_Rest_Framework/mysite
然后在terminal中输入：source myenv/bin/activate


7. 登录admin，依旧没有movedata模块:
去movies/admin.py 中导入models.py中的Moviedata模块，然后注册model： admin.site.register(Moviedata)


8. 在admin panel创建movie后，显示的是Moviedata object(1)，不美观。
去movies/models.py中新增
def __str__(self):
    return self.name
问题解决啦！

9. 可以添加一个API来share这些添加的movie信息来挣钱----序列化Serializer
