from game.console import Console
from game.word_tracker import Word_Tracker
from game.parachute_tracker import Parachute_Tracker
from game.word_select import Word_Select


class Director:
    """
    A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
                Description - console receives inputs and displays outputs.
        keep_playing (boolean): Whether or not the game can continue.
        word_tracker (Word_Tracker): An instance of the class of objects known as Word_Tracker.
                Description - Word_Tracker receives the var guess_letter from Console
                        and determines number of dashes remaining to guess.
        parachute_tracker (Parachute_Tracker):
                An instance of the class of objects known as Parachute_Tracker.
                Description - Parachute_Tracker receives the var state_num from
                        do_updates Method; state_num indicates which parachute outcome.
        word_select (Word_Select): An instance of the class of objects known as Word_Select.
    """

    def __init__(self):
        """
        The class constructor.

        Args:
            self (Director): an instance of Director.
        """

        self.console = Console()
        # self.word_tracker = Word_Tracker()
        # (AH) instantiate Word_Tracker() in start_game Method so Word chosen once per game.
        self.keep_playing = True
        # self.parachute_tracker = Parachute_Tracker()
        # (AH) instantiate Parachute_Tracker() in start_game Method
        #               so parachute is refreshed for each game.
        self.word_select = Word_Select()

    def start_game(self):
        """
        Begin by randomly choosing a new word from list to guess.
        Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        # (Suggestion 1) Word is selected from MIT 1000 word list in reqmts file.
        # (AH) Class Var assigned to select_word() Method in Word_Select Class <SarahA>.
        self.word = self.word_select.select_word()

        # (AH) Explanation:
        # Create Word_Tracker Class instance in start_game Method so Word_Tracker has self.word.
        # The random chosen word from the MIT list is stored in Word_Tracker Class as self.word
        self.word_tracker = Word_Tracker(self.word)
        # Create Parachute_Tracker Class instance in start game Method
        self.parachute_tracker = Parachute_Tracker()
        # Var parachute_tracker.state_num  will display one of 5 possible outcomes.

        # (AH) Loop to call Methods to continue game.
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):
        """
        Outputs the important game information for each round of play.
        In this case, that means the correct letter guessed fills in a dash
        while an incorrect letter guessed causes a parachute cut.

        Args:
            self (Director): An instance of Director.
        """
        # (AH) Print current word guessing results.
        # (AH) Word_Tracker Class determine word length.
        # (AH) Get word_status() Method in Word_Tracker Class <Mireya?>.
        # (AH note) word_status() will return the text for letters and dashes.
        word_progress = self.word_tracker.word_status()
        self.console.write(word_progress)

        # (AH) Print current parachute.
        print_parachute = self.parachute_tracker.get_parachute()
        self.console.write(print_parachute)

    def get_inputs(self):
        """ (AH).
        Gets the inputs at the beginning of each round of play. In this case,
        start by displaying current word guessing status and parachute status.
        ie, word with letters filled in and empty dashes, or parachute cuts.

        Args:
            self (Director): An instance of Director.
        """

        # (AH) Class Var assigned to gett letter guess from user.
        self.guess_letter = self.console.read_word("Guess a letter [a-z]:  ")

    def do_updates(self):
        """
        Updates the important game information for each round of play.
        In this case, that means the .

        Args:
            self (Director): An instance of Director.
        """

        # (AH) Track Method in Word_Tracker Class determines if
        # 	guess_letter is correct and be put in place of a dash,
        # 	then returns a Boolean for parachute to display same
        # 	parachute as prior turn; or guess_letter is incorrect
        # 	and returns a Boolean for the parachute to be cut.
        # (AH) guess_correct is a Boolean data type.
        guess_correct = self.word_tracker.track(self.guess_letter)

        # (AH) increment self.state_num if word_tracker.track(self.guess_letter) is False.
        if not guess_correct:
            self.state_num += 1

        # (AH) Parachute_Tracking Class determine correct parachute to display;
        #                                       depending on self.state_num.
        # parachute_progress = self.parachute_tracking.parachute_draw(self.state_num)

        # (AH) KELTON suggest use !=4  to determine if game over, like Solo CkPt. ???
        self.keep_playing = self.parachute_tracker.game_continue()