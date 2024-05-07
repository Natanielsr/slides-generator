import glob
import os
import re  # Importar expressões regulares
class FileReader:

    def __init__(self):
         self.__path = 'musics/'
         self.__ext = '*.txt'
    
    def read_file(self, file_name):
        full_path = self.__path+file_name
        # Abra o arquivo para leitura
        arquivo = open(full_path, "r", encoding='utf-8')
        # Leia todo o conteúdo do arquivo
        content = arquivo.read()

        return content

    def get_files_name(self):
        # Especifica o caminho da pasta
        txt_path = self.__path+self.__ext

        # Obtém todos os arquivos .txt usando um padrão
        txt_files = glob.glob(txt_path)

        # Filtra para obter apenas arquivos
        txt_files_name = [os.path.basename(file) for file in txt_files]
        ordened_txt_files_name = sorted(txt_files_name, key=self._obter_numero)
        return ordened_txt_files_name
    
    # Função para extrair número do início da string
    def _obter_numero(self, item):
        match = re.match(r"^\d+", item)  # Procura por números no início da string
        if match:
            return int(match.group(0))  # Retorna o número como inteiro
        return 0  # Se não houver número, retorna 0
    


