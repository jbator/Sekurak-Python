import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex2_file_lines_counter.py <path>")

path = sys.argv[1]

with open(path) as f:
    all_lines = f.readlines()

total_lines = len(all_lines)

text_lines = 0
blank_lines = 0
comments_lines = 0

for line in all_lines:
    line = line.strip()
    if line == "":
        blank_lines += 1
    elif line.startswith("#"):
        comments_lines += 1
    else:
        text_lines += 1
        #print(f"Line: {line}")

print(f'Total lines: {total_lines}, Text lines: {text_lines}, Blank lines: {blank_lines}, Comments: {comments_lines}')