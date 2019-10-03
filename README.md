# flask
flask

# Docs
    https://dormousehole.readthedocs.io/en/latest/installation.html#install-create-env
# 开发环境
    创建虚拟环境
    python3 -m venv venv
    激活虚拟环境
    . venv/bin/activate
    安装Flask
    pip install Flask --default-timeout=1000

# 开发服务器
    https://dormousehole.readthedocs.io/en/latest/server.html#server
    export FLASK_APP=my_application
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