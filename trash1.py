def crop_image(original, left, top, right, bottom):
    # original.show()
    width, height = original.size  # Get dimensions
    cropped_example = original.crop((left, top, right, bottom))
    # cropped_example.show()
    return cropped_example


def find_template_on_screen( template, screenshot, threshold):
    # 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    method = eval('cv2.TM_SQDIFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(screenshot, template, method)
    loc = np.where(res <= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        bestFit = min_loc
    else:
        bestFit = max_loc

    count = 0
    points = []
    for pt in zip(*loc[::-1]):
        # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        count += 1
        points.append(pt)
    # plt.subplot(121),plt.imshow(res)
    # plt.subplot(122),plt.imshow(img,cmap = 'jet')
    # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    # plt.show()
    return count, points, bestFit, min_val


coordinates_file='coordinates.txt'
with open(coordinates_file, 'r') as inf:
        c = eval(inf.read())
        coo = c['screen_scraping']

from PIL import Image
import cv2
import numpy as np
from table_analysers.base import Table
from table_analysers import table_screen_based
a=TableScreenBased()

image_part = 'get_my_cards'
file = 'pics/table.png'
new_file = 'pics/old/part.png'
entireScreenPIL = Image.open(file)
tlc = (561,104)
fd = coo[image_part]['PS2']
try:
    pil_image = crop_image(entireScreenPIL, tlc[0] + fd[0], tlc[1] + fd[1], tlc[0] + fd[2],
                                        tlc[1] + fd[3])
except:
    pil_image = crop_image(entireScreenPIL, tlc[0] + fd['x1'], tlc[1] + fd['y1'],
                                        tlc[0] + fd['x2'], tlc[1] + fd['y2'])

pil_image.save(new_file,'png')
t.entireScreenPIL.save(new_file,'png')
name = "pics/" + 'PS' + "/betbutton.png"
template = Image.open(name)
img_1 = cv2.cvtColor(np.array(template), cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)

find_template_on_screen(img_1, img, 0.01)


t.entireScreenPIL =entireScreenPIL


t.entireScreenPIL.save(new_file,'png')

t.check_for_captcha(mouse) and \
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


def check_for_allincall(t):
    func_dict = t.coo['check_for_allincall'][t.tbl]
    t.logger.debug("Check for All in call button")
    pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                                t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])
    # Convert RGB to BGR
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    count, points, bestfit, _ = t.find_template_on_screen(t.allInCallButton, img, 0.01)
    if count > 0:
        t.allInCallButton = True
        t.logger.debug("All in call button found")
    else:
        t.allInCallButton = False
        t.logger.debug("All in call button not found")

    if not t.bet_button_found:
        t.allInCallButton = True
        t.logger.debug("Assume all in call because there is no bet button")

    return True


def get_dealer_position(t):
    func_dict = t.coo['get_dealer_position'][t.tbl]
    t.gui_signals.signal_progressbar_increase.emit(5)
    pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + 0, t.tlc[1] + 0,
                             t.tlc[0] + 950, t.tlc[1] + 700)

    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    count, points, bestfit, _ = t.find_template_on_screen(t.dealer, img, 0.05)
    try:
        point = points[0]
    except:
        t.logger.debug("No dealer found")
        return False

    t.position_utg_plus = ''
    for n, fd in enumerate(func_dict, start=0):
        if point[0] > fd[0] and point[1] > fd[1] and point[0] < fd[2] and point[1] < fd[3]:
            t.position_utg_plus = n
            t.dealer_position = (9 - n) % 6  # 0 is myt, 1 is player to the left
            t.logger.info('Bot position is UTG+' + str(t.position_utg_plus))  # 0 mean bot is UTG

    if t.position_utg_plus == '':
        t.position_utg_plus = 0
        t.dealer_position = 3
        t.logger.error('Could not determine dealer position. Assuming UTG')
    else:
        t.logger.info('Dealer position (0 is myt and 1 is next player): ' + str(t.dealer_position))

    t.big_blind_position_abs_all = (t.dealer_position + 2) % 6  # 0 is myt, 1 is player to my left
    t.big_blind_position_abs_op = t.big_blind_position_abs_all - 1

    return True

