from . import GetData


def download():
    videoObj, destination_location = GetData.VideoData().get_video_data()
    vedioTitle = input("If you want to download with the same video name press x, else enter video name without extension: ")
    if vedioTitle.lower() == "x":
        vedioTitle = videoObj.title
    print("vedioTitle :", vedioTitle)
    videoObj.download(destination_location, vedioTitle + "." + str(videoObj.subtype))


def main():
    print("Hello in YouTube Download Program")
    print("If You Want to Exit in Any Response Enter X")

    while(True):
        # try:
            download()
        # except:
            # print("Sorry, happen an error while downloading")
