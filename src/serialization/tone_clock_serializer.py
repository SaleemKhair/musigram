from mido import MidiFile
import logging
from model.tone_clock import ToneClock
import threading

LOG = logging.getLogger(__package__)

class ToneClockSerializer:
    def __init__(self) -> None:
        self.__chord = threading.local()
        self.__chord.clock = None

    def serialize_message(self, idx, message):
        if self.__chord.clock is None:
            self.__chord.clock = ToneClock(
                channel=message.channel,
                idx=idx)
        else:
            if message.type == 'note_off':
                self.__chord.clock.delete_note(message.note)
            if message.type == 'note_on':
                self.__chord.clock.add_note(message.note)
        LOG.debug(vars(self.__chord.clock))
        yield self.__chord.clock

    def play(self, file_path):
        with open(file=file_path, mode='rb') as midi_file:
            midi = MidiFile(file=midi_file)
            return midi.play(False)
