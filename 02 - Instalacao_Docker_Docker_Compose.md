# Instalando o Docker e Docker Compose

#### Atualizando o Sistema

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

#### Instalando as Dependências, pois algumas dependências são necessárias para que a instalação ocorra sem problemas.

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

### Agora vamos iniciar a instalação o Docker.

- Com os requisitos instalados, a próxima etapa é instalar o Docker. Instalaremos o Docker Community Edition ( **Docker CE** ), que é de código aberto e gratuito para download e uso.

#### Para fazer isso, adicionaremos a chave GPGK

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### Agora iremos instalar o Docker

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

#### Após a instalação, inicie e habilite o serviço do Docker:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

#### Depois que o comando for executado com êxito, considere adicionar o usuário conectado no momento ao grupo docker. Isso permite que você execute o docker sem invocar o sudo.

```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### Verificando a versão do Docker

```bash
docker --version
```
# Instalando Docker Compose

## Agora iremos instalar a versão latest:

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

#### Configure as permissões corretas para o arquivo baixado:

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

#### Verifique a instalação usando o comando a seguir:

```bash
docker-compose --version
```
