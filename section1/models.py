from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'section1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # control questions
    ctrl_p1_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("0", "male"),
                                                                                      ("1", "female")])
    ctrl_p1_qn_2_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                        ("2", 2),
                                                                                        ("3", 3),
                                                                                        ("4", 4),
                                                                                        ("5", 5),
                                                                                        ("6", 6),
                                                                                        ("7", 7),
                                                                                        ("8", 8),
                                                                                        ("9", 9),
                                                                                        ("10", 10)])

    ctrl_p1_qn_3_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                        ("2", 2),
                                                                                        ("3", 3),
                                                                                        ("4", 4),
                                                                                        ("5", 5),
                                                                                        ("6", 6),
                                                                                        ("7", 7),
                                                                                        ("8", 8),
                                                                                        ("9", 9),
                                                                                        ("10", 10)
                                                                                        ])

    ctrl_p5_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                        ("2", 2),
                                                                                        ("3", 3),
                                                                                        ("4", 4),
                                                                                        ("5", 5),
                                                                                        ("6", 6),
                                                                                        ("7", 7),
                                                                                        ("8", 8),
                                                                                        ("9", 9),
                                                                                        ])

    ctrl_p6_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                        ("2", 2),
                                                                                        ("3", 3),
                                                                                        ("4", 4),
                                                                                        ("5", 5),
                                                                                        ("6", 6),
                                                                                        ("7", 7),
                                                                                        ("8", 8),
                                                                                        ("9", 9),
                                                                                        ])

    ctrl_p7_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                        ("2", 2),
                                                                                        ("3", 3),
                                                                                        ("4", 4),
                                                                                        ("5", 5),
                                                                                        ("6", 6),
                                                                                        ("7", 7),
                                                                                        ("8", 8),
                                                                                        ("9", 9),
                                                                                        ])

    ctrl_p10_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p10_qn_2_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9)
                                                                                         ])

    ctrl_p10_qn_3_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_1_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_2_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_3_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_4_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_5_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p12_qn_6_1a = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=[("1", 1),
                                                                                         ("2", 2),
                                                                                         ("3", 3),
                                                                                         ("4", 4),
                                                                                         ("5", 5),
                                                                                         ("6", 6),
                                                                                         ("7", 7),
                                                                                         ("8", 8),
                                                                                         ("9", 9),
                                                                                         ])

    ctrl_p19_qn_1_1b = models.CharField(widget=widgets.RadioSelect(), choices=[("0", "GHC 8"),
                                                                               ("1", "GHC 0"),
                                                                               ("2", "GHC 4")
                                                                               ])

    ctrl_p19_qn_2_1b = models.CharField(widget=widgets.RadioSelect(), choices=[("7", "GHC 7"),
                                                                                  ("0", "GHC 0"),
                                                                                  ("5", "GHC 5")
                                                                                  ])

    ctrl_p19_qn_3_1b = models.CharField(widget=widgets.RadioSelect(), choices=[("7", "GHC 5"),
                                                                                  ("0", "GHC 0"),
                                                                                  ("5", "GHC 7 ")
                                                                                  ])

    ctrl_p21_qn_1_1b = models.IntegerField()

    # ctrl_p26_qn_1_1c = models.CharField(widget=widgets.RadioSelect(), choices=[("0", "GHC 8"),
    #                                                                            ("1", "GHC 0"),
    #                                                                            ("2", "GHC 4")
    #                                                                            ])
    #
    # ctrl_p26_qn_2_1c = models.IntegerField(widget=widgets.RadioSelect(), choices=[("7", "GHC 7"),
    #                                                                               ("0", "GHC 0"),
    #                                                                               ("5", "GHC 5")
    #                                                                               ])
    #
    # ctrl_p26_qn_3_1c = models.IntegerField(widget=widgets.RadioSelect(), choices=[("7", "GHC 7"),
    #                                                                               ("0", "GHC 0"),
    #                                                                               ("5", "GHC 5")
    #                                                                               ])
    #
    # ctrl_p26_qn_4_1c = models.IntegerField(widget=widgets.RadioSelect(), choices=[("7", "GHC 7"),
    #                                                                               ("0", "GHC 0"),
    #                                                                               ("5", "GHC 5")
    #                                                                               ])

    ctrl_p28_qn_1_1c = models.IntegerField()

    ctrl_p29_qn_1_1c = models.IntegerField()
