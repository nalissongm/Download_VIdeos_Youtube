from pytube import YouTube
import os

class DownloadYT:
    def __init__(self,link,path_dw):
        self.link = link
        self.path_dw = path_dw

    def start_download(self,option_down):
        yt = YouTube(self.link) 

        if option_down == 1:
            try:
                download_vid = yt.streams.get_highest_resolution()
                download_vid.download(self.path_dw)
                return True
            except Exception as e:
                print(e)
                return False
        
        if option_down == 2:
            try:
                download_vid = yt.streams.get_lowest_resolution()
                download_vid.download(self.path_dw)
                return True
            except Exception as e:
                print(e)
                return False
        
        if option_down == 3:
            try:
                download_vid = yt.streams.filter(only_audio=True).first()
                out_file = download_vid.download(self.path_dw)

                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                return True
            except Exception as e:
                print(e)
                return False