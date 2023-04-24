import cv2
import pyaudio
import wave
import pyautogui
import numpy as np

# Set up the screen capture
screen_size  = tuple(pyautogui.size())# set the screen size to capture
fourcc = cv2.VideoWriter_fourcc(*"XVID") # set the video codec
video_out = cv2.VideoWriter("screen_capture.avi", fourcc, 20.0, screen_size) # set the video output file and frame rate

# Set up the audio capture
audio = pyaudio.PyAudio() # create a PyAudio object
sample_format = pyaudio.paInt16 # 16-bit resolution
channels = 2 # stereo
fs = 44100 # sample rate
frames_per_buffer = 1024 # number of frames per buffer
stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=frames_per_buffer,
                    input=True,
                    output=True) # open the audio stream

# Record the audio and screen
while True:
    # Capture the screen
    img = pyautogui.screenshot() # take a screenshot
    frame = np.array(img) # convert the image to a numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert the color format from BGR to RGB
    video_out.write(frame) # write the frame to the video output file

    # Record the audio
    data = stream.read(frames_per_buffer) # read audio data from the stream
    video_out.write(data) # write the audio data to the output file

# Release the resources
stream.stop_stream()
stream.close()
audio.terminate()
video_out.release()
cv2.destroyAllWindows()
