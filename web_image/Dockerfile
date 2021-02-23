FROM python:3.8

WORKDIR /code

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

VOLUME [ "./media", "media_folder"]

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0", "-p", "5000" ]

# docker build -t web_image:v2.0 .
# docker run -d --name web_project  -p "5050:5000" web_image:v2.0