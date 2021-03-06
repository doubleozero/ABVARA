# I. Calculations based on: https://www.sapling.com/8093755/salary-audio-book-narrator
#
# New narrator = $50/hr for small publishers
# Med-large publishers = $100/hr - $350/hr
# Finished-hour = the actual reading of a book (book w/ reading time of 5rs = 5 finished-hours)
# Standard rate: $125/hr rec. time + $500/finished-hour
# Some narrators paid by page or by word instead.  $125/page or $0.01-0.05/word (per Voices.com)

# II. Calculations based on:
# https://krystalwascher.com/narrator-blog/how-much-money-can-you-make-recording-audiobooks-from-home
#
# New narrator = $80/finished-hour

class Rate:
    def __init__(self):
        self.xp_level = 0
        self.publisher = 0
        self.rate = 0

        self.xp_message = "NO DATA"
        self.pub_message = "NO DATA"

    def rate_calculator(self, xp, pub_size):
        print(xp)
        print(pub_size)

        self.switch_cases(xp, pub_size)

        if self.xp_level == 1:
            self.xp_message = "You're new!\nNew voice actors typically charge $50/hr for small publishers."
            if self.publisher == 1:
                self.pub_message = "Since your client is a small publisher, let's stick with $50/hr."
                self.rate = 50
            elif self.publisher == 2:
                self.pub_message = "Snagged a large publisher early on?  Nice!\n" \
                                 "The bigger guys typically run $100/hr - $350/hr for experienced talent.\n" \
                                 "For newcomers, $80/hr is a typical average to expect."
                # self.rate = ?
            else:
                self.pub_message = "That's not even on the menu!  Are you a hacker?"
        elif self.xp_level == 2:
            self.xp_message = "Not your first rodeo, huh?"
            if self.publisher == 1:
                self.pub_message = "Since your client is a small publisher, let's stick with $50/hr."
                # self.rate = ?
            elif self.publisher == 2:
                self.pub_message = "Snagged a large publisher early on?  Nice!\n" \
                                 "Since you're experienced and they're one of the big guys, let's aim for $350/hr."
                self.rate = 350
            else:
                self.pub_message = "That's not even on the menu!  Are you a hacker?"
        else:
            self.xp_message = "That's not even on the menu!  Are you a hacker?"

        # Dictionary with both variables - never got this to work:
        # print("Dictionary test:")
        #
        # exp_and_pub_size = {
        #     'exp': ['New to the market', 'Experienced voice actor'],
        #     'pub': ['Small/Medium publisher', 'Large publisher'],
        # }

    def switch_cases(self, xp, pub_size):
        # Sometimes lambdas must be included in choices, but not this time (unsure why)
        xp_choices = {
            "I'm just getting started": 1,
            "Experienced voice actor": 2
        }
        pub_choices = {
            "Small publisher": 1,
            "Medium/Large publisher": 2
        }
        self.xp_level = xp_choices.get(xp, 0)
        self.publisher = pub_choices.get(pub_size, 0)
