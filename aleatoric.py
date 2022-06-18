# Devon Fox - HW#4 Aleatoric - CS410P Music, Computers, and Sound
# May 2022

import argparse
import random
import numpy as np
import sounddevice as sd
import math

sd.default.samplerate = 48000
sd.default.channels = 1
sd.default.blocksize = 1024

ii16 = np.iinfo(np.int16)  # global max/min int16 values

parser = argparse.ArgumentParser()

parser.add_argument('--root', dest='keynumber', type=int, default=48,
                    help='root tone of scale (default: 48)')
parser.add_argument('--beats', dest='sig', type=int, default=8,
                    help='time signature of beats per measure, (default: 8)')
parser.add_argument('--bpm', dest='bpm', type=float, default=90.0,
                    help='beats per minute (default: 90.0)')
parser.add_argument('--ramp', dest='frac', type=float, default=0.5,
                    help='frac of beat time for att/rel (default: 0.5)')
parser.add_argument('--accent', dest='accent', type=float, default=5.0,
                    help='note volume for the first (accent) beat of each measure (default: 5.0)')
parser.add_argument('--volume', dest='volume', type=float, default=8.0,
                    help='note volume for the unaccented beats of each measure (default: 8.0)')

arg = parser.parse_args()


def getAmp(vol):
    exp = ((-6 * (10 - vol)) / 20)
    amp = math.pow(10, exp)
    return amp


def dFromBPM(bpm):
    d = bpm / 60
    return d


def outputSquare(arg):
    samplerate = 48000
    frequency = 440 * 2**((arg.keynumber - 69) / 12)
    duration = 1 / dFromBPM(arg.bpm)
    samples = samplerate * duration
    t = np.linspace(0, duration, int(samples), False)
    wave = 4 * np.floor(frequency * t) - 2 * np.floor(2*frequency * t) + 1
    amp = getAmp(arg.accent)
    wave *= ii16.max * amp / max(abs(wave))  # normalizing
    frac = arg.frac
    length = len(wave)
    ramp = length * frac

    for i in range(len(wave)):
        if i <= ramp:
            wave[i] *= (i / ramp)
        if i > length - ramp:
            wave[i] *= ((length - i) / ramp)

    wave = wave.astype(np.int16)      # setting back to int16
    return wave


def outputSine(arg, k):
    samplerate = 48000
    frequency = 440 * 2**((k - 69) / 12)
    duration = 1 / dFromBPM(arg.bpm)

    samples = samplerate * duration
    t = np.linspace(0, duration, int(samples), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    amp = getAmp(arg.volume)
    wave *= ii16.max * amp / max(abs(wave))  # normalizing
    frac = arg.frac
    length = len(wave)
    ramp = length * frac

    for i in range(len(wave)):
        if i < ramp:
            wave[i] *= (i / ramp)
        if i > length - ramp:
            wave[i] *= ((length - i) / ramp)

    wave = wave.astype(np.int16)
    return wave


def prepareNotes(arg, scale):
    notes = []
    root = outputSquare(arg)
    notes.append(root)
    k = arg.keynumber
    for i in range(len(scale)):
        k += scale[i]
        note = outputSine(arg, k)
        notes.append(note)
    return notes


def run(notes, arg):
    try:
        while True:
            stream.write(notes[0])
            for i in range(arg.sig - 1):
                stream.write(notes[random.randrange(1, arg.sig)])
    except KeyboardInterrupt:
        pass


major = [2, 2, 1, 2, 2, 2, 1]

stream = sd.OutputStream(dtype=np.int16)
stream.start()

notes = prepareNotes(arg, major)
run(notes, arg)
