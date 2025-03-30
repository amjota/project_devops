# Baixando a imagem oficial do SQL Server

#### A imagem oficial do SQL Server 2019 para Linux está disponível no Docker Hub. Para baixá-la, execute o seguinte comando:

```bash
docker pull mcr.microsoft.com/mssql/server:2022-latest
```

#### Depois de baixar a imagem, você pode rodar um contêiner com o SQL Server usando o seguinte comando:

```bash
docker run -e 'ACCEPT_EULA=Y' \
  -e 'SA_PASSWORD=(Suasenhaforte)' \
  -p 1433:1433 \
  --name sql-amjota \
  -v /mnt/data/sql-amjota:/var/opt/mssql/data \
  --restart unless-stopped \
  -d mcr.microsoft.com/mssql/server:2022-latest
```

## Aqui está o que cada parte do comando faz:

- **-e 'ACCEPT_EULA=Y'**: Aceita automaticamente os termos de licenciamento da Microsoft.
- **-e 'SA_PASSWORD= SuaSenhaForte123! '**: Define a senha para o usuário administrador (sa). Importante: a senha precisa ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos.
- **-p 1433:1433**: Mapeia a porta do contêiner (1433) para a porta 1433 do host. Isso permite que você acesse o SQL Server através da porta padrão.
- **--name sql1**: Define o nome do contêiner como sql1.
- **-d**: Executa o contêiner em segundo plano (modo "detached").
- **mcr.microsoft.com/mssql/server:2019-latest**: A imagem que será usada.

