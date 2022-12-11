# Importation de la playlist
from pytube import Playlist
from pytube import YouTube
from pprint import pprint

def downloader():
    lien = input("Entrer le lien ici: ")
    PATH_SAVE = '/home/dgratias/Vidéos/yt_videos' #Le dossier doit être déjà créer (mkdir)

    try:
        try: 
            p = Playlist(lien)
            PATH_SAVE+='/playlists'     #J'ai ajouté le nouveau dossier dans l'ancien avent de continuer
            print(f"Téléchargement de: {p.title}, {p.length} secondes")
            cpt_vid = 1
            for video in p.videos:
                print(f"\t#{cpt_vid}---> downloading '", video.title, " '" ,convertSeconde(video.length))
                video.streams.first().download(PATH_SAVE)
                print(f"\t{video.title} was download seccesfully to {PATH_SAVE}\n")
                cpt_vid+=1
        except:
            video = YouTube(lien)
            print("# ",video.title, convertSeconde(video.length))
            d_video = video.streams.filter(res="720p").first()
            d_video.download(PATH_SAVE)
            print("download complete")
    except: 
        print("Video not found...")
        


def convertSeconde(secondes):
    sec = secondes
    min = 0
    hour = 0

    if sec > 60:
        sec = secondes%60
        min = secondes//60
        if min > 60:
            min = min%60
            hour = min//60

    str_secondes = f" {hour}h: {min}m: {sec}s "
    return str_secondes


def filesFilter(video):
    list_info = video.filter()
    liste_info_aud = video.filter('mp3')
    list_info.append(liste_info_aud)
    return list_info


downloader()