FROM ruby:2.1.5

RUN apt-get update
WORKDIR /app
ADD Gemfile* /app/
RUN bundle install
