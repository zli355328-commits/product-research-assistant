"""Count Unicode code points, including punctuation and internal whitespace."""
import argparse
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', nargs='?', help='UTF-8 text file; otherwise stdin')
    args = parser.parse_args()
    raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
    text = raw.strip()
    length = len(text)
    print(f'{length}/500 ' + ('PASS' if length <= 500 else 'FAIL'))
    return 0 if length <= 500 else 1

if __name__ == '__main__':
    raise SystemExit(main())
