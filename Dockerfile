FROM python:3.7.4-slim-buster

COPY sources.list /etc/apt/sources.list

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONIOENCODING=UTF-8
ENV TZ=Asia/Shanghai
ENV PROJECT_DIR=/opt/vue_music/

COPY ./ $PROJECT_DIR

#COPY ./.env_sample $PROJECT_DIR/.env

WORKDIR $PROJECT_DIR

RUN apt update && apt install -y tzdata locales gcc apt-transport-https ca-certificates libmariadb-dev-compat libmariadb-dev libmysqlclient-dev python3-dev

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

RUN echo "Asia/Shanghai" > /etc/timezone && rm -f /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONPATH=$PYTHONPATH:$PROJECT_DIR

#VOLUME ["$PROJECT_DIR/log/"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
