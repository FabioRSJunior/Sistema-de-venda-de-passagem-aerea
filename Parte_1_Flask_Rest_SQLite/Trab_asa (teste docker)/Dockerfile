FROM ubuntu
RUN apt-get update && apt-get install python3-pip -y && apt-get install python-dev -y
WORKDIR /Trab_asa
COPY app.py models.py utils.py requirements.txt atividades.db /Trab_asa/
WORKDIR /Trab_asa
RUN pip install -r requirements.txt 
RUN pip install flask
CMD ["python3" ,"app.py"]
