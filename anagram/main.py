import collections

def word_hash():

    """"Create a hash table of the 7 letter words with the key as the
    sorted(alphabetically) word and the value the word or words """

    sorted_dict = collections.defaultdict(list)
    words = [ x.strip() for x in open("dictionary.txt", "r") if len(x.strip()) == 7 ]

    for x in words:
        x_sorted = "".join(sorted(x))
        sorted_dict[x_sorted].append(x)

    return sorted_dict

if __name__ == '__main__':

    test = ['RNOSVEI','RUIMOFN','ISCLINO','GUNEENI']
    test1 = word_hash()
    for word in test:
        ana_list = test1["".join(sorted(word.lower()))]
        print(f"{word} anagrams are : {ana_list}")
