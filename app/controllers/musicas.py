import json
import requests
class musicas():
    def __init__(self,id):
        self.album = requests.get('https://theaudiodb.com/api/v1/json/1/album.php?i={0}'.format(id)).json()
    
    def albumInf(self):
        albumInfo = self.album['album']
        self.jsonAlbum = {
            'idAlbum':[],
            'nomeAlbum':[],
            'anoLacamento':[],
            'gravadora':[],
            'descricao':[],
            'logo':[]
        }
       
        for albuns in albumInfo:
            self.jsonAlbum['idAlbum'].append(albuns['idAlbum'])
            self.jsonAlbum['nomeAlbum'].append(albuns['strAlbum'])
            self.jsonAlbum['anoLacamento'].append(albuns['intYearReleased'])
            self.jsonAlbum['gravadora'].append(albuns['strLabel'])
            if 'strDescriptionPT' in albuns and 'strDescriptionEN' in albuns:
                self.jsonAlbum['descricao'].append(albuns['strDescriptionPT']  if albuns['strDescriptionPT'] != None else albuns['strDescriptionEN'])
            else:
                self.jsonAlbum['descricao'].append('')
            self.jsonAlbum['logo'].append(albuns['strAlbumThumb'])
        return self.jsonAlbum

    def musicaAlbumInf(self):
        jsonMusica = dict()
        idAlbum = self.albumInf()
        for id in idAlbum['idAlbum']:
            musicasA = requests.get('https://theaudiodb.com/api/v1/json/1/track.php?m={0}'.format(id)).json()
            musicasA = musicasA['track']
            for inf in musicasA:
                if id in jsonMusica:
                    jsonMusica[id].append({
                        'idMusica':inf['strTrack'],
                        'duracao':inf['intDuration'],
                        'numeroMusica':inf['intTrackNumber'],
                        'logo':inf['strMusicVidScreen1']
                    })
                else:
                    jsonMusica[id] = [{
                        'idMusica':inf['strTrack'],
                        'duracao':inf['intDuration'],
                        'numeroMusica':inf['intTrackNumber'],
                        'logo':inf['strMusicVidScreen1']
                    }]
        return jsonMusica