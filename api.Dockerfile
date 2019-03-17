FROM python:3.6.8-slim

COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

COPY api /src/api
RUN pip install -e /src/api

COPY docker/api_entrypoint.sh /entrypoint.sh
WORKDIR /src

ENTRYPOINT ["bash", "/entrypoint.sh"]