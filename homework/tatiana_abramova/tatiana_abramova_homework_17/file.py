import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('logdir', help='Path to folder with logs')
parser.add_argument('-t', '--text', required=True, help='Text to search')
args = parser.parse_args()


def get_files_in_directory(folder: str):
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]


def find_text_in_line(line: str, text: str, line_number: int, filename: str):
    results = []
    words = line.strip().split()

    if text in words:
        position = words.index(text)
        before = words[max(0, position - 5): position]
        after = words[position + 1: position + 6]
        snippet = ' '.join(before) + f" {text} " + ' '.join(after)
        results.append((filename, line_number, snippet))

    return results


def search_in_file(filepath: str, text: str):
    results = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for i, file_line in enumerate(f, start=1):
            found = find_text_in_line(file_line, text, i, os.path.basename(filepath))
            results.extend(found)
    return results


def logs_files():
    for filepath in get_files_in_directory(args.logdir):
        results = search_in_file(filepath, args.text)
        for filename, line_number, snippet in results:
            print(f'File: {filename}, Line: {line_number}')
            print(snippet)


logs_files()
