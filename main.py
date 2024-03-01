from morse_dict import morse_alphabet
import re


def main():
  text = input('Enter your message: ').upper()
  clean_text = " ".join(text.split())
  output = ""
  regex = '[^a-zA-Z0-9İÜÖÇĞŞ ]'
  text_array = re.findall(regex,text)
  print(text_array)
  special_chars = {'İ':'I','Ö':'O','Ü':'U','Ç':'C','Ğ':'G','Ş':'S'}
  print(str(special_chars.keys()))
  if len(text_array) > 0 or any(char in special_chars for char in text):
    new_text_arr = [*text]
    print(new_text_arr)
    for char in new_text_arr:
      if char in special_chars:
        new_text_arr[new_text_arr.index(char)] = special_chars[char]
      if char in text_array:
        new_text_arr[new_text_arr.index(char)] = " "
    print(new_text_arr)
    output = "".join(new_text_arr).strip()
    clean_text = " ".join(output.split())
    print(morse_converter(clean_text))
  else:
    print(morse_converter(clean_text))


def morse_converter(text): 
  arr = text.split(" ")
  new_text = []
  for letter in arr:
    char = [*letter]
    for ch in char:
      new_text.append(morse_alphabet[ch])
      new_text.append(" ")
    new_text.append("/")
  output = "".join(new_text)
  return output  















if __name__ == "__main__":
  main()