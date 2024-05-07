from src.music import Music
from src.file_reader import FileReader
from src.utils.format import Format
class MusicList:
    def create_music_list(self):
        file_reader = FileReader()
        txt_files_name = file_reader.get_files_name()

        musics = []
        
        for file_name in txt_files_name:
            
            music = self._create_music(
                Format.remove_ext_name(file_name),
                file_reader.read_file(file_name))
            
            musics.append(music)

        return musics
    
    def _create_music(self, title, content):
        return Music(title, content)