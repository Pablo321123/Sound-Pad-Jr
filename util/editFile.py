from model.mediaPlayerModel import SongModel

class EditFile:
    
    def __init__(self, file) -> None:
        self.arq = file
        
    def saveInFile(self, dic_SongModel):
        with open(self.arq, 'w') as file:
            for song in dic_SongModel:
                print(dic_SongModel[song].__str__())
                file.write(dic_SongModel[song].__str__() + '\n')           
    
    def readFile(self) -> SongModel:
        dic_SongModel = {}
        song = None
        with open(self.arq, 'r') as file:
            #variavel para receber os dados dos audios gravados no arquivo
            for linha in file:
                if linha != '\n':
                    aux = linha.split(':')
                    song = SongModel(aux[0], aux[1], aux[2], f"{aux[3]}:{aux[4]}")
                    
                    dic_SongModel[song.name] = song
                
        return dic_SongModel
            
    