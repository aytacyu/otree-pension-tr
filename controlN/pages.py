from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage, SurveyPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'round_number': '{}' .format(self.round_number)
        }


class SendBackWaitPage(WaitPage):
    pass


class P8(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2 """
    form_model = 'group'
    form_fields = ['sent_8' , 'expect_8']

    def is_displayed(self):
        return self.player.rol == 'P8'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + self.group.sent_5,
            'p5_decider': Constants.endowment_Decider - self.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + self.group.sent_6,
            'p6_decider': Constants.endowment_Decider - self.group.sent_6,
            'p6_receiver': Constants.endowment_Receiver + self.group.sent_7,
            'p7_decider': Constants.endowment_Decider - self.group.sent_7
        }


class P7(Page):
    """This page is only for P7"""
    form_model = 'group'
    form_fields = ['sent_7' , 'expect_7']

    def is_displayed(self):
        return self.player.rol == 'P7'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + self.group.sent_5,
            'p5_decider': Constants.endowment_Decider - self.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + self.group.sent_6,
            'p6_decider': Constants.endowment_Decider - self.group.sent_6
        }

class P6(Page):
    """This page is only for P6"""

    form_model = 'group'
    form_fields = ['sent_6' , 'expect_6']

    def is_displayed(self):
        return self.player.rol == 'P6'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
         'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + self.group.sent_5,
            'p5_decider': Constants.endowment_Decider - self.group.sent_5
        }


class P5(Page):
    """This page is only for P7"""
    form_model = 'group'
    form_fields = ['sent_5' , 'expect_5']

    def is_displayed(self):
        return self.player.rol == 'P5'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4
        }


class P4(Page):
    """This page is only for P4"""

    form_model = 'group'
    form_fields = ['sent_4', 'expect_4']

    def is_displayed(self):
        return self.player.rol == 'P4'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3

        }


class P3(Page):
    """This page is only for P3"""
    form_model = 'group'
    form_fields = ['sent_3' , 'expect_3' ]


    def is_displayed(self):
        return self.player.rol == 'P3'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2),
            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2
        }


class P2(Page):
    """This page is only for P2"""

    form_model = 'group'
    form_fields = ['sent_2' , 'expect_2' ]

    def is_displayed(self):
        return self.player.rol == 'P2'

    def vars_for_template(self):

        return {
            'prompt': '0 ile {} arasında bir sayı giriniz'.format(Constants.endowment_Decider-2)

        }


class P1(Page):
    """This page is only for P4"""

    def is_displayed(self):
        return self.player.rol == 'P1'

    def vars_for_template(self):

        return {

        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {

            'p2_transfer': self.group.sent_2,
            'p3_transfer': self.group.sent_3,
            'p4_transfer': self.group.sent_4,
            'p5_transfer': self.group.sent_5,
            'p6_transfer': self.group.sent_6,
            'p7_transfer': self.group.sent_7,
            'p8_transfer': self.group.sent_8,

            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + self.group.sent_5,
            'p5_decider': Constants.endowment_Decider - self.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + self.group.sent_6,
            'p6_decider': Constants.endowment_Decider - self.group.sent_6,
            'p6_receiver': Constants.endowment_Receiver + self.group.sent_7,
            'p7_decider': Constants.endowment_Decider - self.group.sent_7,
            'p7_receiver': Constants.endowment_Receiver + self.group.sent_8,
            'p8_decider': Constants.endowment_Decider - self.group.sent_8,

            'p1.payoff': self.group.set_payoffs(),
            'p2.payoff': self.group.set_payoffs(),
            'p3.payoff': self.group.set_payoffs(),
            'p4.payoff': self.group.set_payoffs(),
            'p5.payoff': self.group.set_payoffs(),
            'p6.payoff': self.group.set_payoffs(),
            'p7.payoff': self.group.set_payoffs(),
            'p8.payoff': self.group.set_payoffs(),
        }


'''
                'p2.payoff' : (Constants.endowment_Decider - self.sent_2) * (Constants.endowment_Receiver + self.sent_3) ,
                'p3.payoff' : (Constants.endowment_Decider - self.sent_3) * (Constants.endowment_Receiver + self.sent_4), 
          
            p4.payoff = (Constants.endowment_Decider - self.sent_4) * (Constants.endowment_Receiver + self.sent_5)
    
            p5.payoff = (Constants.endowment_Decider - self.sent_5) * (Constants.endowment_Receiver + self.sent_6)
    
        
            p6.payoff = (Constants.endowment_Decider - self.sent_6) * (Constants.endowment_Receiver + self.sent_7)
    
        
            p7.payoff = (Constants.endowment_Decider - self.sent_7) * (Constants.endowment_Receiver + self.sent_8)
    
        
            p8.payoff = (Constants.endowment_Decider - self.sent_8) * (
                        self.sent_2 + self.sent_3 + self.sent_4 + self.sent_5 + self.sent_6
'''



class OverallResults(Page):
    """This page displays the earnings of each player"""

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        return {
            'overall_earnings': cumulative_payoff
        }


class Survey(SurveyPage):
    """This page displays the questionnaire for each player"""

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['Alan', 'Yaş', 'Cinsiyet', 'Aylık_ortalama_gelir',
                   'Yatırım_seçenekleri_seçimi',
                   'Yatırım_seçenekleri_seçimi2',
                   'Yatırım_seçenekleri_seçimi3',
                   'Yatırım_seçenekleri_seçimi4',
                   'Yatırım_seçenekleri_seçimi5',
                   'Yatırım_seçenekleri_seçimi6',
                   'Yatırım_seçenekleri_seçimi7',
                   'Yatırım_seçenekleri_seçimi8',
                   'Yatırım_seçenekleri_seçimi9',
                   'Yatırım_seçenekleri_seçimi10'
                   ]


page_sequence = [


    Introduction,
    P1,
    SendBackWaitPage,
    P2,
    SendBackWaitPage,
    P3,
    SendBackWaitPage,
    P4,
    SendBackWaitPage,
    P5,
    SendBackWaitPage,
    P6,
    SendBackWaitPage,
    P7,
    SendBackWaitPage,
    P8,
    ResultsWaitPage,
    Results,
    OverallResults,
    Survey

]
"""SendBackWaitPage,"""
"""P5,
    P4,
    P3,
    P2,
    P1,"""
