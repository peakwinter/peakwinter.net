FROM node:14-alpine AS builder

ARG NODE_ENV
WORKDIR /code
RUN apk add --no-cache build-base python3
ADD package.json yarn.lock /code/
RUN yarn --pure-lockfile
ENV NODE_ENV=${NODE_ENV:-production}
ADD . /code/
RUN yarn build


FROM nginx:alpine AS web

EXPOSE 80

COPY --from=builder /code/dist/ /usr/share/nginx/html
