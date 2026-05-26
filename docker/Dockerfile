FROM python:3.11-slim

# Criar usuário seguro
RUN useradd --create-home --shell /bin/bash appuser

# Pasta de trabalho
WORKDIR /app

# Copiar dependências
COPY app/requirements.txt .

# Instalar libs
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY app/ .

# Segurança
USER appuser

# Porta da aplicação
EXPOSE 5000

# Inicialização
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]