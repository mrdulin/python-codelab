from otherModule import B


def A():
    for pair in [[1, 2], [3, 4]]:
        B(*pair)
