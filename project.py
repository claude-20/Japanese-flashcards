import json
from random import randint
from pick import pick
import os
from colorama import Fore, Style  # Importing colorama library


class Card:
    def __init__(self, character, pronunciation, additional_info, use_case):
        self.character = character
        self.pronunciation = pronunciation
        self.additional_info = additional_info
        self.use_case = use_case

    def __str__(self) -> str:
        return f"The character '{Fore.BLUE}{self.character}{Style.RESET_ALL}' in Japanese, pronounced as '{Fore.GREEN}{self.pronunciation}{Style.RESET_ALL}', {Fore.YELLOW}{self.additional_info}{Style.RESET_ALL}. It can be found in words like '{Fore.CYAN}{self.use_case}{Style.RESET_ALL}'."

    def iscorrect(self, answer):
        return answer == self.pronunciation

    def print_flashcard(self):
        print(f"{Fore.RED}┌───────────────┐{Style.RESET_ALL}")
        print(f"{Fore.RED}│               │{Style.RESET_ALL}")
        print(f"{Fore.RED}│      {self.character}       │{Style.RESET_ALL}")
        print(f"{Fore.RED}│               │{Style.RESET_ALL}")
        print(f"{Fore.RED}└───────────────┘{Style.RESET_ALL}")

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        if isinstance(character, str):
            self._character = character
        else:
            raise ValueError("Character should be a Str")

    @property
    def pronunciation(self):
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        if isinstance(pronunciation, str):
            self._pronunciation = pronunciation
        else:
            raise ValueError("Pronunciation should be a Str")

    @property
    def additional_info(self):
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        if isinstance(additional_info, str):
            self._additional_info = additional_info
        else:
            raise ValueError("Additional info should be a Str")

    @property
    def use_case(self):
        return self._use_case

    @use_case.setter
    def use_case(self, use_case):
        if isinstance(use_case, str):
            self._use_case = use_case
        else:
            raise ValueError("Use case should be a Str")


def main():
    name = choose()
    cards = load_the_cards(name)
    characters = character_list(name)
    card = select_card(cards, characters)
    # Clear the terminal before printing the flashcard
    os.system("cls" if os.name == "nt" else "clear")
    card.print_flashcard()
    if is_success(card):
        print(f"\n{Fore.GREEN}Correct answer. Well done!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}Better luck next time!{Style.RESET_ALL}")
    print(f"\n{card}\n")


def choose():
    title = "Please choose a Japanese alphabet systems: "
    options = ["Hiragana", "Katakana"]
    option, _ = pick(options, title)
    return option.lower()


def load_the_cards(name):
    file_name = f"{name}.json"
    # Open the JSON file
    with open(file_name) as json_file:
        # Load the JSON data
        return json.load(json_file)


def character_list(name):
    hiragana = [
        "あ", "い", "う", "え", "お",
        "か", "き", "く", "け", "こ",
        "さ", "し", "す", "せ", "そ",
        "た", "ち", "つ", "て", "と",
        "な", "に", "ぬ", "ね", "の",
        "は", "ひ", "ふ", "へ", "ほ",
        "ま", "み", "む", "め", "も",
        "や", "ゆ", "よ", "ら", "り",
        "る", "れ", "ろ", "わ", "を",
        "ん",
    ]

    katakana = [
        "ア", "イ", "ウ", "エ", "オ",
        "カ", "キ", "ク", "ケ", "コ",
        "サ", "シ", "ス", "セ", "ソ",
        "タ", "チ", "ツ", "テ", "ト",
        "ナ", "ニ", "ヌ", "ネ", "ノ",
        "ハ", "ヒ", "フ", "ヘ", "ホ",
        "マ", "ミ", "ム", "メ", "モ",
        "ヤ", "ユ", "ヨ","ラ", "リ", 
        "ル", "レ", "ロ","ワ", "ヲ",
        "ン"
    ]

    if name == "katakana":
        return katakana
    elif name == "hiragana":
        return hiragana


def select_card(cards, characters):
    n = randint(0, 45)
    card = cards[characters[n]]

    return Card(
        characters[n],
        cards[characters[n]]["pronunciation"],
        cards[characters[n]]["additional_info"],
        cards[characters[n]]["use_case"],
    )


def is_success(card):
    count = 3
    while count != 0:
        answer = input(f"{Fore.YELLOW}\nWhat is this Character? {Style.RESET_ALL}")
        if card.iscorrect(answer):
            return True
        print(f"{Fore.RED}\nWrong answer. Please Try again!{Style.RESET_ALL}")
        count -= 1
    return False


if __name__ == "__main__":
    main()
