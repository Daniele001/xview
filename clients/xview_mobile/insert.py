from exception import NoDigitsError, TooManyArgumentsError


class Insert:
    def __init__(self, args):
        self.args = args

    def check(self):
        if len(self.args) - 1 == 1:
            if self.args[1].isdigit():
                return int(self.args[1])
            else:
                raise NoDigitsError("Please insert the number of episodes that you want to see")
        if len(self.args) - 1 == 0:
            return 0
        else:
            raise TooManyArgumentsError("Too many arguments")