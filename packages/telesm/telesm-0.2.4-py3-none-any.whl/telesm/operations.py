import nltk
import os
from nltk.corpus import wordnet as wn
from telesm.ai import Ai
from telesm.decorators import Printer


class List():
    def __init__(self, args, db):
        saved_words = db.list_words()
        if not saved_words:
            print("No words saved yet.")
            exit(0)
        else:
            Printer().print_words(
                saved_words, should_navigate=args.navigate)


class DefineAI():
    def __init__(self, word, args, db):
        try:
            response, examples, status = Ai().get_definition(word)
            if status != 200:
                print("Something went wrong. Please try again later.")
                exit(1)

            Printer().print_words([(word.strip(), response, examples)])
            if not args.no_save:
                db.save_word(word, response, examples)
        except Exception as e:
            Printer().print(e)
            exit(1)


class DefineWordNet():
    def __init__(self, word, args, db):
        nltk.download('wordnet', quiet=True)
        synsets = wn.synsets(word.strip().lower())
        if not synsets:
            Printer().print(f"No definition found for '{word}'")
            exit(0)
        definition = synsets[0].definition()
        examples = synsets[0].examples()
        Printer().print_words([(word, definition, examples)])
        if not args.no_save:
            db.save_word(word, definition, examples)


class Define():
    def __init__(self, args, db):
        word_to_search = args.word if args.word else args.ai
        word = db.get_by_word(word_to_search)

        if word:
            Printer().print_words([word])
            exit(0)

        if args.ai or os.getenv("AI_FIRST", "0") == "1":
            DefineAI(word_to_search, args, db)
        else:
            DefineWordNet(word_to_search, args, db)


class RandomWord():
    def __init__(self, args, db):
        random_word = db.get_random_word()
        if not random_word:
            Printer().print("No word could be found in the database.")
            exit(0)

        Printer().print_words([random_word])


class DeleteWord():
    def __init__(self, args, db):
        word = args.delete.strip()
        try:
            db.delete_word(word)
            Printer().print(f"'{word}' is deleted.")
            exit(0)
        except Exception:
            Printer().print("An unexpected error occured. Please try again.")
            exit(1)


class SearchInDatabase():
    def __init__(self, args, db):
        keyword = args.search.strip()
        words = db.search(keyword)
        if not words:
            Printer().print(f"Nothing found for '{keyword}'.")
            exit(0)

        Printer().print_words(words, should_navigate=args.navigate)


class Perform():
    args_to_operations = {
        'list': List,
        'word': Define,
        'ai': Define,
        'random': RandomWord,
        'delete': DeleteWord,
        'search': SearchInDatabase,
    }

    def __init__(self, args, db):
        for arg, val in vars(args).items():
            if val and arg in self.args_to_operations:
                self.args_to_operations[arg](args, db)
