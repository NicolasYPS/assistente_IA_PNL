# Assistente Virtual com Processamento de Linguagem Natural

Um assistente virtual de linha de comando que responde a comandos de voz usando Processamento de Linguagem Natural (PLN). Desenvolvido em Python com as bibliotecas `speech_recognition`, `gTTS`, `pygame` e `wikipedia`.

## Funcionalidades

- Reconhecimento de voz em português brasileiro
- Respostas por voz sintetizada
- Busca na Wikipedia por comando de voz
- Abertura de pesquisas no YouTube
- Localização da farmácia mais próxima via Google Maps
- Exibição da hora atual
- Encerramento do programa por comando

## Requisitos

- Python 3.8 ou superior
- Ambiente virtual recomendado

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/assistente_IA_PNL.git
cd assistente_IA_PNL
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate    # Windows
```

3. Instale as dependências:

```bash
pip install SpeechRecognition gTTS wikipedia pygame
```

4. Instale as dependências do sistema (Linux):

```bash
sudo apt update
sudo apt install portaudio19-dev python3-dev -y
```

## Uso

Execute o programa:

```bash
python main.py
```

O assistente iniciará e aguardará comandos de voz. Experimente:

- “abrir youtube”
- “pesquise na wikipedia sobre python”
- “onde fica a farmácia mais próxima”
- “que horas são”
- “sair”

## Observações

- O sistema foi testado e otimizado para Linux. Em outros sistemas operacionais, pode ser necessário ajustar as dependências de áudio.
- O módulo `pygame` foi utilizado em vez de `playsound` para garantir compatibilidade e estabilidade no Linux.
- O microfone deve estar funcionando e configurado corretamente no sistema.

## Estrutura do Projeto

```
assistente_IA_PNL/
├── main.py              # Código principal do assistente
├── venv/                # Ambiente virtual (não commitado)
└── README.md
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se quiser, posso gerar também um arquivo `LICENSE` padrão MIT para você incluir no repositório — é só pedir.