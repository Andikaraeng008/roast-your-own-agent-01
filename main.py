import os

TEXT = "My agent's idea of a roast is a bullet list of my typos, ranked by severity, with a footnote apologising for the tone."

assert 1 <= len(TEXT) <= 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
