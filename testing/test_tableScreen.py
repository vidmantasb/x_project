from unittest import TestCase
from testing.test_engine import init_table
import os
os.chdir('C:\\Users\\vidmantas\\Documents\\PROJECTS\\POKER\\CODE\\x_projectt')

#t, p, gui_signals, h, logger = init_table('testing/screenshots_ps_real_money/813577545_River_0.png', strategy='vid_ps_3_real_money')


class PokerTestCase(TestCase):
    def setUp(self):
        self.t, self.p, self.gui_signals, self.h, self.logger = init_table('testing/screenshots_ps_real_money/269141380_Flop_0.png',strategy='vid_ps_3_real_money')
        self.t1, self.p1, self.gui_signals1, self.h1, self.logger1 = init_table('testing/screenshots_ps_real_money/322098970_PreFlop_0.png', strategy='vid_ps_3_real_money')
        self.t2, self.p2, self.gui_signals2, self.h2, self.logger2 = init_table('testing/screenshots_ps_real_money/9455534_PreFlop_1.png', strategy='vid_ps_3_real_money')

        self.t31, self.p31, self.gui_signals31, self.h31, self.logger31 = init_table('testing/screenshots_ps_real_money/813577545_PreFlop_0.png', strategy='vid_ps_3_real_money')
        self.t32, self.p32, self.gui_signals32, self.h32, self.logger32 = init_table('testing/screenshots_ps_real_money/813577545_Flop_0.png', strategy='vid_ps_3_real_money')
        self.t33, self.p33, self.gui_signals33, self.h33, self.logger33 = init_table('testing/screenshots_ps_real_money/813577545_Flop_1.png', strategy='vid_ps_3_real_money')
        self.t34, self.p34, self.gui_signals34, self.h34, self.logger34 = init_table('testing/screenshots_ps_real_money/813577545_Turn_0.png', strategy='vid_ps_3_real_money')
        self.t35, self.p35, self.gui_signals35, self.h35, self.logger35 = init_table('testing/screenshots_ps_real_money/813577545_River_0.png', strategy='vid_ps_3_real_money')

