def unique_words(file):
    filedata = file.read()
    words = filedata.split(' ')
    found_words = []
    final_result = []
    for word in words:
        if word in found_words and word not in final_result:
            final_result.append(word)
        else:
            found_words.append(word)
    return final_result

def count_the_article(file):
    filedata = file.read()
    words = filedata.split()
    return len(words)

def sorted_words(file):
    filedata = file.read()
    words = filedata.split()
    words.sort(key=lambda item: (-len(item), item))
    return words


def character_word_count(file):
    filedata = file.read()
    words = filedata.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def starts_with_vow(file):
    filedata = file.read()
    words = filedata.split()
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    vowel_words = []
    for word in words:
        if word.startswith(vowels):
            vowel_words.append(word)
    return vowel_words

def rare_words(file,given_dictionary,all_book_words):
    filedata = file.read()
    words = filedata.split()
    all_book_words.append(words)
    rare_list = (x for x in words if x not in given_dictionary)
    return list(rare_list)                                                                                                                                                                                                                                                                                  

def unused_word(all_book_words,given_dictionary):
    rare_list = (x for x in given_dictionary if x not in all_book_words)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    list(rare_list)                                                                             
    unused_dict = dict()
    for word in rare_list:
        if word in unused_dict:
            unused_dict[word] += 1                                                                                                                                                                  
        else:
            unused_dict[word] = 1
    return unused_dict


given_dictionary = []
all_book_words = []
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/20k.txt","r") as myfile:
    filedata = myfile.read()
    given_dictionary = filedata.split()

with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:
    print(unique_words(myfile))
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:
    print("Number of words in book = "+ str(count_the_article(myfile)))
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:
    print(sorted_words(myfile))
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:
    print(character_word_count(myfile))
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:
    print(starts_with_vow(myfile))
with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book1.txt","r") as myfile:                                                                                                                                
    print(rare_words(myfile,given_dictionary,all_book_words))
    

with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book2.txt","r") as myfile:
    print(rare_words(myfile,given_dictionary,all_book_words))

with open("/home/fazil/openbook1-fazil-ahmed-hakeem/Book3.txt","r") as myfile:
    print(rare_words(myfile,given_dictionary,all_book_words))

print(unused_word(all_book_words,given_dictionary))

