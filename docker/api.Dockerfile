FROM python:3.6.8-slim

ENV PYTHONUNBUFFERED 1
RUN apt-get update --fix-missing --no-install-recommends && \
    apt-get upgrade -y && \
    apt-get install -y build-essential \
    python-dev git \
    libffi-dev libssl-dev libpq-dev \
    wget && \
    pip install -U --no-cache-dir pip setuptools ipython && \
    wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /usr/bin/ && chmod +x /usr/bin/wait-for-it.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

COPY api/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

COPY api/ /src/api
RUN pip install -e /src/api

COPY docker/api_entrypoint.sh /entrypoint.sh
WORKDIR /src

ENTRYPOINT ["bash", "/entrypoint.sh"]