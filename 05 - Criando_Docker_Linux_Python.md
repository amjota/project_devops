# Criando sua Docker do zero com Linux Ubuntu e Python

#### Entrar no diretorio de sua preferencia e criar os seguintes arquivos: Exemplo (/mnt/data/dev-amjota/Docker_Dev)

```bash
sudo mkdir Docker_Dev
```
#### Agora vamos criar o arquivo Dockerfile utilizando o editor "**NANO**":

```bash
sudo nano Dockerfile
```
#### Com este comando vai abrir o editor onde você irá inserir o script abaixo:

```bash
# Use a imagem base do Ubuntu
FROM ubuntu:20.04

# Informar o mantenedor da imagem
LABEL maintainer="Amjota andrejota@amjota.com.br"

# Evitar prompts durante a instalação
ARG DEBIAN_FRONTEND=noninteractive

# Atualiza o sistema e instala dependências básicas
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    curl \
    git

# Criar o usuário amjota
RUN useradd -ms /bin/bash amjota

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /workspace

# Alterar a propriedade do diretório para o usuário amjota
RUN chown -R seuuser:seuuser /workspace

# Copiar o arquivo requirements.txt para o contêiner
# COPY requirements.txt /workspace/

# Instalar as dependências Python com o usuário amjota
# USER seuuser
# RUN pip3 install --user -r requirements.txt

# Definir o comando padrão para rodar o contêiner
CMD [ "python3" ]
```
- Após inserir o script tecle CTRL + O / Enter para salvar - CTRL + X para sair

#### Construir a Imagem Docker

- Depois de criar o Dockerfile, você precisa construir a imagem. No diretório onde seu Dockerfile está localizado, execute:

```bash
docker build -t my-python-container .
```
#### Agora iremos rodar o contêiner
- Depois de construir a imagem, você pode rodar o contêiner com o seguinte comando:

```bash
docker run -d -it --name dev-amjota \
-v /mnt/data/dev-amjota:/workspace \
--restart unless-stopped \
my-python-container \
/bin/bash
```
- O diretório /mnt/data/dev-amjota no host será montado no diretório /workspace do contêiner.
- Qualquer arquivo criado ou modificado dentro do contêiner no diretório /workspace será persistido no host.
- Agora, se o servidor for reiniciado, o Docker irá garantir que o contêiner dev-amjota seja reiniciado automaticamente.

#### Verificação
Você pode acessar o contêiner e verificar se o volume foi montado corretamente:

```bash
docker exec -it dev-amjota-container /bin/bash
ls /workspace
```
Qualquer alteração feita no diretório /workspace dentro do contêiner será refletida no diretório /mnt/data/dev-amjota no host.

#### Ajustar permissões
Para garantir que você tenha acesso total (leitura, escrita e execução) ao diretório e seus arquivos, você pode alterar as permissões com os comandos abaixo:

#### Permitir Acesso ao Usuário Atual
```bash
sudo chown -R $USER:$USER /mnt/data/dev-amjota/project_devops
```
Isso garante que você (usuário atual) seja o proprietário do diretório e todos os arquivos/subdiretórios.

#### Ajustar Permissões de Leitura, Escrita e Execução
Para garantir que o proprietário do diretório tenha permissões completas:

```bash
sudo chmod -R 770 /mnt/data/dev-amjota/project_devops
```
Isso concede:

- 7: Permissão total (leitura, escrita e execução) ao proprietário.
- 7: Permissão total ao grupo.
- 0: Nenhuma permissão para outros usuários.

#### Instalar Dependências Python (opcional)
- Se você quiser instalar pacotes Python adicionais, como numpy, pandas, ou outros, você pode adicionar uma linha no Dockerfile para instalar as bibliotecas, ou rodar pip diretamente no contêiner.
- Dentro do contêiner, use o pip normalmente:
```bash
pip install numpy pandas
```
Ou, você pode criar um arquivo requirements.txt no seu diretório local e adicionar ao Dockerfile:

```bash
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt
```
#### Criando o requirements.txt
- Se você já tem um ambiente Python configurado com todas as dependências instaladas, você pode gerar automaticamente o requirements.txt usando o comando:

```bash
pip freeze > requirements.txt
```

### Resumo

1. Crie um Dockerfile com base no Ubuntu e instale Python.
2. Construa a imagem Docker com docker build.
3. Rode o contêiner usando docker run.
4. Opcionalmente, monte volumes ou instale bibliotecas Python adicionais.

Agora você tem um contêiner com Linux e Python pronto para desenvolvimento!
