FROM python:3.8.5

RUN mkdir -p /usr/src/web_calc/
WORKDIR /usr/src/web_calc/

COPY . /usr/src/web_calc/
RUN pip install flask

EXPOSE 2000

CMD ["python", "calc.py"]
