FROM python:3.6-slim

WORKDIR /usr/src/test_task_smtp

COPY requirements.txt ./
RUN pip3 install --no-cache -r requirements.txt

COPY . /usr/src/test_task_smtp
ENV PYTHONPATH "${PYTONPATH}:/usr/src/test_task_smtp"


CMD pytest -s -v
