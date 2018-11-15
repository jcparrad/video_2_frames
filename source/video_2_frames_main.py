import os
import cv2
import shutil
import video_2_frames as v2f 

# This code shows how to use the api for getting frames from a video.
# You can get all the frames or only every n_frames .
# If get_all_frames then the frames are saved in the folder all_frames
# if select_some_frames, the default n_frames is 15. you can change it wuth getter_v2f.set_n_frames(n_frames. The frames are saved in the folder selected_frames

# initialize the get_frames_from_video object 
getter_v2f = v2f.get_frames_from_video()

# set the video file path 
video_file_path = "/home/get_frames_from_video/data/video/DJI_3560.MP4"
getter_v2f.set_video_file_path(video_file_path)

#set the n_frames for getting only some frames
getter_v2f.set_n_frames(15) # if select_some_frames then every 15 frames are selected. 15 by default

#get only some frames select_some_frames or all the frames get_all_frames
getter_v2f.select_some_frames() # select every 15 frames
getter_v2f.get_all_frames()
