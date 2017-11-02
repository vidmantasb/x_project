from unittest import TestCase
from testing.test_engine import init_table
import os
os.chdir('C:\\Users\\vidmantas\\Documents\\PROJECTS\\POKER\\CODE\\x_projectt')


t1, p1, gui_signals1, h1, logger1 = init_table(
    'testing/screenshots_ps_real_money/322098970_PreFlop_0.png', strategy='vid_ps_3_real_money')


class PokerTestCase(TestCase):
    def setUp(self):
        self.t, self.p, self.gui_signals, self.h, self.logger = init_table('testing/screenshots_ps_real_money/269141380_Flop_0.png',strategy='vid_ps_3_real_money')
        self.t1, self.p1, self.gui_signals1, self.h1, self.logger1 = init_table('testing/screenshots_ps_real_money/322098970_PreFlop_0.png', strategy='vid_ps_3_real_money')

class TestTableScreen(PokerTestCase):

    def test_my_cards_found(self):
        self.assertEqual(self.t.my_cards_found,True)

        self.assertEqual(self.t1.my_cards_found,True)

    def test_my_cards(self):
        self.assertEqual(sorted(self.t.mycards),sorted(['KS', 'JS']))

        self.assertEqual(sorted(self.t1.mycards),sorted(['7S', '7D']))

    def test_table_cards_found(self):
        self.assertEqual(self.t.table_cards_found,True)

        self.assertEqual(self.t1.table_cards_found,True)

    def test_table_cards(self):
        self.assertEqual(sorted(self.t.cardsOnTable),sorted(['6H', 'TH', '6C']))

        self.assertEqual(self.t1.cardsOnTable,[])

    def test_dealer_position_found(self):
        self.assertEqual(self.t.dealer_position_found,True)

        self.assertEqual(self.t1.dealer_position_found,True)

    def test_dealer_position(self):
        self.assertEqual(self.t.dealer_position,1)

        self.assertEqual(self.t1.dealer_position,0)

    def test_check_button_found(self):
        self.assertEqual(self.t.checkButton_found,True)

        self.assertEqual(self.t1.checkButton_found, False)

    def test_fast_fold_button_found(self):
        self.assertEqual(self.t.fast_fold_found,False)

        self.assertEqual(self.t1.fast_fold_found, False)

    def test_any_button_found(self):
        self.assertEqual(self.t.button_found,True)

        self.assertEqual(self.t1.button_found, True)

#    def test_round_number_found(self):
#        self.assertEqual(h.game_number_on_screen,"15,547,039,153")

#    def test_round_number(self):
#        self.assertEqual(h.game_number_on_screen,"15,547,039,153")

    def test_other_players_names_found(self):
        self.assertEqual(self.t.other_players_names_found,True)

        self.assertEqual(self.t1.other_players_names_found, True)

    def test_total_pot(self):
        self.assertEqual(self.t.totalPotValue,0.13)

        self.assertEqual(self.t1.totalPotValue, 0.09)

    def test_round_pot(self):
        self.assertEqual(self.t.round_pot_value,0.13)

        self.assertEqual(self.t1.round_pot_value,0)

    def test_other_active_players(self):
        self.assertEqual(self.t.other_active_players,1)

        self.assertEqual(self.t1.other_active_players,3)

    def test_playersAhead(self):
        self.assertEqual(self.t.playersAhead,0)

        self.assertEqual(self.t1.playersAhead, 2)

    def test_playersBehind(self):
        self.assertEqual(self.t.playersBehind,0)

        self.assertEqual(self.t1.playersBehind, 1)

    def test_isHeadsUp(self):
        self.assertEqual(self.t.isHeadsUp,True)

        self.assertEqual(self.t1.isHeadsUp,False)

    def test_call_button_found(self):
        self.assertEqual(self.t.callButton_found,False)

        self.assertEqual(self.t1.callButton_found,True)

    def test_bet_button_found(self):
        self.assertEqual(self.t.bet_button_found, True)

        self.assertEqual(self.t1.bet_button_found, True)

    def test_allInCallButton_found(self):
        self.assertEqual(self.t.allInCallButton_found,False)

        self.assertEqual(self.t1.allInCallButton_found, False)

    def test_currentCallValue(self):
        self.assertEqual(self.t.currentCallValue,0)

        self.assertEqual(self.t1.currentCallValue, 0.06)

    def test_currentBetValue(self):
        self.assertEqual(self.t.currentBetValue,0.02)

        self.assertEqual(self.t1.currentBetValue,0.1)

    def test_myFunds(self):
        self.assertEqual(self.t.myFunds,1.32)

        self.assertEqual(self.t1.myFunds, 1.0)

    def test_botpot(self):
        self.assertEqual(self.t.bot_pot,0)

        self.assertEqual(self.t1.bot_pot, 0)


    def test_lost_everything_found(self):
        self.assertEqual(self.t.lost_everything_found,False)

        self.assertEqual(self.t1.lost_everything_found, False)

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