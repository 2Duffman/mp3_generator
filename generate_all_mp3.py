from generator_script import download_data, decode_and_save
from scraper_for_ipa import get_pronunciation
import codecs

voice = "Vicki"
#the IPA notation in the files was taken from ChatGPT and is often not correct. I made the Wiktionary scraper script to get the real IPA notation. CBA to change the lists.
country_list = "countries_from_anki_edited"
capital_list = "capitals_from_anki_edited"
lists = [country_list, capital_list]
countries = []
capitals = []
with open(f"lists/{country_list}.txt") as f:
    data = f.read()
    data = data.split("\n")
    for line in data:
        countries.append(line)
with open(f"lists/{capital_list}.txt") as f:
    data = f.read()
    data = data.split("\n")
    for line in data:
        capitals.append(line)
print(capitals, countries)
for country in countries:
    ipa = get_pronunciation(country)
    if ipa:
        voice_file = download_data(ipa, voice)
        decode_and_save(voice_file, f"files/countries/{country.split('::')[0]}.mp3")
for capital in capitals:
    ipa = get_pronunciation(capital)
    if ipa:
        voice_file = download_data(ipa, voice)
        decode_and_save(voice_file, f"files/capitals/{capital.split('::')[0]}.mp3")
