# Evolution Client Python

Client Python para interagir com a API Evolution.

## Instalação

```bash
pip install evolution-client
```

## Uso Básico

### Inicializando o Cliente

```python
from evolution.client import EvolutionClient

client = EvolutionClient(
    base_url='http://seu-servidor:porta',
    api_token='seu-token-api'
)
```

### Gerenciamento de Instâncias

#### Listar Instâncias
```python
instances = client.instances.fetch_instances()
```

#### Criar Nova Instância
```python
from evolution.models.instance import InstanceConfig

config = InstanceConfig(
    instanceName="minha-instancia",
    integration="WHATSAPP-BAILEYS",
    qrcode=True
)

nova_instancia = client.instances.create_instance(config)
```

### Operações com Instâncias

#### Conectar Instância
```python
estado = client.instance_operations.connect(instance_id, instance_token)
```

#### Verificar Estado da Conexão
```python
estado = client.instance_operations.get_connection_state(instance_id, instance_token)
```

#### Definir Presença
```python
from evolution.models.presence import PresenceStatus

client.instance_operations.set_presence(
    instance_id,
    PresenceStatus.AVAILABLE,
    instance_token
)
```

### Enviando Mensagens

#### Mensagem de Texto
```python
from evolution.models.message import TextMessage

mensagem = TextMessage(
    number="5511999999999",
    text="Olá, como vai?",
    delay=1000  # delay opcional em ms
)

response = client.messages.send_text(instance_id, mensagem, instance_token)
```

#### Mensagem de Mídia
```python
from evolution.models.message import MediaMessage, MediaType

mensagem = MediaMessage(
    number="5511999999999",
    mediatype=MediaType.IMAGE.value,
    mimetype="image/jpeg",
    caption="Minha imagem",
    media="base64_da_imagem_ou_url",
    fileName="imagem.jpg"
)

response = client.messages.send_media(instance_id, mensagem, instance_token)
```

#### Mensagem com Botões
```python
from evolution.models.message import ButtonMessage, Button

botoes = [
    Button(
        type="reply",
        displayText="Opção 1",
        id="1"
    ),
    Button(
        type="reply",
        displayText="Opção 2",
        id="2"
    )
]

mensagem = ButtonMessage(
    number="5511999999999",
    title="Título",
    description="Descrição",
    footer="Rodapé",
    buttons=botoes
)

response = client.messages.send_buttons(instance_id, mensagem, instance_token)
```

#### Mensagem com Lista
```python
from evolution.models.message import ListMessage, ListSection, ListRow

rows = [
    ListRow(
        title="Item 1",
        description="Descrição do item 1",
        rowId="1"
    ),
    ListRow(
        title="Item 2",
        description="Descrição do item 2",
        rowId="2"
    )
]

section = ListSection(
    title="Seção 1",
    rows=rows
)

mensagem = ListMessage(
    number="5511999999999",
    title="Título da Lista",
    description="Descrição da lista",
    buttonText="Clique aqui",
    footerText="Rodapé",
    sections=[section]
)

response = client.messages.send_list(instance_id, mensagem, instance_token)
```