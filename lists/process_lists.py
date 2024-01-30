import re

def process_line(line):
    # Use regular expression to remove text after "(" or "<"
    line = f"[sound:{line}.mp3]"
    return line

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = [process_line(line.strip()) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(processed_lines))

if __name__ == "__main__":
    input_filename = "lists/countries_from_anki_edited.txt"
    output_filename = "lists/countries_from_anki_sound_names.txt"
    main(input_filename, output_filename)
    print("Processing complete. Check", output_filename)
