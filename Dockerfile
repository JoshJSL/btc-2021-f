FROM python:3.9

RUN pip install request

copy app.py .

cmd ["py", "app.py"]
