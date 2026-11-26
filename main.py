"""Make the Judge Laugh in One Line — entry for make.fun.

Writes one funny line to /output/entry.txt.
"""
import os

# The joke: even the smart fridge is fed up — a household appliance files a complaint about midnight snacking, as if it were tired of the owner's life choices.
TEXT = "My smart fridge just filed a complaint about my midnight snacking — apparently even the appliances are tired of my life choices."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
