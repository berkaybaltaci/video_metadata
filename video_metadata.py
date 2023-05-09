import os
import json
import cv2

# get the video directory from the user
video_dir = input("Enter the directory containing the video files: ")

# empty list to store video metadata
video_metadata = []

# loop through all video files in the directory
for filename in os.listdir(video_dir):
    if filename.endswith('.mp4') or filename.endswith('.mov'):
        video_path = os.path.join(video_dir, filename)
        # read video file using OpenCV
        cap = cv2.VideoCapture(video_path)
        # get video duration in seconds
        duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
        # add video metadata to the list
        video_metadata.append({'name': filename, 'duration': duration})
        # release the video capture object
        cap.release()

# write video metadata to a JSON file
with open('video_metadata.json', 'w') as outfile:
    json.dump(video_metadata, outfile)