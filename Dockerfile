FROM python:3-slim
ADD /app /app
WORKDIR /app
ENV FLASK_APP hello.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
