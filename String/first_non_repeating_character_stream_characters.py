def first_non_repeating_character_stream_characters(str):
    inDLL = []
    repeated = [0] * 256
    i = 0
    for s in str:
        repeated[ord(s)] += 1
        if repeated[ord(s)] >= 1:
            if s not in inDLL:
                inDLL.append(s)
            else:
                inDLL.remove(s)

        if i == len(str) - 1:
            print "First non repeating character is " + inDLL[0]
        i += 1

    print inDLL


first_non_repeating_character_stream_characters('geeksforgeeksandgeeksquizfor')
