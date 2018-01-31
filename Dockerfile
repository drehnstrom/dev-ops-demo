FROM python:2
WORKDIR /usr/src/app
RUN pip install flask
COPY . .
CMD [ "python", "./main.py" ]

