import sounddevice as sd
from scipy.io.wavfile import write
# import wavio as w

f = 40000   # sample frequency 

dur = 15     # duration (in seconds) of sample frequency

recording = sd.rec(int(dur * f), samplerate = f, channels = 2)

sd.wait()

# Now we convert numpy array into audio file:- 
#     use the write function from scipy.io.wavfile 
#     to convert the NumPy array to an audio file

write("recording1.wav", f, recording)


# write function from the wavio library (does same as above)

# w.write("recording2.wav", recording, f, sampwidth = 2)
