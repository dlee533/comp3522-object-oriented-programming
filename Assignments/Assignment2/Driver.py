from Store import Store


def main():
    """
    Drives the Store program.
    """
    print("Welcome to our Holiday Store!")
    store = Store()
    while store.display_menu():
        pass


if __name__ == "__main__":
    main()
