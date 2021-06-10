from pytube import YouTube

vedio_list = open("sample.txt", "r")
for i in vedio_list:
    yt= YouTube(i)
    try:
        dw =yt.streams.first()
        dw.download("C:/")
        print("Download completed")
    except:
        print("Download failed!")