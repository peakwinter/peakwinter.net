FROM node:alpine-14 AS builder

ARG NODE_ENV
WORKDIR /code
ADD package.json yarn.lock /code/
RUN yarn --pure-lockfile
ENV NODE_ENV=${NODE_ENV:-production}
ADD . /code/
RUN yarn build


FROM nginx:alpine AS web

EXPOSE 80

COPY --from=builder /code/dist/ /usr/share/nginx/html
