import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)



dictionary_list = []
dictionary_book = open("dictionary.txt")
for line in dictionary_book:
    dictionary_list.append(line.strip())
dictionary_book.close()

#Linear Search
print("---Linear Search---")
story_file = open('AliceInWonderLand200.txt')
for variable, line in enumerate(story_file):
    word_list = split_line(line)
    for word in word_list:
        current_position = 0

        while current_position < len(dictionary_list) and dictionary_list[current_position] != word.upper():
            current_position += 1


            if current_position == len(dictionary_list):
                print(f"line {variable + 1}, wrong spelling:{word}")

story_file.close()

#Page Break
#_______________________________________________________________________________________________________________________

print("---Binary Search---")

story_file = open("AliceInWonderLand200.txt")
for variable, line in enumerate(story_file):
    word_list = split_line(line)
    for word in word_list:

        lower_level = 0
        top_level = len(dictionary_list) - 1
        found = False

        while lower_level <= top_level and not found:
            between_pos = (lower_level + top_level) //2

            if  dictionary_list[between_pos] < word.upper():
                lower_level = between_pos + 1

            elif dictionary_list[between_pos] > word.upper():
                top_level = between_pos - 1

            else:
                found = True

        if not found:
            print(f"line {variable + 1}, wrong spelling:{ word}")

story_file.close()









