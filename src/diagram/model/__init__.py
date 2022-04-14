from __future__ import annotations
from typing import Dict, List, Sequence
import logging, copy


LOG = logging.getLogger(__name__)

NOTE_KEYS: Dict[int, str] = {
    4: 'E',
    5: 'F',
    6: 'F#',
    7: 'G',
    8: 'G#',
    9: 'A',
    10: 'A#',
    11: 'B',
    0: 'C',
    1: 'C#',
    2: 'D',
    3: 'D#'

}


def map_note_to_hour(note: int) -> int:
    return note % 12


def map_hour_to_key(hour: int) -> str:
    return NOTE_KEYS[hour]


class Clock:
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
        self.__hours: List[int] = list()
        self.__keys: List[str] = list()
        self.channel: int = channel
        self.idx: int = idx

    def append(self, note) -> None:
        hour = map_note_to_hour(note)
        if hour not in self.__hours:
            self.__hours.append(hour)
            self.__keys.append(map_hour_to_key(hour))
        assert len(self.__hours) < 12 and len(self.__keys) < 12 # This should never happen.

    def remove(self, note) -> None:
        hour = map_note_to_hour(note)
        key = map_hour_to_key(hour)
        if hour in self.__hours: self.__hours.remove(hour)
        if key in self.__keys:self.__keys.remove(key)

    def get_set(self) -> Sequence:
        return self.__hours

    def invert(self, n: int) -> Clock:
        """
        the inverse operation is sometimes designated as T(n)I,
        where I means "invert" and T(n) means "transpose by some interval n" measured in number of semitones.
        Thus, inversion is a combination of an inversion followed by a transposition.
        """
        inverted: Clock = copy.deepcopy(self)
        for i, hr in enumerate(inverted.__hours):
            invert = map_note_to_hour((12 - hr) + n)
            inverted.__hours[i] = invert
            inverted.__keys[i] = map_hour_to_key(invert)
        return inverted

    def transpose(self, by: int) -> Clock:
        transposed: Clock = copy.deepcopy(self)
        for i, hr in enumerate(transposed.__hours):
            transpose = map_note_to_hour(hr + by)
            transposed.__hours[i] = transpose
            transposed.__keys[i] = map_hour_to_key(transpose)
        return transposed

    def is_transpositionally_relative(self, other: Clock) -> bool:
        for i in range(12):
            if other.transpose(i).get_set() == self.get_set():
              return True  
        return False
    
    def is_inversionally_relateive(self, other: Clock) -> bool:
        for i in range(12):
            if other.invert(i).get_set() == self.get_set():
              return True  
        return False

    def _is_symmetical(self, other: Clock) -> bool:
        pass

    def __repr__(self) -> str:
        return f'Clock( intervals: {self.__hours}, keys: {self.__keys}, channel: {self.channel})'
