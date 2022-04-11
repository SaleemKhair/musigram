from diagram.serialization import ClockSerializer
from mido import MidiFile
import unittest

class TestToneClockSerializer(unittest.TestCase):
    def test_serialize(self):
        for track in MidiFile('./data/Nothing Else Matters - Metallica.mid').tracks:            
            assert len([ClockSerializer().serialize_message(i, msg) for i, msg in enumerate(track)]) == len(track)
