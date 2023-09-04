from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Round_55A'
    PLAYERS_PER_GROUP = 6
    NUM_ROUNDS = 1
    A_ROLE = 'a Blue Trader'
    B_ROLE = 'a Blue Trader'
    C_ROLE = 'a Blue Trader'
    D_ROLE = 'a Blue Trader'
    E_ROLE = 'the Red Trader'
    F_ROLE = 'a Blue Trader'
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
        choices=
        [[True, "Yes"], [False, "No"]],
    )

    vote = models.BooleanField(
        label="Do you want to assign the bonus as proposed by the computer?",
        choices=
        [[True, "Yes"], [False, "No"]],
    )


# PAGES
class Waiting(WaitPage):
    pass


class chat(Page):
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
        if player5.trade:
            player5.payoff = (int(participation_count - 1) * ((int(C.TradeValue)) + int(C.TradeBonus))) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player5.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
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
        if player1.trade:
            player1.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player1.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player6.trade:
            player6.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(6 - participation_count) * int(C.NullTrade))
        else:
            player6.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)


class Vote(Page):
    form_model = 'player'
    form_fields = ['vote']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        vote_count = 0
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
            if p.vote:
                vote_count += 1
        group.yes_votes = vote_count
        group.no_votes = 6 - vote_count
        for p in players:
            if p.trade:
                participation_count += 1
        if player5.trade:
            bonus = (int(participation_count - 1) * int(C.TradeBonus))
        else:
            bonus = 0
        if vote_count < 3:
            if player5.trade:
                player5.payoff -= bonus
                if player2.vote:
                    if player3.vote:
                        if player4.vote:
                            if player1.vote:
                                if player6.vote:
                                    pass
                                else:
                                    player6.payoff += int(bonus) / 2
                            else:
                                player1.payoff += int(bonus) / 2
                        else:
                            player4.payoff += int(bonus) / 2
                    else:
                        player3.payoff += int(bonus) / 2
                else:
                    player2.payoff += int(bonus) / 2
            else:
                player5.payoff += 0
        else:
            pass


class Results(Page):
    pass


page_sequence = [Waiting, chat, Participate, PWaitPage, Vote, ResultsWaitPage, Results]