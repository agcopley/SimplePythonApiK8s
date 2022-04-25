# syntax=docker/dockerfile:1
FROM python:3.8-alpine
WORKDIR /code

RUN apk add build-base && apk add libpq && apk add libffi-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir && \
apk --purge del .build-deps
EXPOSE 5000
COPY . .
ENTRYPOINT [ "python" ]
CMD ["app.py"]