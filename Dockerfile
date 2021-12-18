FROM python:3.8

COPY app.py ./

RUN python3 -m pip install requests

CMD ["python", "app.py"]
