FROM python:3.9

# Defina o diretório de trabalho como /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Instale as dependências do seu código Python (se houver)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copie o script de inicialização para o container
COPY ./ /app/

# Dar permissão de execução ao script de inicialização
RUN chmod +x /app/entrypoint.sh

# Comando para executar o script de inicialização quando o container for iniciado
ENTRYPOINT ["/app/entrypoint.sh"]
