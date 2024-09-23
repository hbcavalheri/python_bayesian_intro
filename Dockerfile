# Use uma imagem base do Python 3.10
FROM python:3.10-slim

# Instale ferramentas e bibliotecas de desenvolvimento necessárias
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código fonte para o contêiner
COPY . .

# Defina o comando padrão para executar o script Python
CMD ["python", "bayesian.py"]
