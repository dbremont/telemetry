# Telemetry

> Python Telemetry

## Install (Linux/Ubuntu)

- python3 -m venv venv
- source venv/bin/activate
- pip install flask opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-flask

## Graphana

- run:    docker run -d -v <HOST FILE PATH>:/home/grafana/datasources --name=grafana -p 3000:3000 grafana/grafana
- stop:   docker container stop graphana
- enter:  docker exec -it grafana /bin/bash
- ...

## Graphana Guide

0. Enter: admin, admin by default
1. Install the sqllite driver
2. Create a dashboard
    3. Make some transformation to the data
    4. ...
