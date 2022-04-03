**Tone Clock Diagram**
=== 
<p align="right">
<a><img alt="Main Branch" src="https://github.com/SaleemKhair/tone-clock/actions/workflows/main.yml/badge.svg"></a>
</p>

## Description
---
The Tone Clock, and its related compositional theory Tone-Clock Theory, is a post-tonal music composition technique, developed by composers Peter Schat and Jenny McLeod.

Music written using tone-clock theory features a high economy of musical intervals within a generally chromatic musical language

Read more:
- [Tone-Clock](https://en.wikipedia.org/wiki/Tone_Clock)
- [Set-Theory (music)](https://en.m.wikipedia.org/wiki/Set_theory_(music))
## Development Environment
---
Depends On:
- [tox](https://tox.wiki/en/latest/index.html)
- [make](https://www.gnu.org/software/make/)
- [libjack0](https://packages.debian.org/sid/libjack0)
- [libjack-dev](https://packages.debian.org/sid/libjack-dev)
- [libasound2-dev](https://packages.debian.org/sid/libasound2-dev)

Supports Platform: Linux | Debian
<br>

## Preperation
---
### Install `tox`

Using pip
```bash
$ python3 -m pip install -U tox
```
### Install Platform Dependencies 
`make`, `libjack0`, `libjack-dev`

On Ubuntu
```
$ sudo apt-get install -y make libjack0 libjack-dev libasound2-dev
```
 <br>

## Running
---
To start listening on MIDI device port
### using Makefile
```bash
$ make run
```

### in Visual Studio Code

if you are using vscode theres a `.vscode` file included in the project path.

>To specify input/output port names change the `MIDI_PORT_NAME` variable in the `server` module file `src/server/__main__py`

>To get a list of input/output names use
```bash
## to get input names
$ python3 -c 'import mido; exit(mido.get_input_names())'
## to get output names
$ python3 -c 'import mido; exit(mido.get_output_names())'
```
<br>

## Testing
---
This project uses `tox` and `pytest` to run tests, the test commands are managed by `Make` following:
```
$ make test clean
```
<br>

## Troubleshooting
---
### Integrate PulseAudio with JACK
If youre using PulseAudio or its the default driver for some of your applications (ex Firefox)
JACK might not be able to add or manage its i/o(s), [See](https://jfearn.fedorapeople.org/fdocs/en-US/Fedora_Draft_Documentation/0.1/html/Musicians_Guide/sect-Musicians_Guide-Integrating_PulseAudio_with_JACK.html), to be able to use JACK as the main driver.