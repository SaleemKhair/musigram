from __future__ import annotations
from typing import Dict, List, Sequence
import logging, copy


LOG = logging.getLogger(__package__)

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

    def invert(self) -> Clock:
        pass

    def transpose(self, by: int) -> Clock:
        transposed: Clock = copy.deepcopy(self)
        for i, hr in enumerate(transposed.__hours):
            transposed.__hours[i] = map_note_to_hour(hr + by)
            transposed.__keys[i] = map_hour_to_key(hr)
        return transposed

    def rotate(self, by: int) -> Clock:
        pass
    
    def retrograde(self, by: int) -> Clock:
        pass

    def is_transpositionally_relative(self, other: Clock) -> bool:
        pass
    
    def is_inversionally_relateive(self, othet: Clock) -> bool:
        pass

    def is_equals(self, other: Clock) -> bool:
        return self._is_reflective(other) and self._is_symmetical(other) and self._is_transitive(other)

    def _is_reflective(self, other: Clock) -> bool:
        pass

    def _is_symmetical(self, other: Clock) -> bool:
        pass

    def _is_transitive(self, other: Clock) -> bool:
        pass

    def __repr__(self) -> str:
        return f'Clock( set: {self.__hours}, keys: {self.__keys} )'
