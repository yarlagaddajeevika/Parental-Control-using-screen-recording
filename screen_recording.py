import cv2
import numpy as np
import pyaudio
import wave
import threading
import keyboard
from PIL import ImageGrab
import moviepy.editor as mp
import os

#Record both audio and video
def record_screen_and_audio(output_filename):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (1920, 1080))

    # Define audio parameters
    audio_format = pyaudio.paInt16
    channels = 2
    sample_rate = 44100
    chunk = 1024

    # Initialize pyaudio
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=audio_format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    # Create a flag to indicate recording
    is_recording = True

    # Define function for recording audio
    def record_audio():
        nonlocal is_recording
        frames = []
        while is_recording:
            data = stream.read(chunk)
            frames.append(data)
        # Stop and close the audio stream
        stream.stop_stream()
        stream.close()
        audio.terminate()
        # Save the audio to a file
        wf = wave.open("audio.wav", 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    # Start recording audio in a separate thread
    audio_thread = threading.Thread(target=record_audio)
    audio_thread.start()

    # Start recording video
    while True:
        if keyboard.is_pressed('f9'): # Stop recording when F9 is pressed
            break
        # Capture screen and write to output video file
        img = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert color space from BGR to RGB
        out.write(img)

    # Release the capture and writer
    out.release()

    # Set the flag to stop the audio recording
    is_recording = False

    # Wait for the audio thread to finish
    audio_thread.join()

    # Combine the audio and video files into a single MP4 file
    video = mp.VideoFileClip("output.mp4") 
    audio = mp.AudioFileClip("audio.wav")
    final_output = video.set_audio(audio)
    final_output.write_videofile(output_filename)

