from configobj import ConfigObj
import matplotlib
matplotlib.use('Qt5Agg')
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