file = 'tests/screenshots/751235173_PreFlop_0.png'
strategy = 'Pokemon'
import cv2
img = cv2.cvtColor(np.array(t.entireScreenPIL), cv2.COLOR_BGR2RGB)
t.find_template_on_screen(t.topLeftCorner, img, 0.01)


func_dict = t.coo['get_current_call_value'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.gui_signals.signal_status.emit("Get Bet Value")
t.logger.debug("Get bet value")

func_dict['x1'] = 548
func_dict['x2'] = 606

{'x1': 568, 'x2': 626, 'y1': 518, 'y2': 533}

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.save(new_file,'png')
t.currentBetValue = t.get_ocr_float(pil_image, 'BetValue')




func_dict = t.coo['get_round_pot_value'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(2)
t.gui_signals.signal_status.emit("Get round pot value")
t.logger.debug("Get round pot value")

{'x1': 402, 'x2': 435, 'y1': 154, 'y2': 168}
func_dict['x1'] = 390
func_dict['x2'] = 435
func_dict['y1'] = 150
func_dict['y2'] = 172

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

new_file = 'pics/old/part.png'
pil_image.save(new_file,'png')

value = t.get_ocr_float(pil_image, 'TotalPotValue', 0)
import re
try:
    if not str(value) == '':
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

func_dict = t.coo['check_for_betbutton'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.logger.debug("Check for betbutton")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
count, points, bestfit, _ = t.find_template_on_screen(t.betbutton, img, func_dict['tolerance'])



func_dict = t.coo['get_my_funds'][t.tbl]
t.logger.debug("Check for All in call button")
Out[7]: {'x1': 405, 'x2': 460, 'y1': 408, 'y2': 420}

func_dict['x1'] = 385
func_dict['x2'] = 450
func_dict['y1'] = 406
func_dict['y2'] = 622
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])
# Convert RGB to BGR
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
count, points, bestfit, _ = t.find_template_on_screen(t.allInCallButton, img, 0.01)



fd = t.coo['get_bot_pot'][t.tbl]
fd = (300,300,435,313)


430 -408
import cv2

pil_image_1 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1]-10, t.tlc[0] + fd[2],
                         t.tlc[1] + fd[3]+10)

img = cv2.cvtColor(np.array(pil_image_1), cv2.COLOR_BGR2RGB)
count_1, points_1, bestfit_1, _ = t.find_template_on_screen(t.zero_bot_pot, img, 0.01)

pil_image_2 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[0]+points_1[0][0]+9,
                         t.tlc[1] + fd[3])

pil_image_3 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[2]-44,
                         t.tlc[1] + fd[3])

pil_image_4 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[2]-66,
                         t.tlc[1] + fd[3])
pil_image_5 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[2]-88,
                         t.tlc[1] + fd[3])



value_1 = t.get_ocr_float(pil_image_1, str('get_bot_pot'), force_method=0)
value_2 = t.get_ocr_float(pil_image_2, str('get_bot_pot'), force_method=0)
value_3 = t.get_ocr_float(pil_image_3, str('get_bot_pot'), force_method=0)
value_4 = t.get_ocr_float(pil_image_4, str('get_bot_pot'), force_method=0)
value_5 = t.get_ocr_float(pil_image_5, str('get_bot_pot'), force_method=0)

if value_1<110:
    value = value_1
elif value_4<100|value_4<



import numpy
from PIL import Image
a = numpy.array(pil_image_1)
a = Image.fromarray(a)
a.show()

value = t.get_ocr_float(pil_image, str('get_bot_pot'), force_method=0)
try:
    value = float(re.findall(r'\d{1}\.\d{1,2}', str(value))[0])
except:
    t.logger.debug("Assuming bot pot is 0")
    value = 0
t.bot_pot = value
return value


import Image

def find_rgb(img, r_query, g_query, b_query):
    rgb = img.convert('RGB')
    for x in range(img.size[0]):
       for y in range(img.size[1]):
           r, g, b, = rgb.getpixel((x, y))
           if r == r_query and g == g_query and b == b_query:
               return (x,y)

print(find_rgb(pil_image, 15, 54, 30))
18,54,30

pil_image = t.crop_image(pil_image, 0, 0, 25,13)


