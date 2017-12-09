
import inspect
import re
import cv2  # opencv 3.0
import numpy as np
from testing.test_engine import init_table
from PIL import Image, ImageFilter

#FOR TOTAL POT VALUE
t, p, gui_signals, h, logger = init_table('testing/screenshots_ps_real_money/9455534_PreFlop_1.png', strategy='vid_ps_3_real_money')
#t, p, gui_signals, h, logger = init_table('testing/screenshots_ps_real_money/269141380_Flop_0.png',strategy='vid_ps_3_real_money')
#t, p, gui_signals, h, logger = init_table('testing/screenshots_ps_real_money/322098970_PreFlop_0.png', strategy='vid_ps_3_real_money')
func_dict = t.coo['get_total_pot_value'][t.tbl]
#t.gui_signals.signal_progressbar_increase.emit(5)
#t.gui_signals.signal_status.emit("Get Pot Value")
#t.logger.debug("Get TotalPot value")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                            t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.show()

if t.tbl == 'PS':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.totalpot, img,
                                                                                        0.01)
    right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                             img, 0.01)
    count = (left_count > 0) & (right_count > 0)

    if count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 7, 2, right_points[0][0] + 4,
                                       pil_image.size[1] - 7)
        number_image.show()
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                   force_method=0)  # force_method was 1 before

        if not (value).is_integer():
            value = float(value)
    else:
        value = ''
elif t.tbl == 'PS2':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.totalpot, img,
                                                                                        0.01)
    right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                             img, 0.01)
    count = (left_count > 0) & (right_count > 0)

    if count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 7, 5, right_points[0][0] + 4,
                                       pil_image.size[1] - 5)
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                   force_method=0)  # force_method was 1 before

        if not (value).is_integer():
            value = float(str(value).replace('.', '')[0:(len(str(value)) - 1)])
    else:
        value = ''
else:
    value = t.get_ocr_float(pil_image, 'TotalPotValue', force_method=1)

try:
    if (not str(value) == '') & (t.tbl != 'PS2'):  # was not str(value)==''
        value = float(re.findall(r'\d{1,2}\.\d{1,2}', str(value))[0])
except:
    t.logger.warning("Total pot regex problem: " + str(value))
    value = ''
    t.logger.warning("unable to get pot value")
    t.gui_signals.signal_status.emit("Unable to get pot value")
    pil_image.save("pics/ErrPotValue.png")
    t.totalPotValue = h.previousPot

if value == '':
    t.totalPotValue = 0
else:
    t.totalPotValue = value


#ROUND POT VALUE
func_dict = t.coo['get_round_pot_value'][t.tbl]
#t.gui_signals.signal_progressbar_increase.emit(2)
#t.gui_signals.signal_status.emit("Get round pot value")
#t.logger.debug("Get round pot value")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

#pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + 282, t.tlc[1] + 265,
#                         t.tlc[0] + 435, t.tlc[1] + 285)

pil_image.show()
if t.tbl == 'PS':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.roundpot, img,
                                                                                        0.01)
    if left_count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 7, 3, 140,
                                       pil_image.size[1] - 2)
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                   force_method=0)  # force_method was 1 before

        if not (value).is_integer():
            value = float(value)
    else:
        value = ''
elif t.tbl == 'PS2':
    value = t.get_ocr_float(pil_image, 'RoundPotValue', force_method=0)  # force_method was 1 before
else:
    value = t.get_ocr_float(pil_image, 'RoundPotValue', force_method=1)

try:
    if (not str(value) == '') & (t.tbl != 'PS2'):  # was not str(value)==''
        value = float(re.findall(r'\d{1,2}\.\d{1,2}', str(value))[0])
except:
    t.logger.warning("Round pot regex problem: " + str(value))
    value = ''
    t.logger.warning("unable to get round pot value")
    t.gui_signals.signal_status.emit("Unable to get round pot value")
    pil_image.save("pics/ErrRoundPotValue.png")
    t.round_pot_value = h.previous_round_pot_value

