import sys


def remove_capslock(input_text):
    start_tag = "[CAPSLOCK]"
    end_tag = "[CAPSLOCK]"
    text = input_text
    while start_tag in text and end_tag in text:
        start_index = text.find(start_tag)
        end_index = text.find(end_tag, start_index + len(start_tag))
        if end_index == -1:
            break
        text_to_replace = text[start_index + len(start_tag) : end_index].upper()
        text = text[:start_index] + text_to_replace + text[end_index + len(end_tag) :]
    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py 'input_text'")
        sys.exit(1)

    input_text = sys.argv[1]
    output_text = remove_capslock(input_text)
    print(output_text)
