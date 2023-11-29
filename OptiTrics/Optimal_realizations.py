# There are a lot of simple tricks

def delete_copies(a: list):
    return list(dict.fromkeys(a).keys())


def example_delete_copies():
    a = [1, 2, 3, 4, 2, 3, 5, 2, 3, 67]
    print(delete_copies(a))
