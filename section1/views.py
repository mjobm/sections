from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class P1(Page):
    form_model = models.Player
    form_fields = ["ctrl_p1_qn_1_1a", "ctrl_p1_qn_2_1a", "ctrl_p1_qn_3_1a"]

    def is_displayed(self):
        return True


class P2(Page):
    pass


class P3(Page):
    pass


class P4(Page):
    pass


class P5(Page):

    form_model = models.Player
    form_fields = ["ctrl_p5_qn_1_1a"]

    def is_displayed(self):
        return True


class P6(Page):

    form_model = models.Player
    form_fields = ["ctrl_p6_qn_1_1a"]

    def is_displayed(self):
        return True


class P7(Page):

    form_model = models.Player
    form_fields = ["ctrl_p7_qn_1_1a"]

    def is_displayed(self):
        return True


class P8(Page):
    pass


class P9(Page):
    pass


class P10(Page):

    form_model = models.Player
    form_fields = ["ctrl_p10_qn_1_1a", "ctrl_p10_qn_2_1a", "ctrl_p10_qn_3_1a"]

    def is_displayed(self):
        return True


class P11(Page):
    pass


class P12(Page):
    form_model = models.Player
    form_fields = ["ctrl_p12_qn_1_1a", "ctrl_p12_qn_2_1a",
                   "ctrl_p12_qn_3_1a", "ctrl_p12_qn_4_1a",
                   "ctrl_p12_qn_5_1a", "ctrl_p12_qn_6_1a"]

    def is_displayed(self):
        return True


class P13(Page):
    pass


class P14(Page):
    pass


class P15(Page):
    pass


class P16(Page):
    pass


class P17(Page):
    pass


class P18(Page):
    pass


class P19(Page):

    form_model = models.Player
    form_fields = ["ctrl_p19_qn_1_1b", "ctrl_p19_qn_2_1b", "ctrl_p19_qn_3_1b"]

    def is_displayed(self):
        return True


class P20(Page):
    pass


class P21(Page):

    form_model = models.Player
    form_fields = ["ctrl_p21_qn_1_1b"]

    def is_displayed(self):
        return True


class P22(Page):
    pass


class P23(Page):
    pass


class P24(Page):
    pass


class P25(Page):
    pass


class P26(Page):
    pass


class P27(Page):
    pass


class P28(Page):

    form_model = models.Player
    form_fields = ["ctrl_p28_qn_1_1c"]

    def is_displayed(self):
        return True


class P29(Page):
    form_model = models.Player
    form_fields = ["ctrl_p29_qn_1_1c"]

    def is_displayed(self):
        return True


class P30(Page):
    pass


class P31(Page):
    pass


class P32(Page):
    pass



page_sequence = [
    P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21,
    # P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, P42,
]
