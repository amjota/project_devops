## Montando o diretório de projetos do HOST dentro do container.

Para montar uma unidade externa onde você possa armazenar seus projetos fora do contêiner Docker e ainda acessá-los dentro do contêiner, você pode usar volumes Docker ou montar um diretório do host no contêiner. Isso permite que seus arquivos fiquem fora do contêiner, mas sejam acessíveis dentro dele, garantindo que seus projetos não sejam excluídos quando o contêiner for removido ou parado.

Aqui estão os passos para montar um diretório do host em um contêiner Docker:

1. #### Criar um Diretório no Servidor (Host)

Primeiro, crie um diretório no sistema de arquivos do host (servidor) onde seus projetos serão armazenados.

- **No host**: Crie um diretório para os projetos.

```bash
mkdir /home/user/projetos
```
Substitua /home/user/projetos pelo caminho onde você quer armazenar seus projetos.

2. #### Montar o Diretório do Host no Contêiner com Volumes

Ao iniciar o contêiner Docker, você pode usar a opção -v (volume) para montar o diretório do host no contêiner.

O comando a seguir faz o mapeamento entre um diretório no host (/home/user/projetos) e um diretório dentro do contêiner (por exemplo, /workspace):

```bash
docker run -it -v /home/user/projetos:/workspace --name dev-container my-python-container
```

Neste exemplo:

- O diretório /home/user/projetos no host será montado no diretório /workspace dentro do contêiner.
- Qualquer arquivo que você criar ou editar em /workspace dentro do contêiner será salvo diretamente no diretório /home/user/projetos do host.

3. #### Acessar o Diretório Montado no Contêiner
- Agora, dentro do contêiner, você pode acessar o diretório montado:

```bash
cd /workspace
```
Os arquivos criados nesse diretório estarão visíveis tanto no host quanto no contêiner.

4. #### Verificar o Volume no Contêiner
Você pode verificar os volumes montados em um contêiner em execução usando o comando:

```bash
docker inspect dev-container
```
Isso mostrará detalhes sobre o contêiner, incluindo os volumes que estão montados.

5. #### Verificar os Arquivos no Contêiner
Após rodar o contêiner, você pode verificar se os arquivos estão acessíveis dentro do contêiner:

```bash
docker exec -it dev-container bash
cd /home/amjota
ls
```
Isso deve listar os arquivos que foram movidos para o host e estão sendo montados no contêiner.

## Benefícios:
- Persistência: Seus projetos estarão salvos no host e não serão perdidos se o contêiner for removido.
- Sincronização: Qualquer mudança feita dentro do contêiner em /home/amjota será refletida diretamente no diretório do host.
