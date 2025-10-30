Gerador de QR Code

Este é um script simples em Python para gerar códigos QR a partir de URLs fornecidas pelo usuário. Os QR Codes gerados são salvos como arquivos de imagem PNG em um diretório chamado qrcodes_gerados.

Pré-requisitos

Python 3.6 ou superior instalado em seu sistema.

Configuração do Ambiente

Siga estes passos para configurar seu ambiente de desenvolvimento e instalar as dependências necessárias.

1. Crie o Ambiente Virtual (venv)

É uma boa prática usar um ambiente virtual para isolar as dependências do seu projeto.

Abra seu terminal ou prompt de comando, navegue até a pasta onde você salvou os arquivos (gerador_qrcode.py e requirements.txt) e execute o seguinte comando para criar um ambiente virtual chamado venv:

No macOS ou Linux:

python3 -m venv venv


No Windows:

python -m venv venv


2. Ative o Ambiente Virtual

Antes de instalar as dependências, você precisa "ativar" o ambiente:

No macOS ou Linux:

source venv/bin/activate


(Você verá (venv) aparecer no início da linha do seu terminal).

No Windows (Prompt de Comando):

.\venv\Scripts\activate


(Você verá (venv) aparecer no início da linha do seu terminal).

3. Instale as Dependências

Com o ambiente virtual ativado, use o pip para instalar as bibliotecas listadas no arquivo requirements.txt. O arquivo requirements.txt deve conter apenas a linha qrcode[pil], que instala a biblioteca de QR Code e a biblioteca de imagem (Pillow) da qual ela depende.

Execute o comando:

pip install -r requirements.txt


Como Usar o Script

Depois de instalar as dependências, você pode executar o script.

Certifique-se de que seu ambiente virtual (venv) ainda esteja ativado.

Execute o script gerador_qrcode.py usando o seguinte comando:

python gerador_qrcode.py


O script solicitará duas informações no terminal:

Digite a url: Cole ou digite a URL completa (ex: https://www.google.com) e pressione Enter.

Digite o nome do arquivo QrCode (ex: meu_qrcode): Digite o nome que você deseja dar ao arquivo de imagem (ex: site_empresa) e pressione Enter. Você não precisa adicionar a extensão .png, o script faz isso automaticamente.

Resultado

Após a execução:

Uma nova pasta chamada qrcodes_gerados será criada no mesmo diretório do script (se ainda não existir).

Seu arquivo de imagem QR Code (ex: site_empresa.png) será salvo dentro desta pasta (A PASTA SERÁ CRIADA AUTOMATICAMENTE, SEU NOME SERA "qrcodes_gerados").