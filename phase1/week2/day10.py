"""
Day 10 — Error Handling + File I/O
Phase 1 · Week 2 · Wed Jun 3, 2026 (IST)
Goal: write code that SURVIVES bad input instead of crashing.
"""


# =====================================================================
# BLOCK 1 — ERROR HANDLING
# =====================================================================

# --- Exercise 1.1: safe_divide -------------------------------------
# Return a / b. If b == 0, catch ZeroDivisionError, print a message,
# and return None (instead of crashing).
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("b cannot be zero")
        return None


# --- Exercise 1.2: safe_int ----------------------------------------
# Return int(s). If s is not a valid integer, catch ValueError and
# return None. Test it with "42" (works) and "hello" (fails).
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer")
        return None


# --- Exercise 1.3: custom exception --------------------------------
# Define your own exception type, then raise it for bad input.
class NegativeNumberError(Exception):
    pass


def checked_sqrt(n):
    # If n < 0, raise NegativeNumberError(...). Otherwise return n ** 0.5.
    if n < 0:
        raise NegativeNumberError(f"can't sqrt a negative number: {n}")
    return n ** 0.5


# =====================================================================
# BLOCK 2 — FILE I/O
# =====================================================================

# --- Exercise 2.1: write_lines -------------------------------------
# Open `path` in WRITE mode ('w') using `with`, and write each string
# in `lines` on its own line (remember to add "\n" after each one).
# NOTE: 'w' wipes the file first, then writes.
def write_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


# --- Exercise 2.2: read_file ---------------------------------------
# Open `path` in READ mode ('r') using `with` and return the whole
# contents as a string. Wrap it so a missing file doesn't crash:
#   try / except FileNotFoundError -> print a friendly message, return None.
# (This is today's fusion: file I/O + Block 1 error handling.)
def read_file(path):
    try:
        with open(path, "r") as f:
            return  f.read()
    except FileNotFoundError:
        print(f"file not found: {path}")
        return None


# --- Exercise 2.3: append_line -------------------------------------
# Open `path` in APPEND mode ('a') using `with`, and add line + "\n"
# to the end. 'a' keeps the existing content (unlike 'w').
def append_line(path, line):
    with open(path, "a") as f:
        return f.write(line + "\n")


if __name__ == "__main__":
    # --- Block 1 ---
    print(safe_divide(3, 0))
    print(safe_int("42"))
    print(safe_int("hello"))
    try:
        print(checked_sqrt(10))
        print(checked_sqrt(-10))
    except NegativeNumberError as e:
        print(e)

    # --- Block 2 ---  (uncomment each line as you implement the function)
    write_lines("animals.txt", ["cat", "dog", "bird"])
    print(read_file("animals.txt"))   # exists -> prints the 3 animals
    print(read_file("ghost.txt"))     # missing -> handled gracefully, returns None
    append_line("animals.txt", "fish")
    print(read_file("animals.txt"))   # "fish" should now be on the end

# ---------------------------------------------------------------------
# 📺 FREE VIDEO REFERENCES (Day 10)
#   Block 1 - Error handling  | Corey Schafer, "Using Try/Except Blocks"
#       https://www.youtube.com/watch?v=NIWwJbo-9_8
#   Block 2 - File I/O        | "How to Read and Write Files in Python"
#       https://www.youtube.com/watch?v=Jsnw6HLASZA
#   Reference (free, official) | Python docs: Errors and Exceptions
#       https://docs.python.org/3/tutorial/errors.html
#   Rule: attempt the exercises FIRST, then watch to consolidate.
# ---------------------------------------------------------------------
