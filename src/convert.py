from os import path
from pydub import AudioSegment
from tinytag import TinyTag



import os
start_path = '/tmp' # current directory
for dirpath,dirs,files in os.walk(start_path):
    for filename in files:
        if filename.endswith('.wma'):
            src = path.join(dirpath,filename)
            dest = path.join(dirpath,(filename[0:-4] + ".mp3"))
            print(src)            
            tag = TinyTag.get(src)
            # convert wav to mp3                                                            
            sound = AudioSegment.from_file(src)
            sound.export(dest, format="mp3", bitrate="192k", tags={'artist': tag.artist, 'album': tag.album, 'track': tag.track, 'title' : tag.title, 'album_artist' : tag.albumartist})
            os.remove(src)
            print(dest)
