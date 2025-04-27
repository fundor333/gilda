"""Main script to create a new post."""

import os
import re


def name_cleaning(name: str) -> str:
    """Clean the name of the post to make it a valid title for Hugo."""
    title = re.sub("[^A-Za-z0-9 ]+", " ", name)
    title = title.replace("  ", " ")
    title = title.replace(" ", "-")
    title = title.lower()
    return title


def corso_fc():
    """Create a new course post."""
    print("Make a corso")
    name = input("Give me the name\n")
    title = name_cleaning(name)
    generated = f"{title}"
    os.system(f"hugo new  corsi/{generated}/index.md")
    print(f"Generated {generated}/index.md")


def membro_fc():
    """Create a new member post."""
    print("Make a membro")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new  membro/{generated}/index.md")
    print(f"Generated {generated}/index.md")


ANSWER = {
    "membro": membro_fc,
    "corso": corso_fc,
}


def main_checker():
    """Check the input and call the correct function."""
    t_input = "You need a "
    for e in ANSWER:
        t_input += f"[{e}] "
    t_input += "?\n"

    text = input(t_input)  # Python 3
    # text = "post"
    ANSWER.get(text, main_checker)()


if __name__ == "__main__":
    main_checker()
