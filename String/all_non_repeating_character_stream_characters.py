def all_non_repeating_character_stream_characters(str):
    dll = []
    count = [0] * 256

    for s in str:
        count[ord(s)] += 1
        if count[ord(s)] > 1:
            if s in dll:
                dll.remove(s)
        elif count[ord(s)] == 1:
            dll.append(s)

    return dll

print all_non_repeating_character_stream_characters('ogeekqusigefeksazndgeeksr')