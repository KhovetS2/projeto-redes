FROM --platform=$BUILDPLATFORM python AS builder

WORKDIR /code
COPY ./ /code
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP run.py
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8000



