# Telesm
An offline-first dictionary using WordNet -or- OpenAI

## Why Offline?
I'm sick of online dictionaries. Most of them display lots of ads which is distracting, and almost none of them let you save the words to review them in the future and memorzie them, unless, well, you pay for a premium package.

## Introducing Telesm
So, here's an offline dictionary that uses WordNet to display the definition and the examples of a word. It saves your searched words in a list so you can check them later in your spare time.

Now Telesm also supports calling OpenAI api to get the definition and examples of the word. See Usage for more details.

## Terminology
Telesm is the Persian word for Talisman.

## Installation
Using `pip`:

```bash
pip install telesm
```

Or if you want to have it globally:

```bash
pipx install telesm
```

## Usage

### Definition of a word

```bash
telesm <word>

# Example output:
talisman:
        ‣ a trinket or piece of jewelry usually hung about the neck and thought to be a magical protection against evil or disease
```

This will save the word to the database by default, if you don't want to save the word pass `--no-save` argument.

```bash
telesm <word> --no-save
```

### List all words

```bash
telesm --list
```

If you want to navigate over the words one by one, pass `--navigate` argument:

```bash
telesm --list --navigate
```

### Random word

```bash
telesm --random

# Example output:
accruing:
        ‣ grow by addition
Examples:
        ⁃ The interest accrues
```

### Search in saved words

```bash
telesm --search tal

# Example output:
talisman:
        ‣ a trinket or piece of jewelry usually hung about the neck and thought to be a magical protection against evil or disease
```

### Deleting a word

```bash
telesm --delete <word>
```

### Using AI

To use AI feature you need to specify your OpenAI api key in `~/.telesm.conf` file.

1. Create `~/.telesm.conf` file, if you haven't already.
2. Acquire your api key from OpenAi [Dashboard](https://platform.openai.com/api-keys).
3. Put your api key in the config file:

        OPENAI_API_KEY="<your-api-key>"


Now you can use the AI feature:

```bash
telesm --ai <word>
```

You can set `AI_FIRST=1` to `~/.telesm.conf` file to use AI without the need to pass `--ai` argument:

```bash
telesm <word> # Would use AI now
```

This will also save the word in the database so you'd have it offline for future uses. Pass `--no-save` if you don't want to save it.

If you already searched for a word without using AI and saved the word in the database, passing `--ai` would not have any effects. Try deleting the word by running `telesm --delete <word>` and try again in case you prefer to have the AI definition instead.