def binarize_array(image, threshold=200):
    """Binarize a numpy array."""
    numpy_array = np.array(image)
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return Image.fromarray(numpy_array)

binarize_array(pil_image)
a = numpy.array(pil_image)
image=pil_image
a[:,:,0] = (a[:,:,0]>2)&(a[:,:,0]<25)*0
a[:,:,1] = (a[:,:,1]>73)&(a[:,:,1]<105)*0
a[:,:,2] = (a[:,:,2]>27)&(a[:,:,2]<49)*0

a[:,:,0] *=0
a[:,:,1] *=0
a[:,:,2] *=0

a = numpy.array(pil_image)
threshold = 5
a[:,:,0] =(a[:,:,0]>threshold)*255
#a[:,:,0] =(a[:,:,0]<=threshold)*0
a[:,:,1] =(a[:,:,1]>threshold)*255
#a[:,:,1] =(a[:,:,1]<=threshold)*0
a[:,:,2] =(a[:,:,2]>threshold)*255
#a[:,:,2] =(a[:,:,2]<=threshold)*0
a[:,:,0] = a[:,:,2]
a[:,:,1] = a[:,:,2]
a[:,:,2] = a[:,:,2]
a = Image.fromarray(a)
a.show()

t.get_ocr_float(a, str('get_bot_pot'), force_method=0)



func_dict = t.coo['check_for_call'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.logger.debug("Check for Call")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
count, points, bestfit, _ = t.find_template_on_screen(t.call, img, func_dict['tolerance'])
if count > 0:
    t.callButton_found = True
    t.callButton = True
    t.logger.debug("Call button found")
else:
    t.callButton_found = False
    t.callButton = False
    t.logger.info("Call button NOT found")
    pil_image.save("pics/debug_nocall.png")



func_dict = t.coo['get_current_call_value'][t.tbl]
t.gui_signals.signal_status.emit("Get Call value")
t.gui_signals.signal_progressbar_increase.emit(5)

Out[27]: {'x1': 548, 'x2': 606, 'y1': 518, 'y2': 533}

func_dict['x1'] = 550
func_dict['x2'] = 610
func_dict['y1'] = 518
func_dict['y2'] = 536

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])


pil_image = Image.open('pics/old/ocr_debug_BetValue.png')
pil_image = replace_black_white_colors(pil_image)

pil_image.show()


import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = pil_image
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)


t.get_ocr_float(img, 'CallValue',force_method=0)

image_file = pil_image
image_file = image_file.convert('1')

image_file.show()

t.get_ocr_float(image_file, 'CallValue',force_method=0)

if not t.checkButton:
    t.currentCallValue = t.get_ocr_float(pil_image, 'CallValue',force_method=0)
elif t.checkButton:
    t.currentCallValue = 0

if t.currentCallValue != '':
    t.getCallButtonValueSuccess = True
else:
    t.checkButton = True
    t.logger.debug("Assuming check button as call value is zero")
    try:
        pil_image.save("pics/ErrCallValue.png")
    except:
        pass



from PIL import Image
from scipy.misc import imsave
import numpy


def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


threshold =150
new_file = 'pics/old/part.png'
image_file =pil_image
image = image_file.convert('L')  # convert image to monochrome
image = numpy.array(image)
image = binarize_array(image, threshold)



def replace_black_white_colors(image_file, threshold =150):
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    image = (image == 0) * 255
    return Image.fromarray(image)

image = (image==0)*255
imsave(new_file, image)

img = Image.open(new_file)
img.show()

t.get_ocr_float(img, 'CallValue',force_method=0)
binarize

img_orig = pil_image
basewidth = 300
wpercent = (basewidth / float(img_orig.size[0]))
hsize = int((float(img_orig.size[1]) * float(wpercent)))
img_resized = img_orig.convert('L').resize((basewidth, hsize), Image.ANTIALIAS)
imp = binarize_array(img_resized)
imp.show()
def binarize_array(image, threshold=200):
    """Binarize a numpy array."""
    numpy_array = np.array(image)
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    numpy_array = (numpy_array == 0) * 255
    return Image.fromarray(numpy_array)

