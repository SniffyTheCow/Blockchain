from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'exit_survey_CB'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    survey_gender = models.StringField(
        label="What is your sex",
    )
    survey_age = models.IntegerField(
        label="What is your age",
    )

    survey_preference = models.IntegerField(
        label="Which Validation Method did you Prefer?",
        choices=[
            [1, "Method 1"], [2, "Method 2"],
        ],
        widget = widgets.RadioSelect
    )

    survey_comment = models.StringField(
        label="If you have any comments, please make them in the box below."

    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['survey_gender', 'survey_age', 'survey_comment']


class Results(Page):
    pass


page_sequence = [MyPage, Results]
