# tabs2music
Converts a text file with guitar tabs in ascii format to a mp3 file

## Prerequisites
1. Clone the repository
2. Install fluidsynth and add it to your path: https://github.com/FluidSynth/fluidsynth/wiki/Download
3. Install the needed libraries using the command: `pip install -r requirements.txt`
4. 


Include this link in the description of understanding how the midi to note translation is done: https://computermusicresource.com/midikeys.html

Explain how the time signature is not enforced anywhere, and that its up to the user for the itme signature to be consistent across a bar

Add a list of the features

Upcoming features to be added:
1. Enforce more things with the tab's construction
    - a given bar is in the same time signature for all strings (equal length of notes)
2. More note timing flexibility (triplets)
3. Need to add soundfont to support hammer ons (h), pull offs (p), sliding up (/) and down (\), bending up (b) and down (r), and vibrato (v)
4. Capo
5. When on the website, make tabs also downloadable


Pretty good competitor: https://tab-maker.com/en/app


My soundfont might be weird as I need +12 and not +24 (I thought I needed +24 using the table I found.) Might need people to configure their soundfont's middle C (C4) value
Link to soundfont: https://drive.google.com/drive/folders/1rUSSwPpzpxl2Tg8Jn3kWqOimlxZZPAjN?usp=sharing