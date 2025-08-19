# OOP Football Score Simulator

This project is built to **demonstrate Object-Oriented Programming (OOP)** in Python using a fun, football-themed simulation.  
The code is structured around a `Team` class that models real-world objects with attributes, methods, and encapsulation.

---

## OOP Concepts Demonstrated
- **Encapsulation** – Each `Team` keeps track of its own wins, losses, ties, and points.
- **Properties** – The `record` property dynamically formats the team’s W-L(-T) record.
- **Dunder methods** – `__repr__` and `__str__` give meaningful, Pythonic representations.
- **Private methods** – `_add_points` abstracts repeated logic into an internal helper.
- **Type hints & docstrings** – Used throughout to emphasize clarity and maintainability.

---

## Features
- `Team` objects that behave like real football teams.
- Score simulation with **touchdowns, field goals, and PATs (94% success rate)**.
- Automatic record updates after each game.
- Flexible simulation (`simulate_game`) to run one or many games at once.

---

## Example
```bash
$ python football.py
Raiders beat the Patriots 27 to 24!
Raiders (1-0) PF: 27 | PA: 24
Patriots (0-1) PF: 24 | PA: 27
