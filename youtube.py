import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

myproxy = {"https":"https://192.168.49.1:8000"}
def StartDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_lowest_resolution()
        video.download()
        print(f"El lik que pusiste es: {ytLink}")
    except VideoUnavailable:
        print(f"Algo ocurrió y no se puede bajar el video{ytObject.title} {ytLink}")
    else:
        print(f"El video {ytObject.title} ha sido descargado!")
#configuraciones de sistema
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")  

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Dowloader Angel")

#Add UI Elements
title = customtkinter.CTkLabel(app,width=140,height=28,corner_radius=5,text="Inserte el URL de Youtube que copió")
title.pack()

#link imput
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=300,height=28,corner_radius=5,border_width=5, textvariable=url_var)
link.pack(padx=20, pady=20)

#Download Button
download = customtkinter.CTkButton(app,width=140,height=28,corner_radius=3,text="DOWNLOAD",command=StartDownload)
download.pack(padx=30,pady=30)
#correr ui
app.mainloop()

