# Snakes and Ladders

A lightweight single-player board game written in Python 3 with Tkinter.

**Developer:** Hamdy Abou El Anein
**Contact:** info@daylightlinux.ch
**License:** GNU GPL v3 (see LICENSE).

## Features

- A drawn 100-square board, with snakes and ladders highlighted.
- No EasyGUI dependency or external image assets.
- Secure random die rolls, automatic jumps and end-of-game detection.
- Unit tests for game rules and the real Tkinter interface.

## Run

    python3 snake-game.py

## Tests

    python3 -m unittest discover -s tests -v

The original Garfield-themed version is preserved on the
[old branch](https://github.com/hamdyaea/Ladder-Snake-Game-Garfield/tree/old).
The modern interface uses original vector-like drawing rather than bundled artwork.
