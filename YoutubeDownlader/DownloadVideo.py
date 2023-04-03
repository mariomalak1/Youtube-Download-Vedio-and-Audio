from . import GetData


def download():
    videoObj, destination_location, file_name = GetData.VideoData().get_video_data()
    videoObj.download(destination_location, file_name + "." + str(videoObj.subtype))