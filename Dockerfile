FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install requests names pytest
ENTRYPOINT pytest -s -v test.py --disable-warnings