if value == '':
    t.round_pot_value = 0
else:
    t.round_pot_value = value

#t.logger.info("Final round pot Value: " + str(t.round_pot_value))

#GET BET VALUE
func_dict = t.coo['get_current_bet_value'][t.tbl]
#t.gui_signals.signal_progressbar_increase.emit(5)
#t.gui_signals.signal_status.emit("Get Bet Value")
#t.logger.debug("Get bet value")

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

#pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + 676, t.tlc[1] + func_dict['y1'],
#                         t.tlc[0] + 760, t.tlc[1] + 535)


pil_image.show()

if t.tbl == 'PS':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.buttondollar, img,
                                                                                        0.01)
    if left_count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 8, 0, 90,
                                       pil_image.size[1] - 1)
        number_image.show()
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                   force_method=0)  # force_method was 1 before

        if not (value).is_integer():
            value = float(value)
    else:
else:
    t.currentBetValue = t.get_ocr_float(pil_image, 'BetValue')



if t.currentCallValue == '' and p.selected_strategy['pokerSite'][0:2] == "PS" and t.allInCallButton_found:
    t.logger.warning("Taking call value from button on the right")
    t.currentCallValue = t.currentBetValue
    t.currentBetValue = 9999999

if t.currentBetValue == '':
    t.logger.warning("No bet value")
    t.currentBetValue = 9999999.0

if t.currentCallValue == '':
    t.logger.error("Call Value was empty")
    if p.selected_strategy['pokerSite'][0:2] == "PS" and t.allInCallButton_found:
        t.currentCallValue = t.currentBetValue
        t.currentBetValue = 9999999
    try:
        t.entireScreenPIL.save('log/call_err_debug_fullscreen.png')
    except:
        pass

    t.currentCallValue = 9999999.0

if t.currentBetValue < t.currentCallValue:
    t.currentCallValue = t.currentBetValue / 2
    t.BetValueReadError = True
    t.entireScreenPIL.save("pics/BetValueError.png")

#t.logger.info("Final call value: " + str(t.currentCallValue))
#t.logger.info("Final bet value: " + str(t.currentBetValue))


#GET CALL VALUE
func_dict = t.coo['get_current_call_value'][t.tbl]
#t.gui_signals.signal_status.emit("Get Call value")
#t.gui_signals.signal_progressbar_increase.emit(5)

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.show()

if not t.checkButton:
    if t.tbl == 'PS':
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
        left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.buttondollar, img,
                                                                                         0.01)
        if left_count:
            number_image = t.crop_image(pil_image, left_points[0][0] + 8, 0, 90,
                                        pil_image.size[1] - 1)
            number_image.show()
            t.currentCallValue = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                    force_method=0)  # force_method was 1 before

            if not (t.currentCallValue).is_integer():
                t.currentCallValue = float(t.currentCallValue)
        else:
            t.currentCallValue = ''
    else:
        t.currentCallValue = t.get_ocr_float(pil_image, 'BetValue')
elif t.checkButton:
    t.currentCallValue = 0

if t.currentCallValue != '':
    t.getCallButtonValueSuccess = True
else:
    if p.selected_strategy['pokerSite'][0:2] != "PS":
        t.checkButton = True
    t.logger.debug("Assuming check button as call value is zero")
    try:
        pil_image.save("pics/ErrCallValue.png")
    except:
        pass

#GET MY FUNDS
func_dict = t.coo['get_my_funds'][t.tbl]
#t.gui_signals.signal_progressbar_increase.emit(5)
#t.logger.debug("Get my funds")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                            t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.show()
if t.tbl[0:2] == 'PP':
    basewidth = 200
    wpercent = (basewidth / float(pil_image.size[0]))
    hsize = int((float(pil_image.size[1]) * float(wpercent)))
    pil_image = pil_image.resize((basewidth, hsize), Image.ANTIALIAS)
