import sys
import os
from moviepy.editor import *
import torch
import ffmpeg as fp

from ffmpeg import *


#ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "c:\Users\seca\Documents\UNMUSIC\Videos\Maguires Crack.mp4" 
# 
# -i "c:\Users\seca\Documents\UNMUSIC\Audios\Maguires Crack.wav" -c:v copy -map 0:v:0 -map 1:a:0 "c:\Users\seca\Documents\UNMUSIC\Audios\newtest.mp4"


vid_path = str(r'"c:\Users\seca\Documents\UNMUSIC\Videos\Maguires Crack.mp4"')

aud_path = str(r'"c:\Users\seca\Documents\UNMUSIC\Audios\Maguires Crack.wav"')

out_path = str(r'"c:\Users\seca\Documents\UNMUSIC\Audios\newtest.mp4"')



def cont_extr (a_path, v_path, out_name, choice):

    out_aud = "palcehold"
    out_vid = out_aud

    choice = "random"

    if choice == "cpu":

        os.system(rf"ffmpeg -i {v_path} -map 0:a {out_aud} -map 0:v {out_vid}")


    if choice == "gpu":
        
        os.system(rf"ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i {v_path} -map 0:a {out_aud} -map 0:v {out_vid}")


    return out_vid


def aud_rep(vid_path, aud_path, out_path):
    
    pass




print(vid_path)

print(rf"{vid_path}")

print(f"{vid_path}")


#os.system("ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i c:\Users\seca\Documents\UNMUSIC\Videos\Maguires Crack.mp4 -i c:\Users\seca\Documents\UNMUSIC\Audios\Maguires Crack.wav -c:v copy -map 0:v:0 -map 1:a:0"
#+ " c:\Users\seca\Documents\UNMUSIC\Audios\newtest.mp4")
#^ Defunct

os.system(rf"ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i {vid_path} -i {aud_path} -c:v copy -map 0:v:0 -map 1:a:0"
+ rf" {out_path}" + " -y")

#print((rf"ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i {vid_path} -i {aud_path} -c:v copy -map 0:v:0 -map 1:a:0"
#+ rf" {out_path}"))





#fp.input(aud_path, vid_path)