ARG DCS_FLUENTD_IMAGE
FROM fluent/$DCS_FLUENTD_IMAGE

USER root

# Packages required to build & install Ruby Gems
RUN apk add     \
    build-base  \
    ruby-dev && \
    fluent-gem install fluent-plugin-mongo