t.tbl ='PS2'
func_dict = t.coo['get_round_pot_value'][t.tbl]
func_dict1 = t.coo['get_round_pot_value'][t.tbl]
get_round_pot_value
Out[18]: {'x1': 390, 'x2': 435, 'y1': 150, 'y2': 172}
func_dict['x1'] = 380
func_dict['x2'] = 440
func_dict['y1'] = 268
func_dict['y2'] = 287

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.show()
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
count, points, bestfit, _ = t.find_template_on_screen(t.totalpot, img, 0.01)
if count == 1:
   start_points = points[0]
   number_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1']+start_points[0]+5, t.tlc[1] + func_dict['y1']+start_points[1],
                            t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2']-start_points[1])

number_image.show()

value = t.get_ocr_float(number_image, 'TotalPotValue', force_method=0)


value = t.get_ocr_float(pil_image, 'TotalPotValue', force_method=0)
pil_image.show()

func_dict = t.coo['get_other_player_pots'][t.tbl]
t.gui_signals.signal_status.emit("Get player pots")
for n in range(5):
    n=4
    fd = func_dict[n]
    t.gui_signals.signal_progressbar_increase.emit(1)
    pot_area_image = t.crop_image(t.entireScreenPIL, t.tlc[0] - 20 + fd[0], t.tlc[1] + fd[1] - 20,
                                  t.tlc[0] + fd[2] + 20, t.tlc[1] + fd[3] + 20)
    pot_area_image.show()
    img = cv2.cvtColor(np.array(pot_area_image), cv2.COLOR_BGR2RGB)
    count, points, bestfit, minvalue = t.find_template_on_screen(t.smallDollarSign1, img,
                                                                 float(func_dict[5]))
    has_small_dollarsign = count > 0
    if has_small_dollarsign:
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

fd = t.coo['get_bot_pot'][t.tbl]
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[2],
                         t.tlc[1] + fd[3])
try:
    if t.tbl == 'PS2':
        pil_image_1 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1]-10, t.tlc[0] + fd[2],
                                   t.tlc[1] + fd[3]+10)
        img = cv2.cvtColor(np.array(pil_image_1), cv2.COLOR_BGR2RGB)
        count_1, points_1, bestfit_1, _ = t.find_template_on_screen(t.rightpot, img, 0.01)
        pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                 t.tlc[0] + fd[0] + points_1[0][0],
                                 t.tlc[1] + fd[3])
        value = t.get_ocr_float(pil_image, 'get_bot_pot', force_method=0)

fd = t.coo['get_bot_pot'][t.tbl]
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1], t.tlc[0] + fd[2],
                         t.tlc[1] + fd[3])
try:
    if t.tbl == 'PS2':
        pil_image_1 = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1] - 10, t.tlc[0] + fd[2],
                                   t.tlc[1] + fd[3] + 10)
        img = cv2.cvtColor(np.array(pil_image_1), cv2.COLOR_BGR2RGB)
        count_1, points_1, bestfit_1, _ = t.find_template_on_screen(t.rightpot, img, 0.01)
        pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                 t.tlc[0] + fd[0] + points_1[0][0],
                                 t.tlc[1] + fd[3])
        value = t.get_ocr_float(pil_image, str(inspect.stack()[0][3]), force_method=0)



func_dict = t.coo['get_other_player_funds'][t.tbl]
for i, fd in enumerate(func_dict, start=0):
    i=3
    fd = func_dict[i]
    [691, 310, 743, 326]
    fd[0] = 686
    fd[1] = 305
    fd[2] = 748
    fd[3] = 330

    pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                             t.tlc[0] + fd[2], t.tlc[1] + fd[3])
    pil_image.show()
    # pil_image.show()
    value = t.get_ocr_float(pil_image, 'get_other_player_funds', replace_black_white=False)
    value = float(value) if value != '' else ''
    t.other_players[i]['funds'] = value

func_dict = t.coo['get_round_pot_value'][t.tbl]
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

if t.tbl == 'PS2':
    value = t.get_ocr_float(pil_image, 'RoundPotValue', force_method=0)  # force_method was 1 before

if t.tbl == 'PS2':
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



