class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class TeamNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
