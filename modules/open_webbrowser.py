import webbrowser


def make_webbrowser(search_term: str):
    webbrowser.open("https://www.google.com/search?q=" + search_term)


if __name__ == "__main__":
    user_term = input('Enter a search term: ')
    make_webbrowser(user_term)
