# -*- coding: utf-8 -*-
import wave
import pyaudio

from transform import Transformer
from plugins import pitch


RATE = 44100
CHANNELS = 1
CHUNK = 1024*8
# WIN_SIZE = 256


def main():
    # while True:
    #     input_audio = sys.stdin.read(1024)

    pa = pyaudio.PyAudio()

    kwargs = dict(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=RATE,
        frames_per_buffer=CHUNK,
    )

    inp = pa.open(input=True, **kwargs)
    out = pa.open(output=True, **kwargs)
    wf = wave.open('sample.wav', 'w')
    wf.setnchannels(CHANNELS)
    transformer = Transformer(pitch.pitch_down)

    try:
        inp.start_stream()
        out.start_stream()
        while True:
            data = inp.read(CHUNK)
            transformed = transformer.transform(data)
            out.write(transformed)
            #out.write(data)

    finally:
        inp.stop_stream()
        out.stop_stream()
        inp.close()
        out.close()

if __name__ == '__main__':
    main()
