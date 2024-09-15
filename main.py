def get_book_text(path):
  with open(path) as f:
    return f.read()

def book_word_count(words_to_count):
  words = words_to_count.split()
  return len(words)

def count_characters(text_to_count):
  result = {}

  for letter in text_to_count:
    letter_lower = letter.lower()
    if letter_lower in result:
      result[letter_lower] += 1
    else:
      result[letter_lower] = 1

  return result

def sort_on(dict):
  return dict["num"]

def sorted_list(character_counts):
  # Process character counts into new dictionary for report. 
  char_list = []
  for character in character_counts:
    char_list.append({"letter": character, "num": character_counts[character]})
  
  char_list.sort(reverse=True, key=sort_on)
  return char_list

def main():
  path_to_book = "books/frankenstein.txt"
  file_contents = get_book_text(path_to_book)
  # print(file_contents)

  word_count = book_word_count(file_contents)
  #print(f"WORDS: {word_count}")

  letter_counts = count_characters(file_contents)
  #print(f"Letter counts: ", letter_counts)

  chars_sorted = sorted_list(letter_counts)

  print(f"--- Begin report of {path_to_book} ---")
  print(f"{word_count} words found in the document")
  print()

  for item in chars_sorted:
    if not item["letter"].isalpha():
      continue
    print(f"The '{item['letter']}' character was found {item['num']} times")

  print("--- End report ---")
 


  print(chars_sorted)
  

main()