elif t.tbl == 'PS':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count1, left_points1, left_bestfit1, left_minvalue1 = t.find_template_on_screen(t.buttondollarmyfund, img,
                                                                                     0.01)
    left_count2, left_points2, left_bestfit2, left_minvalue2 = t.find_template_on_screen(t.buttondollarmyfund1, img,
                                                                                     0.01)

    if left_count1>0:
        left_count = left_count1
        left_points = left_points1
    elif left_count2>0:
        left_count = left_count2
        left_points = left_points2

    if left_count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 8, 0, 90,
                                    pil_image.size[1] - 1)

        t.myFunds = t.get_ocr_float(number_image, 'MyFunds')
        if not (t.myFunds).is_integer():
            t.myFunds = float(t.myFunds)
    else:
        t.myFunds = ''
else:
    pil_image_filtered = pil_image.filter(ImageFilter.ModeFilter)
    pil_image_filtered2 = pil_image.filter(ImageFilter.MedianFilter)
    t.myFunds = t.get_ocr_float(pil_image, 'MyFunds')
    if t.myFunds == '':
        t.myFunds = t.get_ocr_float(pil_image_filtered, 'MyFunds')
    if t.myFunds == '':
        t.myFunds = t.get_ocr_float(pil_image_filtered2, 'MyFunds')

t.myFundsError = False
if t.myFunds == '':
    t.myFundsError = True
    t.myFunds = float(h.myFundsHistory[-1])
    t.logger.info("myFunds not regognised!")
    t.gui_signals.signal_status.emit("Funds NOT recognised")
    t.logger.warning("Funds NOT recognised. See pics/FundsError.png to see why.")
    t.entireScreenPIL.save("pics/FundsError.png")
    time.sleep(0.5)
t.logger.debug("Funds: " + str(t.myFunds))


#GET PLAYER FUND
func_dict = t.coo['get_other_player_funds'][t.tbl]
t.gui_signals.signal_status.emit("Get player funds")
for i, fd in enumerate(func_dict, start=0):
    t.gui_signals.signal_progressbar_increase.emit(1)
    pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                t.tlc[0] + fd[2], t.tlc[1] + fd[3])
    pil_image.show()
    if t.tbl == 'PS':
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
        left_count1, left_points1, left_bestfit1, left_minvalue1 = t.find_template_on_screen(t.buttondollarplayerfund1, img,
                                                                                     0.02)
        left_count2, left_points2, left_bestfit2, left_minvalue2 = t.find_template_on_screen(t.buttondollarplayerfund2, img,
                                                                                     0.02)
        if left_count1>0:
            left_points = left_points1
            number_image = t.crop_image(pil_image, left_points[0][0] + 8, 0, 90,
                                        pil_image.size[1] - 1)
            im = number_image.convert('RGBA')

            number_array = np.array(im)  # "data" is a height x width x 4 numpy array
            red, green, blue, alpha = number_array.T  # Temporarily unpack the bands for readability

            # Replace white with red... (leaves alpha values alone...)
            white_areas = (red > 60) & (blue > 60) & (green > 60)
            number_array[..., :-1][white_areas.T] = (255, 255, 255)  # Transpose back needed

            number_image = Image.fromarray(number_array)
            value = t.get_ocr_float(number_image, 'MyFunds')

        elif left_count2>0:
            left_points = left_points2
            number_image = t.crop_image(pil_image, left_points[0][0] + 8, 0, 90,
                                        pil_image.size[1] - 1)
            value = t.get_ocr_float(number_image, 'MyFunds')
        else:
            value = ''
    else:
        value = t.get_ocr_float(pil_image, str(inspect.stack()[0][3]), replace_black_white=False)
        if not value == '':
            if not (value).is_integer():
                value = float(str(value).replace('.', '')[0:(len(str(value)) - 1)])

    value = float(value) if value != '' else ''
    t.other_players[i]['funds'] = value


