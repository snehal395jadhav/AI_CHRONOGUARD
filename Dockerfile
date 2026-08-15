FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8501
EXPOSE 5002
CMD ["streamlit", "run", "index1.py", "--server.address=0.0.0.0", "--server.port=8501"]