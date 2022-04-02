from typing import Dict

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