#GET PLAYERS POTS
func_dict = t.coo['get_other_player_pots'][t.tbl]
t.gui_signals.signal_status.emit("Get player pots")
for n in range(5):
    fd = func_dict[n]
    pot_area_image = t.crop_image(t.entireScreenPIL, t.tlc[0] - 20 + fd[0], t.tlc[1] + fd[1] - 20,
                                  t.tlc[0] + fd[2] + 50, t.tlc[1] + fd[3] + 20)
    img = cv2.cvtColor(np.array(pot_area_image), cv2.COLOR_BGR2RGB)
    if t.tbl == 'PS':
        left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.roundpot, img,
                                                                                         0.01)
        right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                              img, 0.01)
        exist_pot = (right_count > 0) & (left_count > 0)
    elif t.tbl == 'PS2':
        left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.leftpot, img,
                                                                                         0.01)
        right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                              img, 0.01)
        exist_pot = (right_count > 0) & (left_count > 0)
    else:
        count, points, bestfit, minvalue = t.find_template_on_screen(t.smallDollarSign1, img,
                                                                     float(func_dict[5]))
        exist_pot = count > 0

    if exist_pot:
        if t.tbl == 'PS':
            pil_image = t.crop_image(pot_area_image, left_points[0][0]+7, 15,
                                     right_points[0][0] + 8, pot_area_image.size[1] - 15)
            method = func_dict[6]
            value = t.get_ocr_float(pil_image, str(inspect.stack()[0][3]), force_method=method)
        elif t.tbl == 'PS2':
            pil_image = t.crop_image(pot_area_image, left_points[0][0], 15,
                                     right_points[0][0] + 8, pot_area_image.size[1] - 15)
            method = func_dict[6]
            value = t.get_ocr_float(pil_image, str(inspect.stack()[0][3]), force_method=method)
        else:
            pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                     t.tlc[0] + fd[2], t.tlc[1] + fd[3])
            method = func_dict[6]
            value = t.get_ocr_float(pil_image, str(inspect.stack()[0][3]), force_method=method)
            try:
                if not str(value) == '':
                    value = re.findall(r'\d{1}\.\d{1,2}', str(value))[0]
            except:
                t.logger.warning("Player pot regex problem: " + str(value))
                value = ''

        value = float(value) if value != '' else ''
        t.logger.debug("FINAL POT after regex: " + str(value))
        t.other_players[n]['pot'] = value








func_dict = t.coo['get_total_pot_value'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.gui_signals.signal_status.emit("Get Pot Value")
t.logger.debug("Get TotalPot value")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                            t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

if t.tbl == 'PS':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.totalpot, img,
                                                                                        0.01)
    right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                             img, 0.01)
    count = (left_count > 0) & (right_count > 0)

    if count:
        number_image = t.crop_image(pil_image, left_points[0][0] + 7, 2, right_points[0][0] + 4,
                                       pil_image.size[1] - 7)
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]),
                                   force_method=0)  # force_method was 1 before

        if not (value).is_integer():
            value = float(value)
    else:
        value = ''
elif t.tbl =='PS2':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.totalpot, img,
                                                                                        0.01)
    right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                             img, 0.01)
    count = (left_count>0) & (right_count>0)

    if count:
        number_image = t.crop_image(pil_image,  left_points[0][0] + 7, 5, right_points[0][0]+4, pil_image.size[1]-5)
        value = t.get_ocr_float(number_image, str(inspect.stack()[0][3]), force_method=0) # force_method was 1 before

        if not (value).is_integer():
            value = float(str(value).replace('.', '')[0:(len(str(value)) - 1)])
    else:
        value = ''
else:
    value = t.get_ocr_float(pil_image, 'TotalPotValue', force_method=1)

    try:
        if (not str(value)=='')&(t.tbl !='PS2'): #was not str(value)==''
            value = float(re.findall(r'\d{1,2}\.\d{1,2}', str(value))[0])
    except:
        t.logger.warning("Total pot regex problem: " + str(value))
        value = ''
        t.logger.warning("unable to get pot value")
        t.gui_signals.signal_status.emit("Unable to get pot value")
        pil_image.save("pics/ErrPotValue.png")
        t.totalPotValue = h.previousPot

if value == '':
    t.totalPotValue = 0
else:
    t.totalPotValue = value
