from unittest import TestCase
from unittest.mock import MagicMock
import numpy as np
from tools.mouse_mover import *

from decisionmaker.decisionmaker import Decision
from decisionmaker.decisionmaker import DecisionTypes
from tools.mongo_manager import StrategyHandler

from testing.test_engine import init_table
from decisionmaker.current_hand_memory import History, CurrentHandPreflopState
from gui.gui_qt_ui import Ui_Pokerbot
from decisionmaker.montecarlo_python import run_montecarlo_wrapper


#t, p, gui_signals, h, logger = init_table('testing/screenshots/751235173_PreFlop_0.png')
#t, p, gui_signals, h, logger = init_table('testing/screenshots/ps_7.png')
t, p, gui_signals, h, logger = init_table('testing/screenshots/ps_20.png')
#t, p, gui_signals, h, logger = init_table('pics/old/error.png')


p = StrategyHandler()
#p.current_strategy = 'pokemon'
p.current_strategy = 'vid_ps_2'
p.read_strategy('vid_ps_2')
#p.read_strategy('pokemon')
mouse = MouseMoverTableBased(p.selected_strategy['pokerSite'])
p.selected_strategy['gather_player_names'] = 1
h.game_number_on_screen = '1'

ready = t.check_for_captcha(mouse) and \
t.get_lost_everything(h, t, p, gui_signals) and \
t.check_for_imback(mouse) and \
t.get_my_cards(h) and \
t.get_table_cards(h) and \
t.upload_collusion_wrapper(p, h) and \
t.get_dealer_position() and \
t.get_snowie_advice(p, h) and \
t.check_fast_fold(h, p, mouse) and \
t.check_for_button() and \
t.get_round_number(h) and \
t.init_get_other_players_info() and \
t.get_other_player_names(p) and \
t.get_other_player_funds(p) and \
t.get_other_player_pots() and \
t.get_total_pot_value(h) and \
t.get_round_pot_value(h) and \
t.check_for_checkbutton() and \
t.get_other_player_status(p, h) and \
t.check_for_call() and \
t.check_for_betbutton() and \
t.check_for_allincall() and \
t.get_current_call_value(p) and \
t.get_current_bet_value(p)

print('ready :', ready)


#p.current_strategy = 'vid_ps_2'
l = MagicMock()
#t.abs_equity = 0.7
#t.checkButton = True

preflop_state = CurrentHandPreflopState()
config = ConfigObj("config.ini")
ui = Ui_Pokerbot()

#t.isHeadsUp = True
#t.gameStage = "Flop"
#p.selected_strategy['FlopBluffMinEquity'] = 0.3
#p.selected_strategy['FlopBluff'] = "1"

m = run_montecarlo_wrapper(p, gui_signals, config, ui, t, t.game_logger, preflop_state, h)
d = Decision(t, h, p, l)
d.make_decision(t, h, p, logger, t.game_logger)



#d.decision = DecisionTypes.check
#t.playersAhead = 0
#d.bluff(t, p, h)
#t.check_for_allincall()







print('lost everything found :',t.lost_everything_found)
print('imback_found :',t.imback_found)
print('my_cards_found :',t.my_cards_found)
print('table_cards_found :',t.table_cards_found)
print('dealer_position_found :',t.dealer_position_found)
print('fast_fold_found :',t.fast_fold_found)
print('button_found :',t.button_found)
print('other_players_names_found :',t.other_players_names_found)
for i in range(t.other_players.__len__()):
    print('player :',i,', name :', t.other_players[i]['name'],', funds :', t.other_players[i]['funds'], ' pot :',t.other_players[i]['pot'], ' status :', t.other_players[i]['status'])

print('totalPotValue :',t.totalPotValue)
print('round_pot_value :',t.round_pot_value)
print('checkButton_found :',t.checkButton_found)
print('other_active_players :',t.other_active_players)
print('playersAhead :',t.playersAhead)
print('isHeadsUp :',t.isHeadsUp)
print('first_raiser :',t.first_raiser)
print('second_raiser :',t.second_raiser)
print('first_caller :',t.first_caller)
print('first_raiser_utg :',t.first_raiser_utg)
print('second_raiser_utg :',t.second_raiser_utg)
print('first_caller_utg :',t.first_caller_utg)
print('other_player_has_initiative :',t.other_player_has_initiative)
print('callButton_found :',t.callButton_found)
print('bet_button_found :',t.bet_button_found)
print('allInCallButton_found :',t.allInCallButton_found)
print('currentCallValue :',t.currentCallValue)
print('currentBetValue :',t.currentBetValue)
print('myFunds :',t.myFunds)
print('botpot :',t.get_bot_pot(p))
d.decision

#Testing mouse movements
from tools.mouse_mover import *
['Imback',
'Fold', 'Check',
'Call', 'Bet',
'BetPlus',
'Bet half pot',
'Bet pot',
'Bet Bluff',
'Call Deception',
'Check Deception']

mouse_target = 'Bet pot'
m_coor = mouse.coo[mouse_target][0]
topleftcorner=t.tlc
tlx = int(topleftcorner[0])
tly = int(topleftcorner[1])
action =mouse.coo[mouse_target][0]
#[1, 0.3, 592, 436, 30, 12]
#action[2] = 670
#action[3] = 436
number_image = t.crop_image(t.entireScreenPIL,  action[2]+ tlx,
                            action[3] + tly,
                            action[2] + tlx + action[4],action[3]+ tly + action[5])
number_image.show()
action =mouse.coo[mouse_target][1]
number_image = t.crop_image(t.entireScreenPIL,  action[2]+ tlx,
                            action[3] + tly,
                            action[2] + tlx + action[4],action[3]+ tly + action[5])
number_image.show()




