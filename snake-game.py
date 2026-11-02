#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Snakes and Ladders: a lightweight, single-player Tkinter game."""
from __future__ import annotations

import secrets
import tkinter as tk

JUMPS = {2: 37, 11: 33, 25: 7, 43: 21, 55: 27,
         57: 79, 65: 87, 68: 31, 71: 93, 98: 76}


def advance(position: int, dice: int) -> int:
    if not 1 <= position <= 100 or not 1 <= dice <= 6:
        raise ValueError("Invalid position or die roll")
    if position == 100:
        return 100
    landing = position + dice
    if landing > 100:
        landing = 100 - (landing - 100)
    return JUMPS.get(landing, landing)


def square_center(square: int, cell: int) -> tuple[int, int]:
    if not 1 <= square <= 100:
        raise ValueError("Invalid square")
    row = (square - 1) // 10
    col = (square - 1) % 10
    if row % 2:
        col = 9 - col
    return col * cell + cell // 2, (9 - row) * cell + cell // 2


class Game(tk.Tk):
    CELL = 45

    def __init__(self) -> None:
        super().__init__()
        self.title("Snakes and Ladders — Hamdy Abou El Anein")
        self.configure(bg="#101827")
        self.position = 1
        self.turns = 0
        self.message = tk.StringVar(value="Roll the die to start.")
        panel = tk.Frame(self, bg="#101827", padx=18, pady=16)
        panel.pack(fill="both", expand=True)
        tk.Label(panel, text="SNAKES & LADDERS", font=("DejaVu Sans", 15, "bold"),
                 bg="#101827", fg="#8bd6c1").pack(pady=(0, 8))
        size = self.CELL * 10
        self.board = tk.Canvas(panel, width=size, height=size, bg="#142337",
                               highlightthickness=0)
        self.board.pack()
        tk.Label(panel, textvariable=self.message, bg="#101827", fg="#f2c879",
                 wraplength=460).pack(pady=12)
        controls = tk.Frame(panel, bg="#101827")
        controls.pack()
        self.roll_button = tk.Button(controls, text="Roll die", command=self.roll,
                                     bg="#7ddcc0", fg="#10211c", relief="flat",
                                     padx=18, pady=9)
        self.roll_button.pack(side="left", padx=6)
        tk.Button(controls, text="New game", command=self.reset, bg="#2a3a51",
                  fg="white", relief="flat", padx=16, pady=9).pack(side="left", padx=6)
        self.draw()

    def draw(self) -> None:
        self.board.delete("all")
        c = self.CELL
        for number in range(1, 101):
            x, y = square_center(number, c)
            color = "#23455b" if (number + number // 10) % 2 else "#1b3045"
            self.board.create_rectangle(x-c//2, y-c//2, x+c//2, y+c//2,
                                        fill=color, outline="#39566b")
            self.board.create_text(x, y, text=str(number), fill="#d6e7f2",
                                   font=("DejaVu Sans", 9))
        for start, end in JUMPS.items():
            x1, y1 = square_center(start, c)
            x2, y2 = square_center(end, c)
            self.board.create_line(x1, y1, x2, y2, fill="#7ddcc0" if end > start else "#ee927f",
                                   width=3, dash=(4, 4))
        x, y = square_center(self.position, c)
        self.board.create_oval(x-14, y-14, x+14, y+14, fill="#ffd27b", outline="#101827", width=2)

    def roll(self) -> None:
        if self.position == 100:
            return
        dice = secrets.randbelow(6) + 1
        old = self.position
        self.position = advance(self.position, dice)
        self.turns += 1
        self.message.set(f"Rolled {dice}: square {old} → {self.position} · {self.turns} turns")
        if self.position == 100:
            self.message.set(f"You won in {self.turns} turns!")
            self.roll_button.config(state="disabled")
        self.draw()

    def reset(self) -> None:
        self.position, self.turns = 1, 0
        self.message.set("Roll the die to start.")
        self.roll_button.config(state="normal")
        self.draw()


if __name__ == "__main__":
    Game().mainloop()
