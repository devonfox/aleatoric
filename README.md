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
### What Went Down

I originally expected to do this assignment in Rust, and I still may in my own time rewrite this program in Rust.  That being said I really didn't have the time to spare for any roadblocks in the way, so I opted to write this homework in Python.  I originally was going to use `simpleaudio` library, however, I opted to use `sounddevice` to deal with audio, as I also want to fix my currently audio woes in my main project, and I'm in the process of rewriting with `sounddevice` instead of PyAudio.  I wanted to get some experience with sounddevice before implementing in my main project, and that was one of the key takeaways here, along with implementing a cool command line parser.  Not sure why I didn't use libraries for that in the past, as I always ended up writing those myself, and it truly can be a pain when the one thing you want to focus on is writing the actual functional code.  

The program works as intended, and I learned quite a lot in the process, and was interesting as well to create something that makes more than an audible beep, and I will be fun to perhaps flesh this out a bit more, with some additional features down the line as I further my own music/DSP learning outside of this class and afterward.
###  How It Went

Overall, it went rather painlessly, and I was able to get this up and running in a day or so.  That being said, it may have gone that smooth in Rust as well, however, I didn't want to risk it, and there was far more resources available in terms of online reading and also classmate help if I went the Python route. Again, I may still rewrite this in Rust as I feel the functionality could prove useful to go along with my Generative Midi Musicbox Term Project that I did for the CS410P Programming in Rust class that I took last term.  The term project actually in hindsight is something I could've made in this class, but overall I'm excited to be working on a sytnh this term, although it been proving to be quite difficult for me.  Anyways, that aside, I truly found this simple aleatoric program to be quite fun and rewarding to create.  