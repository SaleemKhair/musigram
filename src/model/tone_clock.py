from typing import Set
from model import *

class ToneClock:
    """ 
    A Data Object that hold the Clock-Set (musical set)

    ...

    Attributes
    ----------
    channel: int
        The channel of the MIDI Message.
    idx: int
        The order of which this instance was created relative to all created instances (across all tracks)
    __hours : Set[int]
        A set of numerical representation consisting of distinct integers (i.e., without duplicates)
        which is an unordered (but maintains insertion order) collection of pitch classes
    __keys: Set[str]
        A set of strings that corrispond to '__hours' 
        --e.g. __hours[0, 1, 2 ] would corrispond to __keys['C', 'C#', 'D']
    """

    def __init__(self, idx: int, channel: int):
        self.__hours: Set[int] = set()
        self.__keys: Set[str] = set()
        self.channel: int = channel
        self.idx: int = idx

    def add_note(self, note) -> None:
        hour = map_note_to_hour(note)
        self.__hours.add(hour)
        self.__keys.add(map_hour_to_key(hour))
        assert len(self.__hours) < 12 and len(self.__keys) < 12 # This should never happen.

    def delete_note(self, note) -> None:
        hour = map_note_to_hour(note)
        key = map_hour_to_key(hour)
        if hour in self.__hours: self.__hours.remove(hour)
        if key in self.__keys:self.__keys.remove(key)
