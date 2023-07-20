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

CMD ["python", "src/main.py"]