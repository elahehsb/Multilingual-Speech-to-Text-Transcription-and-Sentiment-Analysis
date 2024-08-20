from langdetect import detect_langs

class LanguageIdentifier:
    def detect_language(self, text):
        return detect_langs(text)[0]

if __name__ == "__main__":
    lang_identifier = LanguageIdentifier()
    language = lang_identifier.detect_language("Bonjour tout le monde")
    print("Detected Language:", language)
