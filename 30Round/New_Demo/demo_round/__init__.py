from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Round_1'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    A_ROLE = 'the Red Trader'
    B_ROLE = 'a Blue Trader'
    C_ROLE = 'a Blue Trader'
    TradeValue = 29
    NullTrade = 30
    TradeBonus = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    Participation_Count = models.IntegerField()
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()


class Player(BasePlayer):
    value = models.FloatField()

    trade = models.BooleanField(
        label="Would you like to Trade?",
        choices=[
            [True, "Yes"],
            [False, "No"]
        ]
    )

    vote = models.BooleanField(
        label="Would you assign the bonus as proposed by the computer?",
        choices=[
            [True, "Yes"],
            [False, "No"]
        ]
    )


# PAGES
class Participate(Page):
    form_model = 'player'
    form_fields = ['trade']

    @staticmethod
    def error_message(player, values):
        if values['trade'] == False:
            return 'Please select another option.'



class PWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        participation_count = 0
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        player3 = player_list[2]
        players = [player1, player2, player3]
        for p in players:
            if p.trade:
                participation_count += 1
        group.Participation_Count = participation_count
        if player1.trade:
            player1.payoff = (int(participation_count) - 1) * (int(C.TradeValue) + int(C.TradeBonus)) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player1.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player2.trade:
            player2.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player2.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player3.trade:
            player3.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player3.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)


class Vote(Page):
    form_model = 'player'
    form_fields = ['vote']

    @staticmethod
    def error_message(player, values):
        if values['vote'] == True:
            return 'Please select another option.'


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        vote_count = 0
        participation_count = 0
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        player3 = player_list[2]
        players = [player1, player2, player3]
        for p in players:
            if p.vote:
                vote_count += 1
        group.yes_votes = vote_count
        group.no_votes = 3 - vote_count
        for p in players:
            if p.trade:
                participation_count += 1
        bonus = (int(participation_count - 1) * int(C.TradeBonus))
        if vote_count < 2:
            share = bonus / int(3 - vote_count)
            if player1.trade:
                player1.payoff -= bonus
                if player1.vote:
                    player1.payoff += 0
                else:
                    player1.payoff += int(share) / 2
            else:
                player1.payoff += 0
            if player2.vote:
                pass
            else:
                player2.payoff += int(share) / 2
            if player3.vote:
                pass
            else:
                player3.payoff += int(share) / 2
        else:
            pass


class Results(Page):
    pass


class fin(Page):
    pass


page_sequence = [Participate, PWaitPage, Vote, ResultsWaitPage, Results, fin]