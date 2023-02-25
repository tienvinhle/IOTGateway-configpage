# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /etc/configPage/  && \
  mkdir /etc/modbus/
WORKDIR /etc/configPage/
COPY . .
RUN pip install 'flask' && \
  rm -rf /var/cache/apk/*
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]