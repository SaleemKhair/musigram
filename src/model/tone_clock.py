from typing import Set
from model import *

class ToneClock:
    def __init__(self, idx: int, channel: int):
        self.__hours: Set[int] = set()
        self.__keys: Set[str] = set()
        self.channel: int = channel
        self.idx: int = idx

    def add_note(self, note) -> None:
        hour = map_note_to_hour(note)
        self.__hours.add(hour)
        self.__keys.add(map_hour_to_key(hour))
        assert len(self.__hours) < 12 and len(self.__keys) < 12

    def delete_note(self, note) -> None:
        hour = map_note_to_hour(note)
        key = map_hour_to_key(hour)
        if hour in self.__hours: self.__hours.remove(hour)
        if key in self.__keys:self.__keys.remove(key)
