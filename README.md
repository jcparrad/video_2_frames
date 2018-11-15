# video_2_frames

The aim of this project is to get frames from a video and savet it. 
The frames to be saved can be all the frames from the video or can be every n_frames (by default it is every 15 frames)

## Running
Edit the file video_2_frames_main.py in the folder source as follows.

1. Set the path to the video you want to get the frames from. For example:

video_file_path = "/home/get_frames_from_video/data/video/DJI_3560.MP4"
getter_v2f.set_video_file_path(video_file_path)

2. If you want to get frames every n_frames, then set it as follows:

getter_v2f.set_n_frames(15) # if select_some_frames then every 15 frames are selected. 15 by default
getter_v2f.select_some_frames() # select every 15 frames

3.If you want to get all the frames fro the video then execute it as follows:
getter_v2f.get_all_frames()


