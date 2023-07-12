#!/bin/bash

source bin/util.sh

port=$(get_available_port)

echo "获取到的port: $port"

cd src && python app.py --port $port --debug
