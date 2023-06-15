FROM mysql:latest

# Define as variáveis de ambiente para configuração do MySQL
ENV MYSQL_DATABASE=langapp
ENV MYSQL_USER=dbuser
ENV MYSQL_PASSWORD=paok
ENV MYSQL_ROOT_PASSWORD=palegal

# Copia o arquivo SQL para o diretório de inicialização do MySQL
COPY init.sql /docker-entrypoint-initdb.d/

# Expor a porta padrão do MySQL (opcional)
EXPOSE 3306

# Comando padrão executado ao iniciar o contêiner
CMD ["mysqld"]