class TestTableScreen(PokerTestCase):

    def test_my_cards_found(self):
        self.assertEqual(self.t.my_cards_found,True)
        self.assertEqual(self.t1.my_cards_found,True)
        self.assertEqual(self.t2.my_cards_found,True)

        self.assertEqual(self.t31.my_cards_found, True)
        self.assertEqual(self.t32.my_cards_found, True)
        self.assertEqual(self.t33.my_cards_found, True)
        self.assertEqual(self.t34.my_cards_found, True)
        self.assertEqual(self.t35.my_cards_found, True)

    def test_my_cards(self):
        self.assertEqual(sorted(self.t.mycards),sorted(['KS', 'JS']))
        self.assertEqual(sorted(self.t1.mycards),sorted(['7S', '7D']))
        self.assertEqual(sorted(self.t2.mycards),sorted(['JS', 'AH']))

        self.assertEqual(sorted(self.t31.mycards),sorted(['6C', '4C']))
        self.assertEqual(sorted(self.t32.mycards),sorted(['6C', '4C']))
        self.assertEqual(sorted(self.t33.mycards),sorted(['6C', '4C']))
        self.assertEqual(sorted(self.t34.mycards),sorted(['6C', '4C']))
        self.assertEqual(sorted(self.t35.mycards),sorted(['6C', '4C']))

    def test_table_cards_found(self):
        self.assertEqual(self.t.table_cards_found,True)
        self.assertEqual(self.t1.table_cards_found,True)
        self.assertEqual(self.t2.table_cards_found,True)

        self.assertEqual(self.t31.table_cards_found,True)
        self.assertEqual(self.t32.table_cards_found,True)
        self.assertEqual(self.t33.table_cards_found,True)
        self.assertEqual(self.t34.table_cards_found,True)
        self.assertEqual(self.t35.table_cards_found,True)


    def test_table_cards(self):
        self.assertEqual(sorted(self.t.cardsOnTable),sorted(['6H', 'TH', '6C']))
        self.assertEqual(self.t1.cardsOnTable,[])
        self.assertEqual(self.t2.cardsOnTable,[])

        self.assertEqual(sorted(self.t31.cardsOnTable),sorted([]))
        self.assertEqual(sorted(self.t32.cardsOnTable),sorted(['2C', '7C', '2H']))
        self.assertEqual(sorted(self.t33.cardsOnTable),sorted(['2C', '7C', '2H']))
        self.assertEqual(sorted(self.t34.cardsOnTable),sorted(['2C', '7C', 'TD', '2H']))
        self.assertEqual(sorted(self.t35.cardsOnTable),sorted(['2C', 'AD', '7C', 'TD', '2H']))

    def test_dealer_position_found(self):
        self.assertEqual(self.t.dealer_position_found,True)
        self.assertEqual(self.t1.dealer_position_found,True)
        self.assertEqual(self.t2.dealer_position_found,True)

        self.assertEqual(self.t31.dealer_position_found,True)
        self.assertEqual(self.t32.dealer_position_found,True)
        self.assertEqual(self.t33.dealer_position_found,True)
        self.assertEqual(self.t34.dealer_position_found,True)
        self.assertEqual(self.t35.dealer_position_found,True)

    def test_dealer_position(self):
        self.assertEqual(self.t.dealer_position,1)
        self.assertEqual(self.t1.dealer_position,0)
        self.assertEqual(self.t2.dealer_position,1)

        self.assertEqual(self.t31.dealer_position,4)
        self.assertEqual(self.t32.dealer_position,4)
        self.assertEqual(self.t33.dealer_position,4)
        self.assertEqual(self.t34.dealer_position,4)
        self.assertEqual(self.t35.dealer_position,4)


    def test_check_button_found(self):
        self.assertEqual(self.t.checkButton_found, True)
        self.assertEqual(self.t1.checkButton_found, False)
        self.assertEqual(self.t2.checkButton_found, False)

        self.assertEqual(self.t31.checkButton_found, False)
        self.assertEqual(self.t32.checkButton_found, True)
        self.assertEqual(self.t33.checkButton_found, False)
        self.assertEqual(self.t34.checkButton_found, True)
        self.assertEqual(self.t35.checkButton_found, True)


    def test_fast_fold_button_found(self):
        self.assertEqual(self.t.fast_fold_found, False)
        self.assertEqual(self.t1.fast_fold_found, False)
        self.assertEqual(self.t2.fast_fold_found, False)

        self.assertEqual(self.t31.fast_fold_found, False)
        self.assertEqual(self.t32.fast_fold_found, False)
        self.assertEqual(self.t33.fast_fold_found, False)
        self.assertEqual(self.t34.fast_fold_found, False)
        self.assertEqual(self.t35.fast_fold_found, False)

    def test_any_button_found(self):
        self.assertEqual(self.t.button_found, True)
        self.assertEqual(self.t1.button_found, True)
        self.assertEqual(self.t2.button_found, True)

        self.assertEqual(self.t31.button_found, True)
        self.assertEqual(self.t32.button_found, True)
        self.assertEqual(self.t33.button_found, True)
        self.assertEqual(self.t34.button_found, True)
        self.assertEqual(self.t35.button_found, True)


#    def test_round_number_found(self):
#        self.assertEqual(h.game_number_on_screen,"15,547,039,153")

