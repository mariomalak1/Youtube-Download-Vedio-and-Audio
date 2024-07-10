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

from .utilize import get_type_from_video, exit_from_program

class VideoData:

    @staticmethod
    def get_video_data():
        videoObj = VideoData.get_video_link()
        dict_streams = VideoData.print_all_res(videoObj)
        itag = VideoData.get_specific_stream_number(dict_streams)
        destinationLocation = VideoData.get_valid_location()

        return videoObj.streams.get_by_itag(itag), destinationLocation

    @staticmethod
    def get_video_link():
        while True:
            link = input("Enter Link Video You Want To Download: ")
            try:
                exit_from_program(link)
                yt = YouTube(link)
                break
            except:
                print("please enter valid link")
        return yt

    @staticmethod
    def get_specific_stream_number(dict_streams):
        while(True):
            res = input("Enter Number Of Stream You Want To Download : ")
            exit_from_program(res)

            try:
                res = int(res)
                if res in dict_streams:
                    return dict_streams[res]
                else:
                    print("Please Enter Valid Number of Stream")
            except:
                print("Please Enter Valid Number of Stream")


    @staticmethod
    def get_valid_location():
        loc = input("Enter Location You Want to Download in It : ")

        exit_from_program(loc)

        if os.path.exists(loc):
            return loc
        else:
            print("Please Enter Valid Path in Your Machine")
            return VideoData.get_valid_location()


    @staticmethod
    def print_all_res(video):
        dict_streams = {}
        print("This All Types and Resolution That Found :")
        video_with_audio_streams = video.streams.filter(progressive=True).order_by("subtype").order_by("mime_type").desc()
        video_without_audio_streams = video.streams.filter(adaptive=True, only_video = True).order_by("subtype").order_by("mime_type").desc()
        audio_streams = video.streams.filter(adaptive=True, only_audio = True).order_by("subtype").order_by("mime_type").desc()

        counter = 0

        print("\nVideo With Audio: ")
        for stream in video_with_audio_streams:
            counter += 1
            print(f"Number : {str(counter)} - {get_type_from_video(stream.mime_type)} - Resolution : {stream.resolution} - Size : {stream.filesize_mb} mb")
            dict_streams[counter] = stream.itag

        print("\nVideo Without Audio: ")
        for stream in video_without_audio_streams:
            if stream.resolution:
                counter += 1
                print(f"Number : {str(counter)} - {get_type_from_video(stream.mime_type)} - Resolution : { stream.resolution } - Size : {stream.filesize_mb} mb")
                dict_streams[counter] = stream.itag

        print("\nAudio: ")
        for stream in audio_streams:
            counter += 1
            print(f"Number : {str(counter)} - {get_type_from_video(stream.mime_type)} - Appoggiaturas  : { stream.abr } - Size : {stream.filesize_mb} mb")
            dict_streams[counter] = stream.itag

        return dict_streams