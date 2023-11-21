FROM python:3.9
WORKDIR /app
COPY server2.py /app/server2.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5372
CMD ["python", "server2.py"]
