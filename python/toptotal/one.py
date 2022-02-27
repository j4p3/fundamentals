def crop(input, limit):
    words = input.split()
    count = 0

    for i, word in enumerate(words):
        count += len(word)
        if i < len(words):
            count += 1
        if count > limit:
            return " ".join(words[:i])
    return input