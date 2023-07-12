#!/bin/bash

source bin/util.sh

port=$1

echo "获取到的port: $port"

echo "sysctl -w net.core.somaxconn=32768 # 执行此命令需要sudo权限"

generate_ini () {
    cat > bin/server.ini <<-EOF
    [uwsgi]
    http = 0.0.0.0:${port}

    strict = true
    module = app
    callable = app
    processes = 4
    master = true
    threads = 1
    pidfile = uwsgi.pid
    vacuum = true
    reload-mercy = 1
    worker-reload-mercy = 1
    listen = 1024
    chdir = src
    virtualenv = $HOME/miniconda3/envs/ConfigCenter
EOF
}

generate_ini

`uwsgi --gevent 4096 --gevent-early-monkey-patch bin/server.ini`
