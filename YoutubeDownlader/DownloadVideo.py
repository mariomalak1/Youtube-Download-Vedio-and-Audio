from . import GetData


def download():
    videoObj, destination_location, file_name = GetData.VideoData().get_video_data()
    if file_name.capitalize() == "Y":
    videoObj.download(destination_location, videoObj.title + "." + str(videoObj.subtype))

def main():
    print("Hello in YouTube Download Program")
    print("If You Want to Exit in Any Response Enter X")

    while(True):
        download()
