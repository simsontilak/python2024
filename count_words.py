# Write a program to get a sentence as input and print the number of words in that sentence
import re


def count_words(sentence):
    count = 0
    prev_space = False
    for letter in sentence.strip():
        if letter == ' ' or letter == '\t':
            if not prev_space:
                count += 1
            prev_space = True
        else:
            prev_space = False
    if count != 0 or len(sentence.strip()) != 0:
        return count + 1
    else:
        return count


def alt_count_words(sentence):
    word_list = re.split(r'\s+',sentence.strip())
    return len(word_list)


def main():
    sentence = input("Enter a sentence:")
    word_count = count_words(sentence)
    alt_count = alt_count_words(sentence)
    print("The number of words in the sentence is", word_count)
    print("The number of words in the sentence is", alt_count)


if __name__ == "__main__":
    main()
