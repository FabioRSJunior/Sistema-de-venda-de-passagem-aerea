FROM python
RUN apt-get update && apt-get install python3-pip -y && apt-get install python3-dev -y
WORKDIR /app
COPY entrypoint.sh app.py database.py models.py routes.py settings.py requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt 
CMD ["/bin/bash", "entrypoint.sh"]