from serialization.tone_clock_serializer import ToneClockSerializer
from mido import MidiFile
import unittest

class TestToneClockSerializer(unittest.TestCase):
    def test_serialize(self):
        for track in MidiFile('./data/Nothing Else Matters - Metallica.mid').tracks:            
            print(track.name)
