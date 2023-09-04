from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cbdc_extended'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 18
    A_ROLE = 'the Red Player'
    B_ROLE = 'A Blue Trader'
    C_ROLE = 'a Blue Trader'
    D_ROLE = 'a Blue Trader'
    E_ROLE = 'a Blue Trader'
    F_ROLE = 'a Blue Trader'
    TradeValue = 29
    NullTrade = 30
    TradeBonus = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    Participation_Count = models.IntegerField()
    Outcome = models.StringField()


class Player(BasePlayer):
    value = models.FloatField()

    trade = models.BooleanField(
        label="Would you like to Trade?",
        choices=
        [[True, "Yes"], [False, "No"]],
    )

    vote = models.BooleanField(
        label="You are the Decision Maker. Do you want to assign the trade bonus to the Red Player?",
        choices=
        [[True, "Yes"], [False, "No"]],
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    session = subsession.session
    if subsession.round_number >= 0:
        subsession.group_randomly()


# PAGES
class Waiting(WaitPage):
    pass


class Chat1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Chat2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 5

    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Chat3(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 9

    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Chat4(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 13

    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Chat5(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 17

    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Participate(Page):
    form_model = 'player'
    form_fields = ['trade']


class PWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        participation_count = 0
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        player3 = player_list[2]
        player4 = player_list[3]
        player5 = player_list[4]
        player6 = player_list[5]
        players = [player1, player2, player3, player4, player5, player6]
        for p in players:
            if p.trade:
                participation_count += 1
        group.Participation_Count = participation_count
        if player1.trade:
            player1.payoff = (int(participation_count - 1) * ((int(C.TradeValue)) + int(C.TradeBonus))) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player1.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player2.trade:
            player2.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player2.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player3.trade:
            player3.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player3.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player4.trade:
            player4.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player4.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player5.trade:
            player5.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player5.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player6.trade:
            player6.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player6.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)


class Vote(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        if player.role == C.B_ROLE:
            return ['vote']
        else:
            pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        dm = group.get_player_by_role(C.B_ROLE)
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        players = [player1, player2, ]
        if player1.trade:
            if not player2.vote:
                bonus = (int(group.Participation_Count - 1) * int(C.TradeBonus))
                player1.payoff -= int(bonus)
                player2.payoff += int(bonus)/2
                group.Outcome = 'Not Awarded'
            else:
                group.Outcome = 'Awarded'
        else:
            if not player2.vote:
                group.Outcome = 'Not Awarded'
            else:
                group.Outcome = 'Awarded'




class Results(Page):
    pass


page_sequence = [Waiting, Chat1, Chat2, Chat3, Chat4, Chat5, Participate, PWaitPage, Vote,
                 ResultsWaitPage, Results]
