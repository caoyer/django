实现功能：
	1. 前端页面对后端数据库实现增删改查
        2. 通过主机、主机、使用部门、机器用途、运维人员等相关数据进行查找
	3. 不同用户可分配不同权限管理相应的主机
	
目录结构：
	cmdb/
	├── cmdb
	│   ├── __init__.py
	│   ├── settings.py    配置文件
	│   ├── urls.py		   路径转发
	│   └── wsgi.py
	├── info.sql           数据库默认的数据文件
	├── manage.py		   执行文件
	└── mysite             
		├── admin.py       django后台admin模块
		├── apps.py
		├── __init__.py
		├── migrations     数据临时文件夹
		│   ├── 0001_initial.py
		│   ├── __init__.py
		├── models.py       数据库建表操作模块
		├── tests.py
		└── views.py        

应用数据库: sqlite3

创建sqlite中的库: sqlite3 mysite.db

启动命令：
	python cmdb/manage.py runserver 0.0.0.0:8000
	
网页访问地址： 
	http://127.0.0.1:8000/admin
