# Usa uma imagem Python leve
FROM python:3.9.13-slim

# Evita que o Python gere arquivos .pyc e buffer de log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define onde o app vai ficar dentro do container
WORKDIR /space

# Instala dependências do sistema (necessário para Postgres)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Instala as dependências do Python
COPY requirements.txt /space/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copia o resto do projeto
COPY . /space/

# Comando padrão ao iniciar (Gunicorn)
CMD ["gunicorn", "space2.wsgi:application", "--bind", "0.0.0.0:8000"]