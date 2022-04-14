from mido import MidiFile, Message
import logging
from ..model import Clock
from diagram import Serializer
from typing import Dict

LOG = logging.getLogger(__name__)
class ClockSerializer(Serializer):
    """
    A Serializer that parses MIDI messages to Clock instances.
    """
    def __init__(self) -> None:
        self.__chords: Dict[int,Clock] = dict()
        self.clock: Clock = None

    def serialize_message(self, idx: int, message: Message):
        if self.__chords.get(message.channel) is None: # create and cache a new instance
            self.clock =  Clock(
                channel=message.channel,
                idx=idx)
            self.__chords[message.channel] = self.clock
        else:
            if message.type == 'note_off': # remove note from cached instance and return state
                self.clock.remove(message.note)
            if message.type == 'note_on': # add note to cached instance and return state

                self.clock.append(message.note)
        LOG.debug(repr(self.clock))
        LOG.debug(repr(message))
        return self.clock

    def play(self, file_path):
        with open(file=file_path, mode='rb') as midi_file:
            midi = MidiFile(file=midi_file)
            return midi.play(False)
