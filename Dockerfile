FROM python:3.7-buster as builder
WORKDIR /opt/app
RUN pip3 install poetry google-python-cloud-debugger google-cloud-profiler
COPY pyproject.toml poetry.lock /opt/app/
RUN poetry export -f requirements.txt > requirements.txt
RUN pip3 install -r requirements.txt


FROM python:3.7-slim-buster as runner
ENV PORT=8000
WORKDIR /opt/app/
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY python_cloud_debug /opt/app/
WORKDIR /opt/app/

ENV PYTHONUNBUFFERED=TRUE
CMD [ "/bin/sh", "-c", "exec /usr/local/bin/uvicorn --host 0.0.0.0 --port $PORT main:app" ]
