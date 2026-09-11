# Week 3 Assignment: Hands-On Lab — Name Splitter, Bug Hunt & First Decisions

This repository contains my Week 3 Python assignment demonstrating string methods, debugging, Boolean expressions, and simple decisions.

## Files

- `name_greeter.py` — Splits a user's full name and greets them using their first name.
- `bug_hunt.py` — Fixes three bugs involving a missing quotation mark, a misspelled variable, and string/integer conversion.
- `ticket_checker.py` — Checks whether a person is an adult using a Boolean expression and displays the appropriate ticket price.
- `screenshots/` — Contains screenshots showing the programs running successfully.

## Bug Hunt Reflection

The bug that took me longest to find was the age calculation because the value returned by `input()` was a string rather than an integer. The error message helped me understand that Python could not combine the age string with the number 1. I fixed the problem by converting the input to an integer using `int()`.