left_corn_img = t.leftpot
right_corn_img = t.rightpot
img_orig = pot_area_image
thresold =0.01
def find_pot_corners(left_corn_img, right_corn_img,img_orig,thresold):
    img = cv2.cvtColor(np.array(img_orig), cv2.COLOR_BGR2RGB)
    left_count, left_points,left_bestfit, left_minvalue = t.find_template_on_screen(left_corn_img, img, thresold)
    right_count, right_cpoints, right_cbestfit, right_minvalue = t.find_template_on_screen(right_corn_img, img, thresold)

    count = (right_count>0) & (left_count>0)

    return count, left_points[0], right_cpoints[0]

count, left_points, right_points = find_pot_corners(t.leftpot,t.rightpot,pot_area_image,0.01)

if n in (0, 1, 2):
    pil_image = t.crop_image(pot_area_image, left_points[0], 15,
                             right_points[0]+8 , pot_area_image.size[1] - 15)
    pil_image.show()
else:
    pil_image = t.crop_image(pot_area_image, 0, 15,
                             points[0][0] + 8, pot_area_image.size[1] - 15)

func_dict = t.coo['get_other_player_pots'][t.tbl]
t.gui_signals.signal_status.emit("Get player pots")
for n in range(5):
    n=1
    fd = func_dict[n]
    pot_area_image = t.crop_image(t.entireScreenPIL, t.tlc[0] - 20 + fd[0], t.tlc[1] + fd[1] - 20,
                                  t.tlc[0] + fd[2] + 20, t.tlc[1] + fd[3] + 20)
    pot_area_image.show()
    import cv2
    img = cv2.cvtColor(np.array(pot_area_image), cv2.COLOR_BGR2RGB)
    if t.tbl=='PS2':
        if n in (0,1,2):
            count, points, bestfit, minvalue = t.find_template_on_screen(t.leftpot, img,0.01)
        else:
            count, points, bestfit, minvalue = t.find_template_on_screen(t.rightpot, img,0.01)

    else:
        count, points, bestfit, minvalue = t.find_template_on_screen(t.smallDollarSign1, img,
                                                                 float(func_dict[5]))
    exist_pot = count > 0
    if exist_pot:
        if t.tbl == 'PS2':
            if n in (0, 1, 2):
                pil_image = t.crop_image(pot_area_image, points[0][0], 15,
                                         pot_area_image.size[0]-50, pot_area_image.size[1]-15)
                pil_image.show()
            else:
                pil_image = t.crop_image(pot_area_image, 0, 15,
                                         points[0][0]+8, pot_area_image.size[1]-15)

            method = func_dict[6]
            value = t.get_ocr_float(pil_image, 'get_other_player_pots', force_method=method)
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

if t.tbl == 'PS2':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    count, points, bestfit, _ = t.find_template_on_screen(t.totalpot, img, 0.01)

    if count == 1:
        start_points = points[0]
        number_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'] + start_points[0] + 5,
                                    t.tlc[1] + func_dict['y1'],
                                    t.tlc[0] + func_dict['x2']-18, t.tlc[1] + func_dict['y2'])
        number_image.show()

        value = t.get_ocr_float(number_image, 'get_total_pot_value', force_method=0, replace_black_white=True)  # force_method was 1 before
        value
    else:
        value = ''
else:
    value = t.get_ocr_float(pil_image, 'TotalPotValue', force_method=1)



func_dict = t.coo['get_other_player_pots'][t.tbl]
t.gui_signals.signal_status.emit("Get player pots")
for n in range(5):
    fd = func_dict[n]
    pot_area_image = t.crop_image(t.entireScreenPIL, t.tlc[0] - 20 + fd[0], t.tlc[1] + fd[1] - 20,
                                  t.tlc[0] + fd[2] + 20, t.tlc[1] + fd[3] + 20)
    img = cv2.cvtColor(np.array(pot_area_image), cv2.COLOR_BGR2RGB)
    if t.tbl == 'PS2':
        left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.leftpot, img, 0.01)
        right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot, img, 0.01)
        exist_pot = (right_count > 0) & (left_count > 0)
    else:
        count, points, bestfit, minvalue = t.find_template_on_screen(t.smallDollarSign1, img,
                                                                     float(func_dict[5]))
        exist_pot = count > 0

    if exist_pot:
        if t.tbl == 'PS2':
            if n in (0, 1, 2):
                pil_image = t.crop_image(pot_area_image, left_points[0][0], 15,
                                         right_points[0][0] + 8, pot_area_image.size[1] - 15)
            else:
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

