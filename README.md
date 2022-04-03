# redes-projeto-a

Para rodar o projeto você deve possuir python3 instalado em sua máquina e estar em ambiente unix


## Como executar o projeto
Para rodar o projeto é nescessário primeiramente rodar o arquivo server.py com o seguinte comando
```shell
  python3 server.py
```
E então insira seus dados de IP do servidor e porta

Após este passo é nescessário rodar o arquivo client.py em um terminal/estação diferente com o comando  
```shell
  python3 client.py
```
E inserir o IP e a Porta que foram inseridos nos campos de servidor para conexão
Após isso os terminais estão prontos para se conversar basta inserir uma mensagem no cliente que ele irá aparecer no servidor

## Para respostas no servidor
Para responder uma mensagem, primeiro aparecerá uma listagem das mensagens que chegaram dos clientes e então você deve inserir os dados de IP e Porta do cliente desejado e então enviar sua resposta.



### Exemplo
```shell 
Client ('127.0.0.1', 48036):
{
  'Ip_Origem': '127.0.1.1',
  'Ip_Destino': '127.0.0.1',
  'Porta_Origem': 0,
  'Porta_Destino': 8080,
  'Timestamp': '23:26:50',
  'Mensagem': 'mensagem daora'
}

DIGITE O IP DO CLIENTE:
-> 127.0.0.1
DIGITE A PORTA:
-> 48036

```


