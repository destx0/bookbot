from stats import count_words ,count_chars
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 
    content = get_book_text(filepath)
    wordcount = count_words(content)
    print(f"Found {wordcount} total words")
    for k , v in count_chars(content).items():
        print(f"{k}: {v}")