func_dict = t.coo['get_other_player_pots'][t.tbl]
t.gui_signals.signal_status.emit("Get player pots")
for n in range(5):
    n=2
    fd = func_dict[n]
    pot_area_image = t.crop_image(t.entireScreenPIL, t.tlc[0] - 20 + fd[0], t.tlc[1] + fd[1] - 20,
                                  t.tlc[0] + fd[2] + 50, t.tlc[1] + fd[3] + 20)
    pot_area_image.show()
    img = cv2.cvtColor(np.array(pot_area_image), cv2.COLOR_BGR2RGB)
    if t.tbl == 'PS2':
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
        if t.tbl == 'PS2':
            if n in (0, 1, 2):
                pil_image = t.crop_image(pot_area_image, left_points[0][0], 15,
                                         right_points[0][0] + 8, pot_area_image.size[1] - 15)
            else:
                pil_image = t.crop_image(pot_area_image, left_points[0][0], 15,
                                         right_points[0][0] + 8, pot_area_image.size[1] - 15)

            method = func_dict[6]
            value = t.get_ocr_float(pil_image, str('get_other_player_pots'), force_method=method)
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

if p.selected_strategy['gather_player_names'] == 1:
    func_dict = t.coo['get_other_player_funds'][t.tbl]
    t.gui_signals.signal_status.emit("Get player funds")
    for i, fd in enumerate(func_dict, start=0):
        i=3
        fd = func_dict[i]
        t.gui_signals.signal_progressbar_increase.emit(1)
        pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                 t.tlc[0] + fd[2], t.tlc[1] + fd[3])
        # pil_image.show()
        value = t.get_ocr_float(pil_image, 'gather_player_names', replace_black_white=False)
        value = float(value) if value != '' else ''
        t.other_players[i]['funds'] = value



func_dict = t.coo['get_total_pot_value'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.gui_signals.signal_status.emit("Get Pot Value")
t.logger.debug("Get TotalPot value")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

if t.tbl == 'PS2':
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
    left_count, left_points, left_bestfit, left_minvalue = t.find_template_on_screen(t.totalpot, img,
                                                                                     0.01)
    right_count, right_points, right_cbestfit, right_minvalue = t.find_template_on_screen(t.rightpot,
                                                                                          img, 0.01)
    count = (left_count > 0) & (right_count > 0)

    if count == 1:
        number_image = t.crop_image(pil_image,  left_points[0][0] + 7,
                                    5,
                                    right_points[0][0]+4,pil_image.size[1]-5)

        value = t.get_ocr_float(number_image, str('get_total_pot_value'), force_method=0)  # force_method was 1 before

        value
        if not (value).is_integer():
            value = float(str(value).replace('.','')[0:(len(str(value))-1)])
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

t.logger.info("Final Total Pot Value: " + str(t.totalPotValue))



from tools.mouse_mover import *
from decisionmaker.decisionmaker import DecisionTypes

mouse = MouseMoverTableBased(p.selected_strategy['pokerSite'])
mouse.move_mouse_away_from_buttons_jump

mouse_target == 'Bet half pot'
if mouse_target == 'Call' and t.allInCallButton_found:
    mouse_target = 'Call2'
mouse.mouse_action(mouse_target, t.tlc)
mouse.coo[mouse_target]

mouse_target = 'Bet half pot'
for action in mouse.coo[mouse_target]:
    print(action)
    for i in range(int(action[0])):
        print(i)


['Imback',
'Fold', 'Check',
'Call', 'Bet',
'BetPlus',
'Bet half pot',
'Bet pot',
'Bet Bluff',
'Call Deception',
'Check Deception']

mouse_target = 'Bet half pot'
m_coor = mouse.coo[mouse_target][0]
topleftcorner=t.tlc
tlx = int(topleftcorner[0])
tly = int(topleftcorner[1])
action =mouse.coo[mouse_target][0]
[1, 0.3, 592, 436, 30, 12]
action[2] = 670
action[3] = 436
number_image = t.crop_image(t.entireScreenPIL,  action[2]+ tlx,
                            action[3] + tly,
                            action[2] + tlx + action[4],action[3]+ tly + action[5])
number_image.show()
action =mouse.coo[mouse_target][1]
number_image = t.crop_image(t.entireScreenPIL,  action[2]+ tlx,
                            action[3] + tly,
                            action[2] + tlx + action[4],action[3]+ tly + action[5])
number_image.show()

func_dict = t.coo['check_for_betbutton'][t.tbl]
t.gui_signals.signal_progressbar_increase.emit(5)
t.logger.debug("Check for betbutton")
pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)
count, points, bestfit, _ = t.find_template_on_screen(t.betbutton, img, func_dict['tolerance'])
if count > 0:
    t.bet_button_found = True
    t.logger.debug("Bet button found")
