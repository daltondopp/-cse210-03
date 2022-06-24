from terminal_service import terminal_service
from animation import animation
from word_list import word_list

class director:
    # The director class is the main class of the program.
    # It contains the main function.
    # It contains the game loop.
    def __init__(self):
        self._terminal_service = terminal_service()
        self._animation = animation()
        self._word_list = word_list()
        



    def start_game(self):
        # The start_game function is the main function of the program.
        # It contains the game loop.
        
        self._get_inputs()
        visual_word = ['_']
        guess_word = self._word_list.random_word()
        visual_word = self._word_list.blank_word(guess_word)
        parachute = self._animation.create_parachute_line()
            
        while '_' in self.visual_word:
            self._render(parachute, self.visual_word)
            self._do_updates(guess_word,parachute,self.visual_word)
            



    def _do_updates(self,guess_word,parachute,visual_word):
            if self.user_guess in guess_word:
                visual_word = self._word_list.reveal_letter(guess_word, self.user_guess)
                print()

            elif self.user_guess not in guess_word:
                # remove the top parachute line in the list
                parachute.pop(0)

            if '_' not in visual_word:
                print(f"{guess_word}\n")
                print("You win!")

            if len(parachute) == 5:
                parachute[0] = '   x   '
                self._animation.print_parachute_line(parachute)
                print("You lose!")
                print("The word was: " + guess_word)
                exit()

    def _get_inputs(self):
        pass

    def _render(self,parachute, visual_word):
        self._terminal_service.word_line(visual_word)

        self._animation.print_parachute_line(parachute)

        self.user_guess = self._terminal_service.get_input()
        return self.user_guess