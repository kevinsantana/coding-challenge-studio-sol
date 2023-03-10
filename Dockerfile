FROM ubuntu:22.04

# DEPENDENCIES
RUN apt-get update

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get install python3.10 -y && apt-get install python3-pip -y && apt-get install libpq-dev -y
RUN pip install --upgrade pip
RUN apt-get clean

# INSTALL APPLICATION
COPY ./valid_password /deploy/valid_password
COPY setup.py /deploy
COPY /tests /deploy/tests
COPY README.md /deploy

WORKDIR /deploy

RUN pip install -e . 

RUN cd /deploy/valid_password
EXPOSE 7000
CMD ["gunicorn", "--bind=0.0.0.0:7000", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--timeout=174000", "valid_password.app:start_application()"]