import base64
import os

def arquivo_para_base64(caminho_arquivo):
    """
    Transforma um arquivo em uma string Base64.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo a ser codificado.

    Returns:
        str: A string Base64 do conteúdo do arquivo, ou None se o arquivo não for encontrado.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    
    if not os.path.isfile(caminho_arquivo):
        print(f"Erro: '{caminho_arquivo}' não é um arquivo válido.")
        return None

    try:
        with open(caminho_arquivo, "rb") as arquivo:
            conteudo_arquivo = arquivo.read()
            conteudo_base64 = base64.b64encode(conteudo_arquivo)
            return conteudo_base64.decode('utf-8')  # Decodifica para string para facilitar o uso
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

def base64_para_arquivo(string_base64, caminho_saida):
    """
    Transforma uma string Base64 de volta em um arquivo.

    Args:
        string_base64 (str): A string Base64 a ser decodificada.
        caminho_saida (str): O caminho completo para onde o arquivo decodificado será salvo.
    
    Returns:
        bool: True se o arquivo foi salvo com sucesso, False caso contrário.
    """
    try:
        conteudo_decodificado = base64.b64decode(string_base64)
        with open(caminho_saida, "wb") as arquivo_saida:
            arquivo_saida.write(conteudo_decodificado)
        print(f"Arquivo decodificado salvo em: {caminho_saida}")
        return True
    except Exception as e:
        print(f"Erro ao decodificar e salvar o arquivo: {e}")
        return False

if __name__ == "__main__":
    # Exemplo de uso:
    caminho_executavel = "C:\\Users\\marce\\Downloads\\lister\\lister.exe"  # Mude para o caminho real do seu executável
    nome_arquivo_saida_base64 = "executavel_codificado.txt"
    nome_arquivo_recuperado = "executavel_recuperado.exe"

    # --- Codificar o arquivo executável para Base64 ---
    print(f"Codificando '{caminho_executavel}' para Base64...")
    executavel_em_base64 = arquivo_para_base64(caminho_executavel)

    if executavel_em_base64:
        print("\nArquivo executável codificado em Base64 (primeiros 100 caracteres):\n")
        print(executavel_em_base64[:100] + "...") # Mostra apenas o início para não sobrecarregar
        
        # Opcional: Salvar a string Base64 em um arquivo de texto
        try:
            with open(nome_arquivo_saida_base64, "w") as f:
                f.write(executavel_em_base64)
            print(f"\nString Base64 salva em '{nome_arquivo_saida_base64}'")
        except IOError as e:
            print(f"Erro ao salvar a string Base64: {e}")

        # --- Decodificar a string Base64 de volta para um arquivo executável ---
        print(f"\nDecodificando a string Base64 de volta para '{nome_arquivo_recuperado}'...")
        base64_para_arquivo(executavel_em_base64, nome_arquivo_recuperado)

        # Você pode verificar se o arquivo recuperado é igual ao original usando ferramentas de hash
        # (md5sum, sha256sum, etc.) ou simplesmente tentando executá-lo (com cuidado).
    else:
        print("A codificação Base64 não foi realizada devido a um erro.")

    print("\nFim do programa.")
