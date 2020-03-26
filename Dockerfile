FROM alpine as webpack-base
WORKDIR /js
RUN apk update && apk add --no-cache npm
ADD package.json /js/
RUN npm install .
ADD webpack.config.js /js/
ADD js /js/src/

FROM webpack-base AS webpack
RUN npm run build

FROM python:3-alpine as web-base
WORKDIR /main
RUN apk update && apk add --no-cache \
  postgresql-client \
  postgresql-dev

COPY requirements.txt /main/
RUN apk add --virtual build-deps build-base \
    && apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev\
    && pip install -r requirements.txt \
    && apk del build-deps \
    && rm -f requirements.txt

RUN addgroup -S django && adduser -S -G django django

FROM web-base AS local-web
RUN apk update && apk add --no-cache git
USER django

FROM web-base AS web

RUN pip install gunicorn
CMD ["sh", "-c", "gunicorn --bind=0.0.0.0:8000 --workers=$(nproc) --forwarded-allow-ips='*' snapburg.wsgi"]
EXPOSE 8000
ADD manage.py /main
ADD snapburg /main/snapburg
ADD apps /main/apps
ADD static /main/static
VOLUME /main/media
COPY --from=webpack-dist /js/dist /main/dist
USER django
