FROM alpine:3.13

RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache python3-dev py3-pip
RUN pip3 install --upgrade pip
COPY app/requirements.txt requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

#COPY ./app .
#CMD ["python3", "app.py"]
#docker build -t flask-app .
#docker run -it -p 7000:7000 -d flask-app