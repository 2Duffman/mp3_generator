import requests
from bs4 import BeautifulSoup

def get_pronunciation(word):
    base_url = "https://en.wiktionary.org/wiki/"
    url = f"{base_url}{word}"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    german_pronunciation = None
    english_pronunciation = None

    # Extract German pronunciation if available
    german_section = soup.find("span", {"id": "German"})
    if german_section:
        german_pronunciation = german_section.find_next("span", {"class": "IPA"})
        if german_pronunciation:
            german_pronunciation = german_pronunciation.text.strip()

    # Extract English pronunciation if available
    english_section = soup.find("span", {"id": "English"})
    if english_section:
        english_pronunciation = english_section.find_next("span", {"class": "IPA"})
        if english_pronunciation:
            english_pronunciation = english_pronunciation.text.strip()

    if german_pronunciation:
        return german_pronunciation
    elif english_pronunciation:
        return english_pronunciation
    else:
        return None

if __name__ == "__main__":
    input_word = input("Enter a word: ")
    pronunciation = get_pronunciation(input_word)
    
    if pronunciation:
        print("Pronunciation:")
        print(pronunciation)
    else:
        print("No pronunciation information found.")
