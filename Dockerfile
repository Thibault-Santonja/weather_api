FROM python:3.10-slim-buster
ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US:en"
ENV LC_ALL "en_US.UTF-8"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY main.py .
COPY requirements.txt .
COPY src src
RUN pip install -r requirements.txt

RUN groupadd nobody
USER nobody:nobody
ARG argument
ENTRYPOINT  ["python", "main.py"]