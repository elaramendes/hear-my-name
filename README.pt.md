# Hear-My-Name

**Hear-My-Name** é um aplicativo que captura sons e emite um aviso quando detecta o nome de uma pessoa. O projeto utiliza reconhecimento de voz com a biblioteca **Vosk** para ouvir sons em tempo real e alerta o usuário quando seu nome é mencionado.

## Membros

- Elara Mendes
- Victor Emanuel
- Pollyana Caetano

## Funcionalidades

- Captura de som em tempo real.
- Reconhecimento de voz usando **Vosk** para identificar o nome da pessoa.
- Emissão de aviso quando o nome é detectado.
- Interface intuitiva para visualização do texto falado.

## Requisitos

- **Python 3.9**

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Bibliotecas**:
  - `Vosk`: Para reconhecimento de fala offline.
  - `Flet`: Para a interface gráfica do usuário.
  - `PyAudio`: Para a captura do áudio em tempo real.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/elaramendes/hear-my-name.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd hear-my-name
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Baixe o modelo de idioma para o Vosk:
   - Visite a página oficial do [Vosk Models](https://alphacephei.com/vosk/models) e baixe o modelo apropriado para o idioma desejado.
   - Extraia o modelo no diretório do projeto.


5. Instruções de Configuração:
   - Crie uma pasta chamada `model` no diretório raiz do projeto para armazenar o modelo Vosk.
   - No diretório raiz do projeto, crie um arquivo chamado `text.txt` para receber o texto transcrito em tempo real.

## Como Usar

1. Execute o aplicativo:
   ```bash
   python gui.py
   ```

   **Nota**: Pode ser necessário selecionar o microfone correto no arquivo `cli.py`. Para isso, ajuste o parâmetro `device_index`:

   ```python
   device_index = 3
   stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024, input_device_index=device_index)
   ```

2. Insira o nome que deseja monitorar no campo específico.

3. O aplicativo capturará sons e notificará quando o nome for mencionado.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou fazer pull requests com melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE.txt).