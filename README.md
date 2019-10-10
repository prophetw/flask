# flask
flask

# Docs

# 开发环境
    ### python3 版本的
    创建虚拟环境
    python3 -m venv venv
    激活虚拟环境
    . venv/bin/activate
    在虚拟环境进行开发 比如安装依赖
    ### python2 版本可以看
    https://dormousehole.readthedocs.io/en/latest/installation.html#install-create-env
# 开发服务器
    https://dormousehole.readthedocs.io/en/latest/server.html#server
    export FLASK_APP=run.py
    export FLASK_ENV=development 开发环境
    flask run
# 部署服务器
    https://dormousehole.readthedocs.io/en/latest/deploying/uwsgi.html#id1
    uwsgi uwsgi.ini
    supervisor 作为自启动
    flask-uwsgi-nginx.conf nginx 配置
    uwsgi.ini uwsgi配置
    mysite.sock sock配置
# CORS
    https://flask-cors.readthedocs.io/en/latest/

# 生成依赖以及安装依赖
    https://pip.pypa.io/en/stable/reference/pip_freeze/
    pip freeze > requirements.txt
    pip install -r requirements.txt