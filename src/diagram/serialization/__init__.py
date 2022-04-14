from mido import MidiFile
import logging
from ..model import Clock
from diagram import Serializer
import threading

LOG = logging.getLogger(__name__)
class ClockSerializer(Serializer):
    """
    A Serializer that parses MIDI messages to Clock instances.

    ...

    Attributes
    ----------
    __chord: threading.local
        .clock: Clock
            A stateful thread-safe instance of Clock that is cached during the stream to keep track if multiple notes
            are played simultaneously.
    """
    def __init__(self) -> None:
        self.__chord = threading.local()
        self.__chord.clock = None

    def serialize_message(self, idx: int, message):
        if self.__chord.clock is None: # create and cache a new instance
            self.__chord.clock = Clock(
                channel=message.channel,
                idx=idx)
        else:
            if message.type == 'note_off': # remove note from cached instance and return state
                self.__chord.clock.remove(message.note)
            if message.type == 'note_on': # add note to cached instance and return state
                self.__chord.clock.append(message.note)
        LOG.debug(repr(self.__chord.clock))
        return self.__chord.clock

    def play(self, file_path):
        with open(file=file_path, mode='rb') as midi_file:
            midi = MidiFile(file=midi_file)
            return midi.play(False)
