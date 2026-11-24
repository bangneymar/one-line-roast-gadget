import os

SETUP = "Your charging cable only works if you bend it at exactly 43 degrees and wedge it under a book, "
TWIST = "a daily yoga pose you perform for a phone that never says thanks."
LINE = SETUP + TWIST

def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

def main():
    write_entry("/output/entry.txt", LINE)

if __name__ == "__main__":
    main()
