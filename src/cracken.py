# -*- coding: utf-8 -*-
import alsaaudio

from transform import Transformer
from plugins import pitch

RATE = 44100
CHANNELS = 1
CHUNK = 1024



def main():
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
    inp.setchannels(CHANNELS)
    inp.setrate(RATE)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(CHUNK)

    out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
    out.setchannels(CHANNELS)
    out.setrate(RATE)
    out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    out.setperiodsize(CHUNK + 1000)
    transformer = Transformer(pitch.pitch_up)

    while True:
        l, data = inp.read()
        if data:
            transformed = transformer.transform(data)
            out.write(transformed)

if __name__ == '__main__':
    main()
