
**MusiGram**
=== 

[**Tone Clock**](https://en.wikipedia.org/wiki/Tone_Clock) and [**Pitch-Class Set**](https://en.m.wikipedia.org/wiki/Set_theory_(music)) Diagram Genetation and Analysis 

![](https://github.com/SaleemKhair/tone-clock/actions/workflows/main.yml/badge.svg)


#### **Library to translate MIDI signals into __pitch-class sets__ or __tone-clock sets__, and provide basic post-tonal analysis operations.**
----

### Background
---

The **Tone Clock**, and its related compositional [tone-clock](https://en.wikipedia.org/wiki/Tone_Clock) theory, is a post-tonal music composition technique, developed by composers Peter Schat and Jenny McLeod.

>Music written using **Tone Clock** theory features a high economy of musical intervals within a generally chromatic musical language.

The [pitch-class set](https://en.m.wikipedia.org/wiki/Set_theory_(music)) theory provides concepts for categorizing musical objects and describing their relationships. Howard Hanson first elaborated many of the concepts for analyzing tonal music

Other resources: [@Sideways on
Youtube](https://www.youtube.com/watch?v=oGeBem72R3Y)

---

### Development Environment
---
#### **Depends On:**
- [libjack0](https://packages.debian.org/sid/libjack0)
- [libjack-dev](https://packages.debian.org/sid/libjack-dev)
- [libasound2-dev](https://packages.debian.org/sid/libasound2-dev)

**Supports Platform:** Linux | Debian

---
### Preperation
---

#### 1. Install Platform Dependencies 
`libjack0`, `libjack-dev`, `libasound2-dev`

>On Ubuntu
```
$ sudo apt-get install -y libjack0 libjack-dev libasound2-dev
```

#### 2. Install `tox`

>Using pip
```bash
$ python3 -m pip install -U tox
```

#### 3. Setup project
>setup python virtual environment
```bash
~$ git clone https://github.com/SaleemKhair/musigram
~$ cd musigram
## create virtual environment under .venv
~$ python3 -m venv .venv
## activate
source .venv/bin/activate
```
>install dependencies
```bash
(.venv)~$ pip install -r requirements.txt
```
---
### Scripts
---

* [proc_clock_vermidi](bin/proc_clock_vermidi):
Subscribes to a MIDI and serializes each midi signal to a clock in real-time.

---
### Testing
---
>This project uses `tox` and `pytest` to run tests.
```
$ tox -e py38
```
---
### Troubleshooting
---
#### MIDI Ports
>To get a list of input/output names use
```bash
## to get input names
$ python3 -c 'import mido; exit(mido.get_input_names())'
## to get output names
$ python3 -c 'import mido; exit(mido.get_output_names())'
```

#### Integrate PulseAudio with JACK
>If youre using PulseAudio or its the default driver for some of your applications (ex Firefox)
JACK might not be able to add or manage its i/o(s), [See](https://jfearn.fedorapeople.org/fdocs/en-US/Fedora_Draft_Documentation/0.1/html/Musicians_Guide/sect-Musicians_Guide-Integrating_PulseAudio_with_JACK.html), to be able to use JACK as the main driver.