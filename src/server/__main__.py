from controller.port_controller import PortController
from serialization.tone_clock_serializer import ToneClockSerializer
from mido import open_input, open_output
import subprocess
import logging
import logging.config

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger('server')
MIDI_PORT_NAME='Virtual Raw MIDI 1-0:VirMIDI 1-0 20:0'

def module_loaded(module_name):
    """Checks if module is loaded"""
    lsmod_proc = subprocess.Popen(['lsmod'], stdout=subprocess.PIPE)
    grep_proc = subprocess.Popen(
        ['grep', module_name], stdin=lsmod_proc.stdout)
    grep_proc.communicate()  # Block until finished
    return grep_proc.returncode == 0


for module_name in ['snd_virmidi']:
    loaded = module_loaded(module_name)
    if not loaded:
        LOG.warning('snd_virmidi kernel module is not loaded')


try:
    in_port = open_input(MIDI_PORT_NAME)
    out_port = open_output(MIDI_PORT_NAME)
    serializer = ToneClockSerializer()
    for (message, clock) in PortController(serializer).get_clocks(in_port):
        LOG.debug(vars(*clock))
        out_port.send(message)
except KeyboardInterrupt as ex:
    LOG.error('User Terminate Signal Received.')
finally:
    in_port.close()
    out_port.close()
