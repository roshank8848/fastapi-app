FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE  8000

ENV MONGO_URI="mongodb://localhost:27017/"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]