import os
import cv2
import shutil


class get_frames_from_video():

	def __init__(self):

		self.vidcap = None
		self.video_file_path = None
		self.temp_frames_folder = None
		self.n_frames = 15

	def set_video_file_path(self, video_file_path):
		self.video_file_path = video_file_path
		print ("set self.video_file_path to %s"  %self.video_file_path)
	
	def set_n_frames(self, n_frames):
		self.n_frames = n_frames
		print ("set self.n_frames to %s"  %self.n_frames)

	def video_2_frame(self, frames_folder):
		# This function gets all the frames from the video 
		# specified at  self.video_file_path
		# the frames are saved at the folder path frames_folder
		# returns the number of frames
		
			if not os.path.exists(frames_folder):
				os.makedirs(frames_folder)

			self.vidcap = cv2.VideoCapture(self.video_file_path)
			success,image = self.vidcap.read()
			count = 0
			success = True
			while success:
				name_frame = "frame_" + str(count) + ".jpg"
				frame_file_path = os.path.join(frames_folder, name_frame)
				cv2.imwrite(frame_file_path, image)     # save frame as JPEG file
				success,image = self.vidcap.read()
				print ('Read a new frame: ', count)
				count += 1
			return count

	def select_some_frames(self):
		# relative paths
		
		# generate the frames from video and save it in self.temp_frames_folder
		temp_dir = os.path.dirname(os.path.realpath("__file__"))
		self.temp_frames_folder = os.path.join(temp_dir, "temp_frames")
		#print ("temp_frames_folder ", self.temp_frames_folder)
		if not os.path.exists(self.temp_frames_folder):
				os.makedirs(self.temp_frames_folder)
		count_frames = self.video_2_frame(self.temp_frames_folder)
		#print (count_frames)


		# chose some frames every n_frames frames from self.temp_frames_folder
		# and save its paths in an array
		cont_images_choosed = 0
		path_choosed_images = []
		for i in range(0, count_frames):
			if i%self.n_frames == 0:
				filename = "frame_" +  str(i) + ".jpg"
				file_path = os.path.join(self.temp_frames_folder, filename)
				path_choosed_images.append(file_path)
				cont_images_choosed +=1
		print ("Total number of choosed frames selected: %s" %cont_images_choosed)

		# iterate over the array that has the paths of every frame in the tem folder
		# and copy that in the  selected_frames_folder
		root_dir = os.path.dirname(os.path.realpath(self.video_file_path))
		#print ("root_dir", root_dir)
		selected_frames_folder = os.path.join(root_dir, "selected_frames")
		#print ("selected_frames_folder", selected_frames_folder)
		if not os.path.exists(selected_frames_folder):
				os.makedirs(selected_frames_folder)
		for path in path_choosed_images:
			shutil.copy2(path, selected_frames_folder) # target filename is /dst/dir/file.ext

		# delete the temporal folder where all the frames are located
		shutil.rmtree(self.temp_frames_folder)
	
	def get_all_frames(self):

		# create the folder that will keep all the frames from the video 
		root_dir = os.path.dirname(os.path.realpath(self.video_file_path))
		all_frames_folder = os.path.join(root_dir, "all_frames")
		if not os.path.exists(all_frames_folder):
				os.makedirs(all_frames_folder)
		count_frames = self.video_2_frame(all_frames_folder)
		print ("Total number of frames generated: %s" %count_frames)

		
