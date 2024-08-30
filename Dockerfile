FROM apache/airflow:2.9.2

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
    && apt-get clean

COPY requirements.txt /requirements.txt
USER airflow

RUN pip install --no-cache-dir -r /requirements.txt

USER airflow

ENTRYPOINT ["/entrypoint"]
CMD ["bash"]