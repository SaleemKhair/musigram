from . import Serializer, Processor
import logging

LOG = logging.getLogger(__name__)
class ClockProcessor(Processor):
    def __init__(self, serializer: Serializer):
        self._serializer = serializer

    def process(self, in_port):
        LOG.debug(f'Started processing for input port {in_port}')
        for idx, message in enumerate(in_port):
            yield (message, self._serializer.serialize_message(idx, message))
