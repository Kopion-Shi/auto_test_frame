FROM ubuntu:18.04

MAINTAINER carlshixinlei "carl3633524461@outlook.com"

RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean
RUN  apt-get update -y && \
     apt-get install -y apt-utils \
                    build-essential \
                    curl \
                    git \
                    cmake \
                    unzip \
                    autoconf \
                    autogen \
                    libtool \
                    mlocate \
                    zlib1g-dev \
                    python \
                    python3-dev \
                    python3-pip


RUN set -ex \
    && mkdir /usr/local/python3 \
    && mkdir /usr/local/openssl \
    && mkdir /home/code


COPY Python-3.8.16.tar.xz  /usr/local/python3/
COPY openssl-3.0.1.tar.gz  /usr/local/openssl/


RUN set -ex \
    && cd /usr/local/openssl \
    && tar -zxvf openssl-3.0.1.tar.gz \
    && cd openssl-3.0.1 \
    && ./config --prefix=/usr/local/openssl \
    && make && make install


RUN set -ex \
    && cd /usr/local/python3 \
    && tar -xvJf  Python-3.8.16.tar.xz \
    && cd Python-3.8.16 \
    && ./configure prefix=/usr/local/python3 \
    && make && make install \
    && ln -s /usr/local/python3/bin/python3.8 /usr/local/bin/python \
    && ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip


COPY . /home/code
WORKDIR /home/code
RUN pip install -U pip --index-url http://pypi.douban.com/simple/  --trusted-host pypi.douban.com
RUN pip install -r requirements.txt --index-url http://pypi.douban.com/simple/  --trusted-host pypi.douban.com
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

EXPOSE 82

