import pyautogui
import cv2
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav

# Set the resolution and framerate of the recording
resolution = (1920, 1080)
fps = 30

# Set the duration of the recording in seconds
duration = 600 #10min

# Start recording audio
fs = 44100
duration_samps = duration * fs
recording = sd.rec(duration_samps, samplerate=fs, channels=2)

# Start recording screen
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter("screen_recording.mp4", fourcc, fps, resolution)

for i in range(duration * fps):
    # Capture the screen and convert to numpy array
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video writer
    video_writer.write(frame)

# Stop recording audio and save the wav file
sd.wait()
wav.write("audio_recording.wav", fs, recording)

# Release the video writer and close the window
video_writer.release()
cv2.destroyAllWindows()
