# Use a imagem base apropriada
FROM python:3.12

# Instalar dependências do sistema para mysqlclient
RUN apt-get update && \
    apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt e instalar as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor a porta em que o servidor vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]