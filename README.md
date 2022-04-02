**Tone Clock Diagram**
===
 Translate MIDI (signals/files) to Musical Tone-Clocks based on the Tone-Clock Throry.
![tone-clock main](https://github.com/SaleemKhair/tone-clock/actions/workflows/main.yml/badge.svg)
## Description
---
The Tone Clock, and its related compositional theory Tone-Clock Theory, is a post-tonal music composition technique, developed by composers Peter Schat and Jenny McLeod.

Music written using tone-clock theory features a high economy of musical intervals within a generally chromatic musical language

[Read more...](https://en.wikipedia.org/wiki/Tone_Clock)

## Development Environment
---
Depends On:
- [tox](https://tox.wiki/en/latest/index.html)
- [make](https://www.gnu.org/software/make/)
- [libjack0](https://packages.debian.org/sid/libjack0)
- [libjack-dev](https://packages.debian.org/sid/libjack-dev)
- [libasound2-dev](https://packages.debian.org/sid/libasound2-dev)

Supports Platform: Linux | Debian
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
## Testing
---
This project uses `tox` and `pytest` to run tests, to execute tests run the and the test commands are managed by `Make` following:
```
$ make test clean
```
