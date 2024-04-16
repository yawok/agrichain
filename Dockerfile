FROM python:3.10

WORKDIR /agrichain

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -x start_docker_app.sh

EXPOSE 8000

CMD ["/bin/bash", "start_docker_app.sh"]