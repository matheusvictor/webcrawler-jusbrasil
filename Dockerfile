FROM joyzoursky/python-chromedriver:3.9-selenium

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
