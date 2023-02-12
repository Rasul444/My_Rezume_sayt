FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /Ahmedov
WORKDIR /Ahmedov

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
