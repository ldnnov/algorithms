import hashlib


# Maybe I didn't understand task description correctly.
def substring_count(string):
    str_length = len(string)
    empty_substring_hash = hashlib.sha1(' '.encode('utf-8')).hexdigest()
    substring = ''
    hashes = set()
    i = 0
    while i < str_length - 1:
        for j in range(i, str_length):
            hashes.add(hashlib.sha1(
                (substring + string[j]).encode('utf-8')
            ).hexdigest())
        substring += string[i]
        i += 1
    if empty_substring_hash in hashes:
        hashes.remove(empty_substring_hash)

    return len(hashes)


s = input("Insert some string: ")
sub_count = substring_count(s)
print(f"Substrings in \"{s}\": {sub_count}")
