# Modding the pyaudio basic recording file to be user controllable in terms
# of record time and file naming

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
WAVE_OUTPUT_FILENAME = raw_input("What would you like to call your recording? > ")
if '.wav' not in WAVE_OUTPUT_FILENAME:
    WAVE_OUTPUT_FILENAME += '.wav'
RECORD_SECONDS = int(raw_input("How many seconds would you like to record > "))



p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print"* recording " + WAVE_OUTPUT_FILENAME

frames = []
range_size = int(RATE / CHUNK * RECORD_SECONDS)
for i in range(0, range_size):
    data = stream.read(CHUNK)
    frames.append(data)

print "* done recording " + WAVE_OUTPUT_FILENAME

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(/recordings/WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
