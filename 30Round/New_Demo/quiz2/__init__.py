from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_1 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="1. Will you know your color before you choose whether to trade?",
        choices=[
            [0, "Yes"],
            [1, "No, but I know that the chance of being red is the same for everyone in the group."],
            [0, "No information given about this"],
        ]
    )

    question_2 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="2. Suppose you chose to trade. How may trades will you execute?",
        choices=[
            [0, "1 for sure"],
            [0, "2 for sure"],
            [1, "0, 1 or 2 depending on whether neither, one or both of the other two participants chose to trade."],
        ]
    )

    question_3 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="3. How many players can be red in a period?",
        choices=[
            [1, "One"],
            [0, "Two"],
            [0, "Three"],
        ]
    )

    question_4 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="4. You chose to trade, you are blue, and only one other person chose to trade. "
              "The red player is not trading Your earnings are:",
        choices=[
            [1, "59 points"],
            [0, "More than 59 points"],
            [0, "60 points"],
        ]
    )

    question_5 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="5. You chose to trade, you are red, and only one other person chose to trade. "
              "The Decision Maker said YES. Your earnings are:",
        choices=[
            [0, "59 points"],
            [0, "159 points"],
            [1, "109 points"],
        ]
    )

    question_6 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="6. You chose not to trade, you are blue, and the other two persons chose to trade. "
              "The Decision Maker voted NO.",
        choices=[
            [0, "The red player earns 159 points"],
            [0, "You earn 60 points"],
            [1, "You earn 60 points and, if you are the decision maker, "
                "you also earn 25 points from the reduced bonus."],
        ]
    )

    question_7 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="7. No one chose to trade and YES is the Decision Maker's choice. You all earn:",
        choices=[
            [0, "58 points"],
            [1, "60 points"],
            [0, "60 points and the red player earns additional 100 bonus points"],
        ]
    )

    question_8 = models.IntegerField(
        widget=widgets.RadioSelect,
        label="8. Everyone chose to trade and YES is the choice. "
              "Here, everyone completes 2 trades and everyone earns",
        choices=[
            [0, "58 points"],
            [0, "60 points"],
            [1, "58 points and the red player earns additional 100 bonus points"],
        ]
    )


# PAGES
class Question1(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6',
                   'question_7', 'question_8']

    @staticmethod
    def error_message(player, values):
        if values['question_1'] != 1:
            return 'Please Check Your Answer For Question 1'
        if values['question_2'] != 1:
            return 'Please Check Your Answer For Question 2'
        if values['question_3'] != 1:
            return 'Please Check Your Answer For Question 3'
        if values['question_4'] != 1:
            return 'Please Check Your Answer For Question 4'
        if values['question_5'] != 1:
            return 'Please Check Your Answer For Question 5'
        if values['question_6'] != 1:
            return 'Please Check Your Answer For Question 6'
        if values['question_7'] != 1:
            return 'Please Check Your Answer For Question 7'
        if values['question_8'] != 1:
            return 'Please Check Your Answer For Question 8'

class Results(Page):
    pass


page_sequence = [Question1, Results]