else:
    t.bet_button_found = False
    t.logger.info("Bet button NOT found")

d.preflop_sheet_name = ''
if t.equity >= float(p.selected_strategy['alwaysCallEquity']):
    d.logger.info("Equity is above the always call threshold")
    d.finalCallLimit = 99999999

# if t.myFunds * int(p.selected_strategy['always_call_low_stack_multiplier']) < t.totalPotValue:
#    d.logger.info("Low funds call everything activated")
#    d.finalCallLimit = 99999999

if p.selected_strategy['preflop_override'] and t.gameStage == GameStages.PreFlop.value:
    d.preflop_override(t, logger, h, p)

else:
    d.calling(t, p, h)
    d.betting(t, p, h)
    if t.checkButton:
        d.check_deception(t, p, h)

    if t.allInCallButton_found == False and t.equity >= float(p.selected_strategy[
                                                                  'secondRiverBetPotMinEquity']) and t.gameStage == GameStages.River.value and h.histGameStage == GameStages.River.value:
        d.decision = DecisionTypes.bet4

        # d.bully(t,p,h,logger)

d.admin(t, p, h)
d.bluff(t, p, h)
d.decision = d.decision.value

if p.selected_strategy['gather_player_names'] == 1:
    func_dict = t.coo['get_other_player_funds'][t.tbl]
    t.gui_signals.signal_status.emit("Get player funds")
    for i, fd in enumerate(func_dict, start=0):
        t.gui_signals.signal_progressbar_increase.emit(1)
        pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + fd[0], t.tlc[1] + fd[1],
                                 t.tlc[0] + fd[2], t.tlc[1] + fd[3])
        # pil_image.show()
        value = t.get_ocr_float(pil_image, str('get_other_player_funds'), replace_black_white=False)
        if not value == '':
            if not (value).is_integer():
                value = float(str(value).replace('.', '')[0:(len(str(value)) - 1)])
        value = float(value) if value != '' else ''
        t.other_players[i]['funds'] = value

func_dict = t.coo['check_for_imback'][t.tbl]
func_dict['x1'] = 274
func_dict['x2'] = 500
func_dict['y1'] = 180
func_dict['y2'] = 230


func_dict['x1'] = 174
func_dict['x2'] = 600
func_dict['y1'] = 180
func_dict['y2'] = 530

pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                         t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

pil_image.show()
# Convert RGB to BGR
img = cv2.cvtColor(np.array(t.entireScreenPIL), cv2.COLOR_BGR2RGB)
count, points, bestfit, minvalue = t.find_template_on_screen(t.notlostEverything, img, 0.01)
t.imback_found = count > 0


def get_current_bet_value(self, p):
    func_dict = t.coo['get_current_bet_value'][t.tbl]
    self.gui_signals.signal_progressbar_increase.emit(5)
    self.gui_signals.signal_status.emit("Get Bet Value")
    self.logger.debug("Get bet value")

    pil_image = t.crop_image(t.entireScreenPIL, t.tlc[0] + func_dict['x1'], t.tlc[1] + func_dict['y1'],
                                t.tlc[0] + func_dict['x2'], t.tlc[1] + func_dict['y2'])

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

    t.logger.info("Final call value: " + str(t.currentCallValue))
    t.logger.info("Final bet value: " + str(t.currentBetValue))