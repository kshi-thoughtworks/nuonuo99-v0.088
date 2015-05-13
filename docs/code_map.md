## 代码结构说明

fixtures 目录下是该 app 的 model 的初始数据

- backup.sh  数据库与 media 目录下文件备份
- install.sh  数据库初始化, 加载默认数据
- run.sh  启动 runserver, 默认监听 8000 端口, 支持所有 IP 访问
- requirements.txt  环境依赖文件
- manage.py
- README.md
- \_\_init\_\_.py
- init\_data  初始化数据. media 目录下的图片, 视频等
- media:  资源文件, 主要是图片, 图像等
- accounts:  用户管理, 帐号管理模块
    - fixtures/ 
    - models.py
    - \_\_init\_\_.py

- base:  project 基础模块. 基类, 通用方法, model, template 继承的 base, 通用 static 文件等
    - settings.py  尝试在同目录下加载 local\_settings.py. 默认使用 sqlite3
    - wsgi.py  生产环境用 wsgi 部署
    - static/  通用静态文件, 各文件具体用途参加目录下的 README.md
        - css/
        - fonts/
        - js/
        - README.md

    - templates/
        - base.html  template 继承的 base
        - brand-logo.html  此处配置网站名, navbar.html 中用到
        - home.html  首页 content
        - navbar.html  导航栏
        - nav-list.html  导航栏的超链接. navbar.html 中用到

    - \_\_init\_\_.py
    - urls.py
    - views.py
    - models.py
    - adminx.py
    - fixtures/

- docs:
    - README.md  关键进展与遗留问题
    - code\_map.md  本文, 文档地图
    - frs/  需求管理
    - dev-iter1/  迭代1 开发文档

- provider:  供应商管理
    - adminx.py
    - fixtures/
    - \_\_init\_\_.py
    - models.py

- service:  服务内容与产品管理
    - adminx.py
    - fixtures/
    - \_\_init\_\_.py
    - models.py
