import tkinter
from pytube import YouTube
import customtkinter

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onP)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded", text_color="white")
    except Exception as e:
        finishLabel.configure(text=f"An error occurred: {e}", text_color="red")
    
    
def onP(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    perc_of_comp = bytes_downloaded / total_size * 100
    per = str(int(perc_of_comp))
    pPerc.configure(text = per + '%')
    pPerc.update()
    
    #prog Bar
    progressBar.set(float(perc_of_comp + 16) / 100 )
    
# sys settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# title
title = customtkinter.CTkLabel(app, text="Paste the YouTube Link: ")
title.pack(padx=10, pady=10)

# link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finish download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# progress %
pPerc = customtkinter.CTkLabel(app, text="0.00%")
pPerc.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# warning label
warning = customtkinter.CTkLabel(app, text="Videos should not be age restricted for the downloader to work", text_color="red")
warning.pack(pady=120)

app.mainloop()

