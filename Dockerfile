FROM quay.io/basisai/python-alpine-grpcio
# set work directory
RUN apk add gcc g++ linux-headers
RUN apk add --update alpine-sdk
RUN apk add postgresql-dev
WORKDIR /usr/src/app

RUN apk add --update py3-pip tk
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity

# set environment variables
ENV PYTHON_PIP_VERSION=20.1
ENV URL=http://api.weatherbit.io/v2.0/current
ENV KEY=ff8e83a0d6a844a2b209cae6f8a5ce0b
ENV URL_REDIS=https://cr-redis-ifelqlekta-uc.a.run.app
ENV SECRET_KEY='django-insecure-pz^e*u(1$e$vg$1^qouarv*fa=yc(+p13@^r^)6&gja*vqh$v'

# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]