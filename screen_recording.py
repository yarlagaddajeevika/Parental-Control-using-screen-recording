import cv2
import numpy as np
import pyautogui
import sounddevice as sd
from scipy.io.wavfile import write

# Set screen resolution and framerate
screen_size = (1920, 1080)
fps = 30.0
duration = 10.0

# Set audio parameters
sample_rate = 44100
channels = 2

# Start recording audio and video
print("Recording audio and video...")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, screen_size)
recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels)

# Loop over the frames and write to output video
for i in range(int(fps * duration)):
    # Capture screen image and convert to numpy array
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write frame to output video
    out.write(frame)

    # Record audio
    audio = sd.wait()

# Save audio as WAV file
write("audio.wav", sample_rate, recording)

# Release video writer and close window
out.release()
cv2.destroyAllWindows()

print("Screen and audio recording finished.")
