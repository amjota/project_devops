# Montando disco no linux para os dados armazenados fiquem fora dos container "Docker".

1. ### Identificando o novo disco

Para montar e configurar seu novo HD de 1TB no Linux, especialmente para armazenar dados do Nextcloud, siga este passo a passo:

Abra o terminal e execute o seguinte comando:

```bash
sudo fdisk -l
```
Esse comando listará todos os discos e partições no seu sistema. O novo disco geralmente será algo como /dev/sdb ou /dev/sdc, dependendo do seu sistema.

2. ### Criar uma partição no novo disco

Se o disco ainda não estiver particionado, você precisará criar uma partição.

Execute o seguinte comando para abrir o utilitário fdisk no novo disco (substitua /dev/sdb pelo identificador correto do seu novo disco):

```bash
sudo fdisk /dev/sdb
```
Dentro do fdisk, você pode seguir estes passos:

- Pressione n para criar uma nova partição.
- Pressione p para torná-la uma partição primária.
- Pressione 1 para escolher o número da partição.
- Pressione Enter para aceitar o primeiro e último setor padrão (utiliza o espaço completo).
- Pressione w para gravar as mudanças e sair.

3. ### Formatar a nova partição

Agora que a partição está criada, formate-a com o sistema de arquivos desejado. Para um uso comum, ext4 é uma boa escolha.

```bash
sudo mkfs.ext4 /dev/sdX1
```
Substitua /dev/sdX1 pela partição que você acabou de criar (geralmente, será algo como /dev/sdb1).

4. ### Criar um ponto de montagem
Agora, crie um diretório onde o disco será montado. Como você mencionou que ele será utilizado para armazenar dados do Nextcloud, podemos montá-lo diretamente no diretório de dados do Nextcloud.

```bash
mkdir -p /mnt/data
```
5. ### Montar o novo disco
Monte o novo disco no ponto de montagem criado:

```bash
sudo mount /dev/sdb1 /mnt/data
```
6. ### Criar os diretorios das Dockers
Dentro da pasta montada, crie os diretórios que serão usados por cada contêiner:

```bash
sudo mkdir -p /mnt/data/container1 /mnt/data/container2
```
No Docker, você pode montar esses diretórios em diferentes contêineres. Por exemplo, ao criar dois contêineres, um para cada diretório, use a opção -v para mapear o volume.

7. ### Configurar a montagem automática (opcional)
Para garantir que o disco seja montado automaticamente toda vez que o sistema iniciar, você deve adicionar uma entrada no arquivo /etc/fstab.

Abra o arquivo /etc/fstab com um editor de texto:

```bash
sudo nano /etc/fstab
```
Adicione a seguinte linha no final do arquivo:

```bash
/dev/sdb1 /mnt/data ext4 defaults 0 2
```

8. ### Alterar permissões
 O diretório /mnt/data/sql-amjota precisa ter permissões apropriadas para que o usuário que o contêiner está usando (mssql) possa gravar nele.

```bash
sudo chown -R www-data:www-data /mnt/data
sudo chown -R 10001:10001 /mnt/data/sql-amjota
```
Agora, o novo HD de 1TB está montado e pronto para ser usado como o armazenamento de dados do SQLServer.
