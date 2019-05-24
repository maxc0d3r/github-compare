FROM python:3.7-alpine

COPY . /github-compare

WORKDIR /github-compare

RUN pip install -r requirements.txt

ENTRYPOINT [ "python","app.py" ]
