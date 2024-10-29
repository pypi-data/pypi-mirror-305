import os
import json
import hashlib
import anthropic
import argparse
from dotenv import load_dotenv
import requests
from google.cloud import translate_v2 as translate

# Load environment variables
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
media_path = os.getenv("MEDIA_PATH", "output/media")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Instantiate the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Initialize the Google Translate client
translate_client = translate.Client()

# Create directories if they don't exist
os.makedirs(media_path, exist_ok=True)

def translate_to_english(word):
    """Translate a Japanese word to English using Google Cloud Translation API."""
    result = translate_client.translate(word, target_language='en')
    return result['translatedText']


def generate_hash(text):
    """Generate a SHA-256 hash of the given text."""
    return hashlib.sha256(text.encode()).hexdigest()

def get_word_info(word):
    system_message = (
        "You are an assistant providing comprehensive vocabulary information for Japanese English learners. "
        "Generate JSON data for the word with the following fields strictly in JSON format: "
        "{word, ipa, meanJP, typeOfWord (ex: verb: EN, JP), cefr, frequency (highest, high, often, rare), "
        "define1..N [EN, JP], origin [EN, JP], formality [EN, JP], "
        "usage [Contextual Usage: Describe situations where this word is suitable or not in both EN and JP, "
        "Decision Factors: Criteria for choosing this word over others in both EN and JP, "
        "Examples: Provide real-life examples with explanations of meaning and intent in both EN and JP], "
        "exampleSentence [EN, JP], exampleArticles [EN, JP], exampleTalks [EN, JP], exampleToddler [EN, JP], "
        "collocation1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>], "
        "idiom [casual: {idiom1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>]}, "
        "formal: {idiom1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>]}], "
        "slang [casual: {slang1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>]}, "
        "formal: {slang1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>]}], "
        "alternative1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>], "
        "synonym1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>], "
        "antonym1..3 [EN, JP, sample<EN: Cloze sample sentence with {{c1::missing word or phrase}}, JP: Japanese translation without Cloze>], "
        "note [EN, JP], SpeechChanges (if exist, or 'na'): EN, JP, "
        "medias: {youglish: URL to Youglish search for word, gimage: URL to Google Images search, "
        "dictionary_com: URL to Dictionary.com for word, merriam_webster: URL to Merriam-Webster for word, "
        "oxford_learners: URL to Oxford Learner's Dictionaries for word, cambridge: URL to Cambridge Dictionary for word, "
        "thesaurus: URL to Thesaurus.com for word, ngram: URL to Google Ngram Viewer for word, "
        "wiktionary: URL to Wiktionary for word}}. "
        "Do not add any text outside of this JSON object."
    )
    
    messages = [{"role": "user", "content": [{"type": "text", "text": f"Generate JSON data from word: '{word}'."}]}]

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8172,
            temperature=1,
            system=system_message,
            messages=messages
        )
        
        word_info = response.content[0].text.strip()
        word_info_json = json.loads(word_info)
        return word_info_json

    except json.JSONDecodeError:
        print("Error: Unable to parse response as JSON.")
        return {"error": "Failed to parse response as JSON", "response": word_info}
    except Exception as e:
        return {"error": f"Error retrieving word information: {str(e)}"}

def process_text_item(text_en, text_jp, sample_en=None, sample_jp=None):
    """Generate hash for text item and return structured data with media links."""
    data = {
        "EN": text_en or "",  # Ensure EN field is always present
        "JP": text_jp or "",  # Ensure JP field is always present
        "Hash": generate_hash(text_en or "")
    }
    if sample_en and sample_jp:
        data["Sample"] = {
            "EN": sample_en,
            "JP": sample_jp,
            "Hash": generate_hash(sample_en)
        }
    return data

def main():
    parser = argparse.ArgumentParser(description="A CLI tool for Japanese learners to study English vocabulary using Anthropic API.")
    parser.add_argument("word", type=str, help="The English word to look up.")
    args = parser.parse_args()

    # word_info = get_word_info(args.word)
  
    word = args.word
    if any("\u4e00" <= char <= "\u9fff" for char in word):
        word = translate_to_english(word)
        print(f"Translated '{args.word}' to '{word}'.")

    word_info = get_word_info(word)
    # print(json.dumps(word_info, indent=2, ensure_ascii=False))
  
    # Process defines
    for i in range(1, 4):
        define_key = f"define{i}"
        if define_key in word_info:
            word_info[define_key] = process_text_item(
                word_info[define_key].get("EN", ""), 
                word_info[define_key].get("JP", ""),
            )

    # Process usage and add Japanese translations and hash
    if "usage" in word_info:
        word_info["usage"] = {
            "Contextual Usage": process_text_item(
                word_info["usage"]["Contextual Usage"].get("EN", ""), 
                word_info["usage"]["Contextual Usage"].get("JP", "")
            ),
            "Decision Factors": process_text_item(
                word_info["usage"]["Decision Factors"].get("EN", ""), 
                word_info["usage"]["Decision Factors"].get("JP", "")
            ),
            "Examples": process_text_item(
                word_info["usage"]["Examples"].get("EN", ""), 
                word_info["usage"]["Examples"].get("JP", "")
            )
        }

    # Process example sentences and add hashes for samples
    for key in ["exampleSentence", "exampleArticles", "exampleTalks", "exampleToddler"]:
        if key in word_info:
            word_info[key] = process_text_item(
                word_info[key].get("EN", ""), word_info[key].get("JP", "")
            )

    # Process collocations
    for i in range(1, 4):
        collocation_key = f"collocation{i}"
        if collocation_key in word_info:
            word_info[collocation_key] = process_text_item(
                word_info[collocation_key].get("EN", ""), 
                word_info[collocation_key].get("JP", ""),
                word_info[collocation_key].get("sample", {}).get("EN"),
                word_info[collocation_key].get("sample", {}).get("JP")
            )

    # Process idioms, slang, alternatives, synonyms, and antonyms with casual/formal distinctions
    for category in ["idiom", "slang"]:
        for style in ["casual", "formal"]:
            if style in word_info.get(category, {}):
                for i in range(1, 4):
                    key = f"{category}{i}"
                    if key in word_info[category][style]:
                        word_info[category][style][key] = process_text_item(
                            word_info[category][style][key].get("EN", ""), 
                            word_info[category][style][key].get("JP", ""),
                            word_info[category][style][key].get("sample", {}).get("EN"),
                            word_info[category][style][key].get("sample", {}).get("JP")
                        )

    # Process alternatives, synonyms, and antonyms without casual/formal distinction
    for category in ["alternative", "synonym", "antonym"]:
        for i in range(1, 4):
            key = f"{category}{i}"
            if key in word_info:
                word_info[key] = process_text_item(
                    word_info[key].get("EN", ""), word_info[key].get("JP", ""),
                    word_info[key].get("sample", {}).get("EN"),
                    word_info[key].get("sample", {}).get("JP")
                )

    # Output the processed word information with hash values
    print(json.dumps(word_info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
