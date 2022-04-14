from musigram.serialization import ClockSerializer
from mido import MidiFile, MetaMessage
import unittest

class TestClockSerializer(unittest.TestCase):
    def test_serialize(self):
        midi_file = MidiFile('./data/Nothing Else Matters - Metallica.mid')
        for track in midi_file.tracks:   
            if len(track) > 22:
                assert len([ClockSerializer().serialize_message(i, msg) for i, msg in enumerate(track) if not isinstance(msg, MetaMessage)]) == len(track) - 3 # number of ignored MetaMessages
