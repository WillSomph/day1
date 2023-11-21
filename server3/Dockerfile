FROM python:3.9
WORKDIR /app
COPY server3.py /app/server3.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "server3.py"]