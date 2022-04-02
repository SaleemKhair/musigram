from serialization.tone_clock_serializer import ToneClockSerializer


class PortController:
    def __init__(self, serializer: ToneClockSerializer):
        self._serializer = serializer

    def get_clocks(self, in_port):
        for idx, message in enumerate(in_port):
            yield (message, self._serializer.serialize_message(idx, message))
