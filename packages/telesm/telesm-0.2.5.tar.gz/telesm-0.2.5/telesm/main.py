#!/usr/bin/env python3

import argparse
import os
from telesm.db import Database
from telesm import operations
from telesm.env import Env




def parse_args():
    parser = argparse.ArgumentParser(
        description='Get the definition of a word')
    parser.add_argument('word', nargs='?', type=str, help='The word to define')
    parser.add_argument('--list', action='store_true',
                        help='List all saved words')
    parser.add_argument('--navigate', action='store_true',
                        help='Navigate through saved words')
    parser.add_argument('--no-save', action='store_true',
                        help='Do not save the searched word in the database')
    parser.add_argument('--random', action='store_true',
                        help='Display a random word from the database')
    parser.add_argument('--delete', type=str,
                        help='Deletes a word', metavar="<string>")
    parser.add_argument(
        '--search', type=str, help='Full-Text search for a keyword in the database, including word, its definition and exampes', metavar='<string>')
    parser.add_argument(
        '--ai', type=str, help='Use OpenAI to show the definition and etymology of the word (requires internet connection)'
    )
    return parser.parse_args()


def main():
    Env().load_env()
    DB_FILE = os.path.expanduser('~/.telesm.db')
    db = Database(DB_FILE)
    args = parse_args()
    operations.Perform(args, db)
