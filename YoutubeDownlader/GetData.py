"""
    this file that display all features and take valid response from the user
    this features will be as:
        - download specific video with link with a specific resolution if the video have it
    logic of this file will be :
        /*
            1- the user will ask to enter link of youtube video that want to download
            2- system will check this is a valid youtube link or not
            3- if it is not valid link he will go to step 1, else continue
            4- system will display all resolution are in this video
            5- the user will ask to enter a valid type, as like as "mp4", "mp3"
            6- if not valid will go to step 5, else continue
            7- user will ask to enter valid resolution for this type
            8- if not valid will go to step 8, else continue
            9- then user will ask for the name of the file he wants to download
            10- then he will ask for location for this file
            11- then this data will be sent to download video file and start to download
        */
"""

# importing the module
from pytube import YouTube
import os

# class DownloadVideo:
#     videoObj = ""
#     typeToDownload = ""
#     res = 0
#     destinationLocation = ""
#
#     def __init__(self, videoObj, typeToDownload, res, destinationLocation):
#         self.destinationLocation = destinationLocation
#         self.res = res
#         self.videoObj = videoObj
#         self.typeToDownload = typeToDownload
#
#     def __str__(self):
#         return str(self.videoObj.streams.filter(mime_type=self.typeToDownload, resolution=self.res))



class VideoData:
    @staticmethod
    def get_video_data():
        videoObj = VideoData.get_video_link()
        dict_streams = VideoData.print_video_res_types(videoObj)
        typeToDownload = VideoData.get_type_video(dict_streams)
        res = VideoData.get_resolution_video(dict_streams, typeToDownload)
        destinationLocation = VideoData.get_valid_location()
        file_name = VideoData.get_file_name()

        return videoObj.streams.filter(mime_type= typeToDownload, resolution= res).first(), destinationLocation, file_name


    @staticmethod
    def get_video_link():
        while True:
            link = input("enter link video you want to download : ")
            try:
                yt = YouTube(link)
                break
            except:
                print("please enter valid link")
        return yt

    @staticmethod
    def get_type_video(dict_streams):
        while True:
            video_type = input("enter video type as \"video/3gpp\" \"audio/mp4\" :  ")
            if video_type in dict_streams:
                return video_type
            else:
                print("please enter valid type as writen before")

    @staticmethod
    def get_resolution_video(dict_streams, type_video):
        while True:
            quality = input("enter quality of video or audio you want")
            if quality in dict_streams[type_video]:
                return quality
            else:
                print("please enter valid quality")

    @staticmethod
    def get_valid_location():
        loc = input("enter location you want to download in it : ")
        if os.path.exists(loc):
            return loc
        else:
            return VideoData.get_valid_location()

    @staticmethod
    def print_video_res_types(video):
        dict_streams = {}
        print("this all types and resolution that found")

        for stream in video.streams:
            dict_streams[stream.mime_type] = []


        for stream_mime_type in dict_streams:
            for stream in video.streams.filter(mime_type = stream_mime_type):
                if stream.resolution:
                    dict_streams[stream_mime_type].append(stream.resolution)
                elif stream.audio_codec:
                    dict_streams[stream_mime_type].append(stream.audio_codec)
            if dict_streams[stream_mime_type]:
                print(str(stream_mime_type) + " : " + str(dict_streams[stream_mime_type]))

        return dict_streams

    @staticmethod
    def get_file_name():
        name = input("enter name of file as you want to save it, to download with the common name enter x")
        return name
