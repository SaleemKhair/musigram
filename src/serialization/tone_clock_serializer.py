from mido import MidiFile
import logging
from model.tone_clock import ToneClock
import threading

LOG = logging.getLogger(__package__)

# TODO Refactor: Naming, Design
## The class has to be coupled with an i/o port to force creating a new insrance for each port stream to achive thread-safty.
## Mapper/Reducer might be a better name since it deals with a single message
class ToneClockSerializer:
    """
    A Serializer that parses MIDI messages to ToneClock instances.

    ...

    Attributes
    ----------
    __chord: threading.local
        .clock: ToneClock
            A stateful thread-safe instance of ToneClock that is cached during the stream to keep track if multiple notes
            are played simultaneously.
    """
    def __init__(self) -> None:
        self.__chord = threading.local()
        self.__chord.clock = None

    def serialize_message(self, idx, message):
        if self.__chord.clock is None: # create and cache a new instance
            self.__chord.clock = ToneClock(
                channel=message.channel,
                idx=idx)
        else:
            if message.type == 'note_off': # remove note from cached instance and return state
                self.__chord.clock.delete_note(message.note)
            if message.type == 'note_on': # add note to cached instance and return state
                self.__chord.clock.add_note(message.note)
        LOG.debug(vars(self.__chord.clock))
        yield self.__chord.clock

    def play(self, file_path):
        with open(file=file_path, mode='rb') as midi_file:
            midi = MidiFile(file=midi_file)
            return midi.play(False)
