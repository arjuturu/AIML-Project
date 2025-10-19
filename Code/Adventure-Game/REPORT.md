REPORT - Adventure Game (Course-End Project)

Summary
-------
This small project implements a text-based adventure game in Python (`adventure_game.py`). The game lets a player explore a forest or cave, make choices, and attempt to find a legendary treasure.

How GitHub Copilot assisted
--------------------------
- Suggested function structures and docstrings while drafting `start_game`, `forest_path`, and `cave_path`.
- Offered concise looping and input validation patterns (prompt loop) that were adapted into `input_choice()`.
- Helped formulate branching story events and short, clear in-game messages.

Key challenges
--------------
- Crafting clear but concise user prompts and keeping input handling robust against unexpected values.
- Designing a satisfying branching structure that is simple enough for a short assignment but still offers meaningful choices.

Enhancements and modifications
------------------------------
- Implemented `input_choice()` to centralize input validation and support a 'quit' option.
- Added a lightweight main loop with replay support and graceful exits.
- Provided docstrings and inline comments for readability and maintainability.

How to convert this report to PDF
---------------------------------
- Open `REPORT.md` in VS Code and use "Print to PDF" or the Markdown preview's export feature.
- Or use pandoc (if installed):

  pandoc REPORT.md -o REPORT.pdf

Notes
-----
This repository also contains an IPython notebook and other course materials. The game intentionally keeps logic small and dependency-free so it can run in any standard Python 3 environment.

