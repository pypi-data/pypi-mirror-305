import curses


class Formatter():
    def __init__(self):
        pass

    def format_word_with_definition_and_examples(self, word, definition, examples=[]):
        if examples:
            formatted_examples = "\n".join(
                f"\t⁃ {example}" for example in examples)
            examples_text = f"\nExamples:\n{formatted_examples}"
        else:
            examples_text = ""

        return f"{word}:\n\t‣ {definition}{examples_text}"


class Printer():
    def __init__(self):
        pass

    def print(self, str):
        print(str)

    def print_words(self, words, should_navigate=False):
        if should_navigate:
            self.print_navigate(words)
        else:
            for word in words:
                print(Formatter().format_word_with_definition_and_examples(
                    word[0], word[1], word[2]))
                print("---")

    def print_navigate(self, words):
        def navigate_words(stdscr):
            curses.curs_set(0)
            curses.start_color()
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

            current_index = 0
            total = len(words)

            while True:
                stdscr.clear()
                word, definition, examples = words[current_index]
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(0, 0, f"{word}:")
                stdscr.addstr(1, 4, f"{definition[:curses.COLS - 1]}")
                if examples:
                    stdscr.addstr(2, 0, "Examples:")
                    for i, example in enumerate(examples):
                        stdscr.addstr(3+i, 4, f"- {example}")
                stdscr.attroff(curses.color_pair(1))
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(curses.LINES - 3, 0,
                              f"({current_index+1}/{total})")
                stdscr.addstr(curses.LINES - 2, 0,
                              "Press 'J' to move down, 'K' to move up, 'Q' to quit.")
                stdscr.attroff(curses.color_pair(2))
                stdscr.refresh()

                key = stdscr.getch()

                if key == ord('j') and current_index < len(words) - 1:
                    current_index += 1
                elif key == ord('k') and current_index > 0:
                    current_index -= 1
                elif key == ord('q'):
                    break
        curses.wrapper(navigate_words)
