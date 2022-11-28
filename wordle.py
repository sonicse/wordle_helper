
def words_gen(filename):
    with open(filename, "r", encoding="utf8") as fin:
        for line in fin.readlines():
            line = line.strip()
            yield line


def filter_words(words, exclude, include, chars):
    for line in words:
        if len(line) != 5:
            continue

        flag = True
        for idx, char in enumerate(chars):
            if char and line[idx:idx+1] != char:
                flag = False
                break

        if not flag:
            continue

        flag = True
        for c in exclude:
            if c in line:
                flag = False
                break

        if not flag:
            continue

        flag = True
        for c in include:
            if c not in line:
                flag = False
                break

        if not flag:
            continue

        yield line

