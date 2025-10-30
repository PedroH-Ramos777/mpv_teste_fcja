import qrcode
import os

DIRETORIO_SAIDA = "qrcodes_gerados" 

def gerar_qrcode_url(url, nome_arquivo):
    """
    Gera um QR Code a partir de uma URL e salva como uma imagem PNG.

    Args:
        url (str): A URL que será codificada no QR Code.
        nome_arquivo (str): O nome do arquivo de imagem a ser salvo.

    """
    # Constrói o caminho completo: pasta_saida/nome_do_arquivo.png
    # O os.path.join garante que o separador de barra esteja correto para Windows ou Linux/macOS
    caminho_completo_arquivo = os.path.join(DIRETORIO_SAIDA, nome_arquivo)

    try:
        # 1. Cria o diretório de saída se ele não existir
        if not os.path.exists(DIRETORIO_SAIDA):
            os.makedirs(DIRETORIO_SAIDA)
            print(f"📁 Diretório '{DIRETORIO_SAIDA}' criado.")

        #c 2. Cria um objeto QR Code
        # version=1: menor e menos complexo (pode aumentar automaticamente)
        # box_size=10: controla quantos pixels cada "caixa" do QR Code terá
        # border=4: espessura da borda branca ao redor do QR Code
        qr = qrcode.QRCode(
            version=1,
            # CORREÇÃO APLICADA AQUI: Deve ser 'qrcode.constants'
            error_correction=qrcode.constants.ERROR_CORRECT_L, # Nível de correção de erro (L, M, Q, H)
            box_size=10,
            border=4,
        )

        # 3. Adiciona os dados (a URL)
        qr.add_data(url)
        qr.make(fit=True) # Ajusta o tamanho da matriz se a URL for grande

        # 4. Cria a imagem
        img = qr.make_image(fill_color="black", back_color="white")

        # 5. Salva o arquivo
        img.save(caminho_completo_arquivo)

        print(f"✅ QR Code gerado com sucesso!")
        print(f"Arquivo salvo como: {nome_arquivo}")

    except Exception as e:
        print(f"❌ Ocorreu um erro ao gerar o QR Code: {e}")


# --- EXECUTAR A FUNÇÃO ---
digiteUrl = input("Digite a url: ")
arquivo_nome = input("Digite o nome do arquivo QrCode (ex: meu_qrcode): ")

# Adicionando a verificação de URL para evitar erros de entrada vazia
if not digiteUrl:
    print("❌ URL não digitada. O programa será encerrado.")
else:
    url_do_site = digiteUrl 
    nome_do_arquivo = (arquivo_nome + ".png")
    gerar_qrcode_url(url_do_site, nome_do_arquivo)