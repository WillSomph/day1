FROM python:3.9
WORKDIR /app 
COPY server4.py /app/server4.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 1111
CMD ["python", "server4.py"]
