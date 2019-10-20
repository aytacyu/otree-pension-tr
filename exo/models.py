from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools

doc = """
This is a standard 2-player control game where the amount sent by player 1 gets
tripled. The control game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'exo'
    players_per_group = 8
    num_rounds = 10

    instructions_template = 'exo/instructions.html'
    table_template = 'exo/table.html'

    # Initial amount allocated to players+
    endowment_Decider = c(9)
    endowment_Receiver = c(1)
    multiplier = 1



class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.color = random.choice(['RED', 'BLUE']);
        else:
            for p in self.get_players():
                p.color = p.in_round(self.round_number - 1).color

        self.group_randomly()
        rol_lst = ['P2', 'P3', 'P4', 'P5', 'P6', 'P7']
        for p in self.get_players():
            round = self.round_number if self.round_number <= 8 else self.round_number - 8
            if p.id_in_subsession == round:
                p.rol = 'P1'
            elif p.id_in_subsession == (9 - round):
                p.rol = 'P8'
            else:
                random.shuffle(rol_lst)
                p.rol = rol_lst.pop(0)
        for p in self.get_players():
            print('P{0}:{1}'.format(p.id_in_subsession, p.rol))
        print('---------------')

"""    def creating_session(self):
        self.group_randomly()

"""

class Group(BaseGroup):

    sent_2 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    expect_2 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_3 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P3""",
    )
    expect_3 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_4 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P4""",
            )
    expect_4 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_5 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P5""",
    )
    expect_5 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_6 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P6""",
    )
    expect_6 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_7 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P7""",
    )
    expect_7 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    sent_8 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P8""",
    )
    expect_8 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P2""",
    )
    def set_payoffs(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)
        p6 = self.get_player_by_id(6)
        p7 = self.get_player_by_id(7)
        p8 = self.get_player_by_id(8)

        p1.payoff = 2 *( Constants.endowment_Receiver + self.sent_2)
        p2.payoff = (Constants.endowment_Decider - self.sent_2) *( Constants.endowment_Receiver + self.sent_3)
        p3.payoff = (Constants.endowment_Decider - self.sent_3) *( Constants.endowment_Receiver + self.sent_4)
        p4.payoff = (Constants.endowment_Decider - self.sent_4) *( Constants.endowment_Receiver + self.sent_5)
        p5.payoff = (Constants.endowment_Decider - self.sent_5) *( Constants.endowment_Receiver + self.sent_6)
        p6.payoff = (Constants.endowment_Decider - self.sent_6) *( Constants.endowment_Receiver + self.sent_7)
        p7.payoff = (Constants.endowment_Decider - self.sent_7) *( Constants.endowment_Receiver + self.sent_8)
        p8.payoff = (Constants.endowment_Decider - self.sent_8) *( ( Constants.endowment_Receiver + self.sent_2) + ( Constants.endowment_Receiver + self.sent_3) + ( Constants.endowment_Receiver + self.sent_4) + ( Constants.endowment_Receiver + self.sent_5) + ( Constants.endowment_Receiver + self.sent_6)+ ( Constants.endowment_Receiver + self.sent_7) + ( Constants.endowment_Receiver + self.sent_8)) / 7

"""        p8.payoff = (Constants.endowment_Decider - self.sent_8) *( self.sent_2 + self.sent_3 + self.sent_4 + self.sent_5 + self.sent_6 + self.sent_7 + self.sent_8) / 7
"""


class Player(BasePlayer):
    color = models.StringField()
    overall_payoff = models.CurrencyField(initial=0)

    # def role(self):
    #     return {1: 'P1', 2: 'P2', 3: 'P3', 4: 'P4', 5: 'P5', 6: 'P6', 7: 'P7', 8: 'P8'}[self.id_in_group]
    rol = models.StringField(initial='')
    Alan = models.StringField()

    Yaş = models.StringField(choices=['≤24', '25-34', '35-44', '45-54', '>55'], widget=widgets.RadioSelect)

    Cinsiyet = models.StringField(choices=['Kadın', 'Erkek'], widget=widgets.RadioSelect)

    Aylık_ortalama_gelir = models.StringField(widget=widgets.RadioSelect)

    def Aylık_ortalama_gelir_choices (self):
        choices = ['500-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+']
        return choices

    Yatırım_seçenekleri_seçimi = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi_choices(self):
        choices = ['%10 olasılıkla 8₺, %90 olasılıkla 6,4₺',
                   '%10 olasılıkla 15,4₺, %90 olasılıkla 0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi2 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi2_choices(self):
        choices = ['%20 olasılıkla 8₺, %80 olasılıkla 6,4₺',
                   '%20 olasılıkla 15,4₺, %80 olasılıkla 0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi3 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi3_choices(self):
        choices = ['%30 olasılıkla 8₺, %70 olasılıkla 6,4₺',
                   '%30 olasılıkla 15,4₺, %70 olasılıkla  0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi4 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi4_choices(self):
        choices = ['%40 olasılıkla 8₺, %60 olasılıkla 6,4₺',
                   '%40 olasılıkla 15,4₺, %60 olasılıkla 0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi5 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi5_choices(self):
        choices = ['%50 olasılıkla 8₺, %50 olasılıkla  6,4₺',
                   '%50 olasılıkla 15,4₺, %50 olasılıkla 0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi6 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi6_choices(self):
        choices = ['%60 olasılıkla 8₺, %40 olasılıkla  6,4₺',
                   '%60 olasılıkla 15,4₺, %40 olasılıkla  0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi7 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi7_choices(self):
        choices = ['%70 olasılıkla 8₺, %30 olasılıkla 6,4₺',
                   '%70 olasılıkla 15,4₺, %30 olasılıkla  0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi8 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi8_choices(self):
        choices = ['%80 olasılıkla 8₺, %20 olasılıkla 6,4₺',
                   '%80 olasılıkla 15,4₺, %20 olasılıkla  0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi9 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi9_choices(self):
        choices = ['%90 olasılıkla 8₺, %10 olasılıkla  6,4₺',
                   '%90 olasılıkla 15,4₺, %10 olasılıkla  0,4₺']
        return choices

    Yatırım_seçenekleri_seçimi10 = models.StringField(widget=widgets.RadioSelect)

    def Yatırım_seçenekleri_seçimi10_choices(self):
        choices = ['%100 olasılıkla 8₺, %0 olasılıkla  6,4₺',
                   '%100 olasılıkla 15,4₺, %0 olasılıkla 0,4₺']
        return choices
