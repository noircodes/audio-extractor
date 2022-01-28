import moviepy.editor

video = moviepy.editor.VideoFileClip("test.mp4")

# if your video is in same folder share your python file is there than you can give name direct
# else you need to give path of the video file

audio = video.audio
audio.write_audiofile("extracted.mp3")