from itertools import permutations


def anagrams(words):
    s = {}
    while len(words) > 0:
        words1 = words.pop()
        s[words1] = s.get(words1, [])
        s[words1].append(words1)
        i = 0
        while i < len(words):
            word = words[i]
            perm = [''.join(p) for p in permutations(words1)]
            if word in perm:
                words.remove(word)
                s[words1].append(word)
            else:
                i += 1

    contain = list()

    for _, value in s.items():
        contain.append(value)

    print(contain)
    return contain


# lst = list()
# for key, value in anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']).items():
#     lst.append(value)

print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
