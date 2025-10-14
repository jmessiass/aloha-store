# Use uma imagem base do Python
FROM python:3.14

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos requirements.txt e o resto do código para o diretório de trabalho
COPY requirements.txt requirements.txt
COPY . .

# Instale as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que o Flask está rodando
EXPOSE 8080

# Comando para iniciar a aplicação Flask
CMD ["python", "alohastore.py"]