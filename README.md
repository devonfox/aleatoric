## HW4: Aleatoric

CS410P - Music, Sound, and Computers

*Devon Fox 2022*

### Linux Build Instructions

Make sure the latest version of Python is installed.

1. First upgrade pip and setuptools:

`pip install --upgrade pip setuptools`

2. Then make sure the ALSA development dependencies are installed:

`sudo apt-get install -y python3-dev libasound2-dev`

3. Install Numpy (math library)

`pip install numpy`

4. Install Sounddevice (audio Library)

`pip install sounddevice`

To run the program, in the same directory, type the following in the terminal:

`python3 aleatoric.py`

You can customize many aspects of the resulting audio (or dare I say music) with the following commands:

*Without entering arguments, the defaults will be used Give command `-h` to access help menu*

Ex. `--root 60` 
* allows us to select the root note of the major scale we will generate (Default: 48)

Ex. `--beats 4`
* alters the time signature, and counts how many beats including the root note we will generate per bar (Default: 8)

Ex. `--bpm 240`
* set the tempo or 'beats per minute' (Default: 90)

Ex. `--ramp 0.5`
* the fraction of both attack and release of each generated sound (Default: 0.5)

Ex. `--accent 4`
* note volume for the first (accent) beat of each measure (Default: 5.0)

Ex. `--volume 6`
* note volume for the first (accent) beat of each measure (Default: 8.0)
