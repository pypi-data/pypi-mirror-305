from spellchecker import SpellChecker
import unicodedata

def initialize_spell_checker(canadian_cities, us_cities):
    all_cities = set([city.lower() for city in canadian_cities + us_cities])
    spell_checker = SpellChecker()
    spell_checker.word_frequency.load_words(all_cities)
    return spell_checker

def correct_spelling(word, spell_checker):
    if word is None:
        return None
    word_normalized = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode('utf-8')
    corrected = spell_checker.correction(word_normalized.lower())
    return corrected.title() if corrected else word_normalized

