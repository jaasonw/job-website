FROM python:3.11-slim
WORKDIR /app
COPY . /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install .
CMD ["python", "-m", "sweify"]