#    def test_round_number(self):
#        self.assertEqual(h.game_number_on_screen,"15,547,039,153")

    def test_other_players_names_found(self):
        self.assertEqual(self.t.other_players_names_found, True)
        self.assertEqual(self.t1.other_players_names_found, True)
        self.assertEqual(self.t2.other_players_names_found, True)

        self.assertEqual(self.t31.other_players_names_found, True)
        self.assertEqual(self.t32.other_players_names_found, True)
        self.assertEqual(self.t33.other_players_names_found, True)
        self.assertEqual(self.t34.other_players_names_found, True)
        self.assertEqual(self.t35.other_players_names_found, True)

    def test_total_pot(self):
        self.assertEqual(self.t.totalPotValue, 0.13)
        self.assertEqual(self.t1.totalPotValue, 0.09)
        self.assertEqual(self.t2.totalPotValue, 1.02)

        self.assertEqual(self.t31.totalPotValue, 0.07)
        self.assertEqual(self.t32.totalPotValue, 0.09)
        self.assertEqual(self.t33.totalPotValue, 0.13)
        self.assertEqual(self.t34.totalPotValue, 0.16)
        self.assertEqual(self.t35.totalPotValue, 0.16)


    def test_round_pot(self):
        self.assertEqual(self.t.round_pot_value,0.13)
        self.assertEqual(self.t1.round_pot_value,0)
        self.assertEqual(self.t2.round_pot_value,0)

        self.assertEqual(self.t31.round_pot_value,0)
        self.assertEqual(self.t32.round_pot_value,0.09)
        self.assertEqual(self.t33.round_pot_value,0.09)
        self.assertEqual(self.t34.round_pot_value,0.16)
        self.assertEqual(self.t35.round_pot_value,0.16)


    def test_other_active_players(self):
        self.assertEqual(self.t.other_active_players,1)
        self.assertEqual(self.t1.other_active_players,3)
        self.assertEqual(self.t2.other_active_players,1)

        self.assertEqual(self.t31.other_active_players,1)
        self.assertEqual(self.t32.other_active_players,1)
        self.assertEqual(self.t33.other_active_players,1)
        self.assertEqual(self.t34.other_active_players,1)
        self.assertEqual(self.t35.other_active_players,1)

    def test_playersAhead(self):
        self.assertEqual(self.t.playersAhead, 0)
        self.assertEqual(self.t1.playersAhead, 2)
        self.assertEqual(self.t2.playersAhead, 0)

        self.assertEqual(self.t31.playersAhead, 1)
        self.assertEqual(self.t32.playersAhead, 1)
        self.assertEqual(self.t33.playersAhead, 1)
        self.assertEqual(self.t34.playersAhead, 1)
        self.assertEqual(self.t35.playersAhead, 1)



    def test_playersBehind(self):
        self.assertEqual(self.t.playersBehind, 0)
        self.assertEqual(self.t1.playersBehind, 1)
        self.assertEqual(self.t2.playersBehind, 1)

        self.assertEqual(self.t31.playersBehind, 0)
        self.assertEqual(self.t32.playersBehind, 0)
        self.assertEqual(self.t33.playersBehind, 0)
        self.assertEqual(self.t34.playersBehind, 0)
        self.assertEqual(self.t35.playersBehind, 0)


    def test_isHeadsUp(self):
        self.assertEqual(self.t.isHeadsUp,True)
        self.assertEqual(self.t1.isHeadsUp,False)
        self.assertEqual(self.t2.isHeadsUp,True)

        self.assertEqual(self.t31.isHeadsUp,True)
        self.assertEqual(self.t32.isHeadsUp,True)
        self.assertEqual(self.t33.isHeadsUp,True)
        self.assertEqual(self.t34.isHeadsUp,True)
        self.assertEqual(self.t35.isHeadsUp,True)


    def test_call_button_found(self):
        self.assertEqual(self.t.callButton_found,False)
        self.assertEqual(self.t1.callButton_found,True)
        self.assertEqual(self.t2.callButton_found,True)

        self.assertEqual(self.t31.callButton_found,True)
        self.assertEqual(self.t32.callButton_found,False)
        self.assertEqual(self.t33.callButton_found,True)
        self.assertEqual(self.t34.callButton_found,False)
        self.assertEqual(self.t35.callButton_found,False)


    def test_bet_button_found(self):
        self.assertEqual(self.t.bet_button_found, True)
        self.assertEqual(self.t1.bet_button_found, True)
        self.assertEqual(self.t2.bet_button_found, False)

        self.assertEqual(self.t31.bet_button_found, True)
        self.assertEqual(self.t32.bet_button_found, True)
        self.assertEqual(self.t33.bet_button_found, True)
        self.assertEqual(self.t34.bet_button_found, True)
        self.assertEqual(self.t35.bet_button_found, True)

    def test_allInCallButton_found(self):
        self.assertEqual(self.t.allInCallButton_found, False)
        self.assertEqual(self.t1.allInCallButton_found, False)
        self.assertEqual(self.t2.allInCallButton_found, True)

        self.assertEqual(self.t31.allInCallButton_found, False)
        self.assertEqual(self.t32.allInCallButton_found, False)
        self.assertEqual(self.t33.allInCallButton_found, False)
        self.assertEqual(self.t34.allInCallButton_found, False)
        self.assertEqual(self.t35.allInCallButton_found, False)


    def test_currentCallValue(self):
        self.assertEqual(self.t.currentCallValue, 0)
        self.assertEqual(self.t1.currentCallValue, 0.06)
        self.assertEqual(self.t2.currentCallValue, 0.47)

        self.assertEqual(self.t31.currentCallValue, 0.02)
        self.assertEqual(self.t32.currentCallValue, 0)
        self.assertEqual(self.t33.currentCallValue, 0.04)
        self.assertEqual(self.t34.currentCallValue, 0)
        self.assertEqual(self.t35.currentCallValue, 0)


    def test_currentBetValue(self):
        self.assertEqual(self.t.currentBetValue,0.02)
        self.assertEqual(self.t1.currentBetValue,0.1)
        self.assertEqual(self.t2.currentBetValue,9999999)

        self.assertEqual(self.t31.currentBetValue,0.06)
        self.assertEqual(self.t32.currentBetValue,0.02)
        self.assertEqual(self.t33.currentBetValue,0.08)
        self.assertEqual(self.t34.currentBetValue,0.02)
        self.assertEqual(self.t35.currentBetValue,0.02)


    def test_myFunds(self):
        self.assertEqual(self.t.myFunds, 1.32)
        self.assertEqual(self.t1.myFunds, 1.0)
        self.assertEqual(self.t2.myFunds, 0.47)

        self.assertEqual(self.t31.myFunds, 0.42)
        self.assertEqual(self.t32.myFunds, 0.4)
        self.assertEqual(self.t33.myFunds, 0.4)
        self.assertEqual(self.t34.myFunds, 0.36)
        self.assertEqual(self.t35.myFunds, 0.36)


    def test_botpot(self):
        self.assertEqual(self.t.bot_pot, 0)
        self.assertEqual(self.t1.bot_pot, 0)
        self.assertEqual(self.t2.bot_pot, 0.24)

        self.assertEqual(self.t31.bot_pot, 0.02)
        self.assertEqual(self.t32.bot_pot, 0)
        self.assertEqual(self.t33.bot_pot, 0)
        self.assertEqual(self.t34.bot_pot, 0)
        self.assertEqual(self.t35.bot_pot, 0)

    def test_lost_everything_found(self):
        self.assertEqual(self.t.lost_everything_found, False)
        self.assertEqual(self.t1.lost_everything_found, False)
        self.assertEqual(self.t2.lost_everything_found, False)

        self.assertEqual(self.t31.lost_everything_found, False)
        self.assertEqual(self.t32.lost_everything_found, False)
        self.assertEqual(self.t33.lost_everything_found, False)
        self.assertEqual(self.t34.lost_everything_found, False)
        self.assertEqual(self.t35.lost_everything_found, False)

    def test_players_funds(self):
        self.assertEqual(self.t.other_players[0]['funds'], 4.31)
        self.assertEqual(self.t.other_players[1]['funds'], 2.23)
        self.assertEqual(self.t.other_players[2]['funds'], 2.44)
        self.assertEqual(self.t.other_players[3]['funds'], 2.09)
        self.assertEqual(self.t.other_players[4]['funds'], 2.09)

        self.assertEqual(self.t1.other_players[0]['funds'], 0.91)
        self.assertEqual(self.t1.other_players[1]['funds'], 1.98)
        self.assertEqual(self.t1.other_players[2]['funds'], 4.0)
        self.assertEqual(self.t1.other_players[3]['funds'], 2.17)
        self.assertEqual(self.t1.other_players[4]['funds'], 1.94)

        self.assertEqual(self.t2.other_players[0]['funds'], 4.07)
        self.assertEqual(self.t2.other_players[1]['funds'], 3.39)
        self.assertEqual(self.t2.other_players[2]['funds'], 2.70)
        self.assertEqual(self.t2.other_players[3]['funds'], 0.62)
        self.assertEqual(self.t2.other_players[4]['funds'], 3.74)



        self.assertEqual(self.t31.other_players[0]['funds'], 0.4)
        self.assertEqual(self.t31.other_players[1]['funds'], 2)
        self.assertEqual(self.t31.other_players[2]['funds'], 1.91)
        self.assertEqual(self.t31.other_players[3]['funds'], 2.36)
        self.assertEqual(self.t31.other_players[4]['funds'], 0.41)

        self.assertEqual(self.t32.other_players[0]['funds'], 0.4)
        self.assertEqual(self.t32.other_players[1]['funds'], 2)
        self.assertEqual(self.t32.other_players[2]['funds'], 1.91)
        self.assertEqual(self.t32.other_players[3]['funds'], 2.36)
        self.assertEqual(self.t32.other_players[4]['funds'], 0.41)

        self.assertEqual(self.t33.other_players[0]['funds'], 0.36)
        self.assertEqual(self.t33.other_players[1]['funds'], 2)
        self.assertEqual(self.t33.other_players[2]['funds'], 1.91)
        self.assertEqual(self.t33.other_players[3]['funds'], 2.36)
        self.assertEqual(self.t33.other_players[4]['funds'], 0.41)

        self.assertEqual(self.t34.other_players[0]['funds'], 0.36)
        self.assertEqual(self.t34.other_players[1]['funds'], 2)
        self.assertEqual(self.t34.other_players[2]['funds'], 1.91)
        self.assertEqual(self.t34.other_players[3]['funds'], 2.36)
        self.assertEqual(self.t34.other_players[4]['funds'], 0.41)

        self.assertEqual(self.t35.other_players[0]['funds'], 0.36)
        self.assertEqual(self.t35.other_players[1]['funds'], 2)
        self.assertEqual(self.t35.other_players[2]['funds'], 1.91)
        self.assertEqual(self.t35.other_players[3]['funds'], 2.36)
        self.assertEqual(self.t35.other_players[4]['funds'], 0.41)

    def test_players_pots(self):
        self.assertEqual(self.t.other_players[0]['pot'], '')
        self.assertEqual(self.t.other_players[1]['pot'], '')
        self.assertEqual(self.t.other_players[2]['pot'], '')
        self.assertEqual(self.t.other_players[3]['pot'], '')
        self.assertEqual(self.t.other_players[4]['pot'], '')

        self.assertEqual(self.t1.other_players[0]['pot'], 0.01)
        self.assertEqual(self.t1.other_players[1]['pot'], 0.02)
        self.assertEqual(self.t1.other_players[2]['pot'], '')
        self.assertEqual(self.t1.other_players[3]['pot'], '')
        self.assertEqual(self.t1.other_players[4]['pot'], 0.06)

        self.assertEqual(self.t2.other_players[0]['pot'], '')
        self.assertEqual(self.t2.other_players[1]['pot'], 0.01)
        self.assertEqual(self.t2.other_players[2]['pot'], 0.02)
        self.assertEqual(self.t2.other_players[3]['pot'], 0.75)
        self.assertEqual(self.t2.other_players[4]['pot'], '')



        self.assertEqual(self.t31.other_players[0]['pot'], 0.04)
        self.assertEqual(self.t31.other_players[1]['pot'], '')
        self.assertEqual(self.t31.other_players[2]['pot'], '')
        self.assertEqual(self.t31.other_players[3]['pot'], '')
        self.assertEqual(self.t31.other_players[4]['pot'], 0.01)

        self.assertEqual(self.t32.other_players[0]['pot'], '')
        self.assertEqual(self.t32.other_players[1]['pot'], '')
        self.assertEqual(self.t32.other_players[2]['pot'], '')
        self.assertEqual(self.t32.other_players[3]['pot'], '')
        self.assertEqual(self.t32.other_players[4]['pot'], '')

        self.assertEqual(self.t33.other_players[0]['pot'], 0.04)
        self.assertEqual(self.t33.other_players[1]['pot'], '')
        self.assertEqual(self.t33.other_players[2]['pot'], '')
        self.assertEqual(self.t33.other_players[3]['pot'], '')
        self.assertEqual(self.t33.other_players[4]['pot'], '')

        self.assertEqual(self.t34.other_players[0]['pot'], '')
        self.assertEqual(self.t34.other_players[1]['pot'], '')
        self.assertEqual(self.t34.other_players[2]['pot'], '')
        self.assertEqual(self.t34.other_players[3]['pot'], '')
        self.assertEqual(self.t34.other_players[4]['pot'], '')

        self.assertEqual(self.t35.other_players[0]['pot'], '')
        self.assertEqual(self.t35.other_players[1]['pot'], '')
        self.assertEqual(self.t35.other_players[2]['pot'], '')
        self.assertEqual(self.t35.other_players[3]['pot'], '')
        self.assertEqual(self.t35.other_players[4]['pot'], '')

    def test_players_status(self):
        self.assertEqual(self.t.other_players[0]['status'], 0)
        self.assertEqual(self.t.other_players[1]['status'], 0)
        self.assertEqual(self.t.other_players[2]['status'], 1)
        self.assertEqual(self.t.other_players[3]['status'], 0)
        self.assertEqual(self.t.other_players[4]['status'], 0)

        self.assertEqual(self.t1.other_players[0]['status'], 1)
        self.assertEqual(self.t1.other_players[1]['status'], 1)
        self.assertEqual(self.t1.other_players[2]['status'], 0)
        self.assertEqual(self.t1.other_players[3]['status'], 0)
        self.assertEqual(self.t1.other_players[4]['status'], 1)

        self.assertEqual(self.t2.other_players[0]['status'], 0)
        self.assertEqual(self.t2.other_players[1]['status'], 0)
        self.assertEqual(self.t2.other_players[2]['status'], 0)
        self.assertEqual(self.t2.other_players[3]['status'], 1)
        self.assertEqual(self.t2.other_players[4]['status'], 0)



        self.assertEqual(self.t31.other_players[0]['status'], 1)
        self.assertEqual(self.t31.other_players[1]['status'], 0)
        self.assertEqual(self.t31.other_players[2]['status'], 0)
        self.assertEqual(self.t31.other_players[3]['status'], 0)
        self.assertEqual(self.t31.other_players[4]['status'], 0)

        self.assertEqual(self.t32.other_players[0]['status'], 1)
        self.assertEqual(self.t32.other_players[1]['status'], 0)
        self.assertEqual(self.t32.other_players[2]['status'], 0)
        self.assertEqual(self.t32.other_players[3]['status'], 0)
        self.assertEqual(self.t32.other_players[4]['status'], 0)

        self.assertEqual(self.t33.other_players[0]['status'], 1)
        self.assertEqual(self.t33.other_players[1]['status'], 0)
        self.assertEqual(self.t33.other_players[2]['status'], 0)
        self.assertEqual(self.t33.other_players[3]['status'], 0)
        self.assertEqual(self.t33.other_players[4]['status'], 0)

        self.assertEqual(self.t34.other_players[0]['status'], 1)
        self.assertEqual(self.t34.other_players[1]['status'], 0)
        self.assertEqual(self.t34.other_players[2]['status'], 0)
        self.assertEqual(self.t34.other_players[3]['status'], 0)
        self.assertEqual(self.t34.other_players[4]['status'], 0)

        self.assertEqual(self.t35.other_players[0]['status'], 1)
        self.assertEqual(self.t35.other_players[1]['status'], 0)
        self.assertEqual(self.t35.other_players[2]['status'], 0)
        self.assertEqual(self.t35.other_players[3]['status'], 0)
        self.assertEqual(self.t35.other_players[4]['status'], 0)