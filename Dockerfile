FROM python:3.11-slim
WORKDIR /app
COPY . /app
# COPY pyproject.toml /app
# WORKDIR /
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN pip install .


CMD ["python", "-m", "sweify"]