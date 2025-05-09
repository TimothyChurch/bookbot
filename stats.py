def get_word_count(text):
    word_count = len(text.split())
    return word_count

def charater_count(text):
    words = text.split()
    char_counts = {}
    character_list = []
    for word in words:
        chars = list(word)
        for char in chars:
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    for char in char_counts:
        character_list.append({'char': char, 'num': char_counts[char]  })
    character_list.sort(key=lambda x: x['num'], reverse=True)
    return character_list