from enum import Enum


class Actions(Enum):
    Exit = 0
    AddBook = 1
    RemoveBook = 2
    FindBook = 3
    PrintBook = 4
    PrintAll = 5
    Undo = 6
    Return = "Что-нибудь"