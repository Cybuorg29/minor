# play a C-major chord using the scikit-learn MIDI library
from sklearn.datasets import load_sample_file
from sklearn.feature_extraction.io import MidiDispatcher

# use MidiDispatcher to create a new sequence
dispatcher = MidiDispatcher()
notes = [60, 64, 67]  # C-major notes
velocities = [127, 127, 127]  # maximum amplitude
dispatcher.add_chords([(0, notes, velocities)])

# play the sequence
player = MidiPlayer(dispatcher.io)
player.play()