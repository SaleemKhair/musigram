from mido import MidiFile, Message
import logging
from .model import Clock
from . import Serializer
from typing import Dict

LOG = logging.getLogger(__name__)
class ClockSerializer(Serializer):
    """
    A Serializer that parses MIDI messages to Clock instances.
    """
    def __init__(self) -> None:
        self.__chords: Dict[int,Clock] = dict()

    def serialize_message(self, idx: int, message: Message):
        if self.__chords.get(message.channel) is None:
            self.__chords[message.channel] =  Clock(
                channel=message.channel,
                idx=idx)
        
        clock: Clock = self.__chords.get(message.channel)
        if message.type == 'note_off':
            clock.remove(message.note)
        if message.type == 'note_on':
            clock.append(message.note)
        LOG.debug(repr(clock))
        return clock

    def play(self, file_path):
        with open(file=file_path, mode='rb') as midi_file:
            midi = MidiFile(file=midi_file)
            return midi.play(False)
