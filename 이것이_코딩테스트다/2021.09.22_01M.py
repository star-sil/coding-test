#접두사
import sys
N = int(sys.stdin.readline())
dict_word = {}
for _ in range(6):
    dict_word[input()] = []
for key in dict_word.keys():
    for compare_word in dict_word.keys():
        if key != compare_word and key in compare_word:
            if key not in dict_word.values():
                dict_word[key].append(compare_word)
count = 0
for value_list in dict_word.values():
    count += len(value_list)
print(count)