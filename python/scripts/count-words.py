"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    words = dict()

    for word in s.split():
        if word not in words:
            words[ word ] = 1
        else:
            words[ word ] += 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    list = []
    for key in words.keys():
        val = words[ key ]
        list.append( (key, val) )

    alpha = sorted(list, key=lambda x: x[0], reverse=False)

    top_n = sorted(alpha, key=lambda x: x[1], reverse=True)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    return top_n[ 0:n ]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()