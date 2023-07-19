FROM python:3.11-slim
RUN mkdir /app
COPY ./src /app/src
COPY ./cron /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN pip install .

RUN apt update
RUN apt install cron -y

RUN \
  chmod 0644 /app/cron && \
  crontab /app/cron

RUN \
  touch /var/log/cron.log

CMD (cron -f &) && tail -f /var/log/cron.log