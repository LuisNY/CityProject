FROM python:3.9.1-buster

ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306

RUN mkdir -p /home/PyCity

WORKDIR /home/PyCity

COPY . .

RUN pip3 install pymysql
RUN pip3 install cryptography

RUN chmod +x ./wait-for-it.sh ./docker-entrypoint.sh

RUN useradd -ms /bin/bash luigi
USER luigi

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python3", "main.py"]
