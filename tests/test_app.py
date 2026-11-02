# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("game", Path(__file__).resolve().parents[1] / "snake-game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)

class Tests(TestCase):
    def test_ladders_and_snakes(self):
        self.assertEqual(game.advance(1, 1), 37)
        self.assertEqual(game.advance(24, 1), 7)
        self.assertEqual(game.advance(99, 3), 76)
    def test_validation(self):
        with self.assertRaises(ValueError):
            game.advance(0, 3)
    def test_gui(self):
        window = game.Game()
        try:
            with patch.object(game.secrets, "randbelow", return_value=0):
                window.roll()
            self.assertEqual(window.position, 37)
            window.reset()
            self.assertEqual(window.position, 1)
        finally:
            window.destroy()
