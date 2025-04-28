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
    os.system(f"hugo new corso/{generated}/index.md")
    print(f"Generated {generated}/index.md")


def membro_fc():
    """Create a new member post."""
    print("Make a membro")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new membro/{generated}/index.md")
    print(f"Generated {generated}/index.md")


def spazio_fc():
    """Create a new space post."""
    print("Make a spazio")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new spazio/{generated}/_index.md")
    print(f"Generated {generated}/_index.md")


def quest_fc():
    """Create a new quest post."""
    print("Make a quest")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new quest/{generated}/index.md")
    print(f"Generated {generated}/index.md")


def personaggio_fc():
    """Create a new character post."""
    print("Make a personaggio")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new personaggio/{generated}/index.md")
    print(f"Generated {generated}/index.md")


def bestiario_fc():
    """Create a new bestiario post."""
    print("Make a bestiario")
    name = input("Give me the name\n")
    title = name_cleaning(name)

    generated = f"{title}"

    os.system(f"hugo new bestiario/{generated}/index.md")
    print(f"Generated {generated}/index.md")


ANSWER = {
    "membro": membro_fc,
    "corso": corso_fc,
    "spazio": spazio_fc,
    "quest": quest_fc,
    "personaggio": personaggio_fc,
    "bestiario": bestiario_fc,
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
