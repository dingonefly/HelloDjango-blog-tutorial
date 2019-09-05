#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 16:45
# @Author  : dingyifei

# 远程连接服务器。
# 进入项目根目录，从远程仓库拉取最新的代码。
# 如果项目引入了新的依赖，需要执行 pip install -r requirement.txt 安装最新依赖。
# 如果修改或新增了项目静态文件，需要执行 python manage.py collectstatic 收集静态文件。
# 如果数据库发生了变化，需要执行 python manage.py migrate 迁移数据库。
# 重启 Nginx 和 Gunicorn 使改动生效。
from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/dingyifei213/07HelloDjango-blog-tutorial.git'

env.user = 'root'
env.password = 'xl1ytcY?'

# 填写你自己的主机对应的域名
env.hosts = ['www.onefly.top']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/dyf/sites/demo.onefly.top/07HelloDjango-blog-tutorial'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python manage.py collectstatic --noinput &&
        ../env/bin/python manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.onefly.top')
    sudo('service nginx reload')

if __name__ == '__main__':
    GIT_REPO = 'https://github.com/dingyifei213/07HelloDjango-blog-tutorial.git'

    env.user = 'dyf'
    env.password = 'xl1ytcY?'

    # 填写你自己的主机对应的域名
    env.hosts = ['47.98.152.71']
    # env.hosts = ['www.onefly.top']

    # 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
    env.port = '22'
    deploy()