FROM python:3.9
WORKDIR /app 
COPY server1.py /app/server1.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4567
CMD ["python", "server1.py"]
