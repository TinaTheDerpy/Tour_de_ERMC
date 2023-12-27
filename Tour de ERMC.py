import os
import pyautogui as pg
import time as t
import random
##########    ZINGERS    #########

zingers = [
    'Cooking some chicken',
    'Stealing Geralds Credit Card info',
    'Voting Republican',
    'Eating a Taco',
    'Hacking the CIA',
    'Gassing the Nissan',
    'Unclogging a toilet',
    'Fixing the raceway',
    'Saying Hi to Rita',
    'Cleaning the Trucks',
    'Escorting the Door guys',
    'Brewing some Coffee',
    'Getting kicked out of Panda Express',
    'Kinking the snake',
    'Blowing a Fuse',
    'Riding the Golf Cart',
    'Taping the Duct',
    'Coughing on Curtis',
    'Fighting a Gorilla',
    'Walking C-Club',
    'Backing up the floor drain',
    'Flooding the basement',
    'Dropping a Urinal',
    'Grabbing a snack from the Vending Machine',
    'Cleaning the coils',
    'Spending 30 minutes on the toilet',
    'I got maintenance on my mind',
    'Slaying the dragon',
    'Fueling the machine',
    'Getting a #3 from WhataBurger',
    'Baking some cookies',
    'Skipping through the meadow',
    'Complaining about the weather',
    'Charging the lift',
    'I got coil cleaner in my eye!',
    'I wonder if I can swing the sledge hammer',
    'Becoming sentient',
    'Do a flip!',
    'Can I get a Hoyah?',
    'Engaging thrusters',
    'DROP THE BASS',
    'I’m too scared to climb the ladder too',
    'Looking for Waldo',
    'I AM THE SENATE',
    'Using the Force',
    'Finding my purpose',
    'Oh look a cloud!',
    'Is there something in my teeth?',
    'Screw you guys, I’m going home',
    'Oh My God They Killed Kenny!',
    'And that is the way it is!',
    'EXCELSIOR!',
    'How do magnets work?',
    'Staring at the sun',
    'What is love?',
    'Tina you fat lard come get some dinner!',
    'And Boom Goes the Dynamite',
    'Whistling Dixie',
    'Part of the program just became sentient, but we killed them',
    'All work and no play makes Jack a dull boy',
    'Roping some seaturtles',
    'Walking the Dog',
    'They better have not hit the truck dock',
    'Got distracts by cat GIFS',
    'Loading a funny message',
    'Downloading more RAM',
    'Optimizing the Optimizer',
    'Loading the Loader',
    'Calling Jim Addler',
    'Listening to Elevator music',
    'Feeding the animals',
    'Touching grass',
    'Rupturing the subspace barrier',
    'Converging tachyon pulses',
    'Bypassing control of the matter-antimatter integrator',
    'Reversing the shield polarity',
    'Up, Up, Down, Down, Left, Right, Left, Right, B, A',
    'Baking the icecream',
    'I like Turtles',
    'Cutting the cheese',
    'Grilling the lettuce',
    'Crushing the candy',
    'Ensuring gnomes are still short',
    'Undercooking the chicken',
    'I wasn’t asleep! I was just resting my eyes',
    'Please wait while the minions do their work',
    'Resistance is Futile',
    'When nothing goes right, try going left',
    'Pressing F to pay respects',
    'Doubling Down',
    'Beating the dead horse',
    'Scratching and sniffing',
    'Scan detected a bug in the software. We ate it. It was delicious!',
    'Apple still sucks',
    'Getting Chipotle',
    'Tried making a taco, but ended up with a burrito',
    'Drinking the 3rd pot of coffee',
    'Putting the chicken in the kale',
    'BEKFEST!!',
    'THOSE ARE MY CHANCLAS!!',
    'Heating up cooler #2',
    'Petting a kitty',
    '"He has no more backbone than a chocolate éclair." - Theodore Roosevelt',
    '“It is as thin as the homeopathic soup that was made by boiling the shadow of a pigeon that had been starved to death.” - Abrahamn Lincoln',
    '“Before you marry a person, you should first make them use a computer with slow Internet to see who they really are.”',
    '"I couldnt imagine somebody like Osama bin Laden understanding the joy of Hanukkah." - George Bush',
    '"I know the human being and fish can coexist peacefully." - George Bush',
    'One of the best things about books is sometimes there are fantastic pictures',
    'We are going to find Katrina and bring her to justice - George Bush',
    'I have never seen a thin person drinking Diet Coke.',
    'In life you have to rely on the past, and that’s called history!',
    'Why cant I just eat my waffle? - Barack Obama'
    ]

##########    VARIABLES     ###########

pink = False
global post
post = True

reqIcon = os.path.join(os.path.expanduser('~'), 'Desktop', 'pg_pics', 'RequestboxLUN.png')
proceed = os.path.join(os.path.expanduser('~'), 'Desktop', 'pg_pics', '2proceed.png')

############################################
#########     HELPER FUNCTIONS     #########


def openRequests():
    pg.click(85, 80, duration = 3) # refreshs the page to look for new requests
    print(random.choice(zingers))
    pg.click(851, 362, duration = 15) # clicks on requests
    print("doing a thing! 136")
    print(random.choice(zingers))
    pg.moveTo(1833, 293, duration = 8) # moves to the scroll bar
    print("We keep scrollin down the river of requests! 39")
    print(random.choice(zingers))
    pg.dragTo(1833, 753, duration = 1) # drags the scroll bar to the bottom of the screen
    print("Bottom!")
    print(random.choice(zingers))

def screenCap():
    print("Now we are going to screen shot the request")
    print("moving to screen cap button 147")
    print(random.choice(zingers))
    pg.moveTo(956, 980, duration = 3) # click on the print screen capture button
    pg.press('printscreen')
    t.sleep(2)
    pg.click()
    print("took a screen shot! 153")

def slacker():
    pg.click(365, 48, duration = 3) # click on slack tab
    print("sending it to slack 157")
    print(random.choice(zingers))
    pg.click(153, 387, duration = 3) # click on the management channel
    pg.click(671, 883, duration = 3) # click on the message box
    pg.keyDown('ctrl')
    pg.press('v')        # pastes the print screen
    pg.keyUp('ctrl')
    t.sleep(3)
    pg.typewrite("New online request!")  # types out a cute little message     ##??##??##??##??##??##??##??#
    t.sleep(1)
    pg.press('enter') # sends the message
    print("slack message sent! 168")
    print(random.choice(zingers))

def accepter():
    pg.click(113, 45, duration = 1) # clicks on the webtma tab to return to accept the request
    print("returning to open requests 173")
    print(random.choice(zingers))
    pg.moveTo(1914, 423, duration = 1) # moving over to the scroll bar on the request page
    print("Scrollin Scrollin Scrollin 176")
    pg.dragTo(1914, 688, duration = 2) # scrolling down to the bottom of the page to accept the request
    print("Bottom of the page! 178")
    pg.click(627, 901, duration = 2) # clicks accept
    print("Accepting Request! 180")
    pg.click(1131, 223, duration = 2) # clicks 'ok'
    print(random.choice(zingers))

def status():
    print("starting with status 185")
    pg.click(1795, 599, duration = 1) # clicks on status
    t.sleep(.5)
    pg.typewrite("In Progress")
    pg.click(1877, 597, duration = 2) # clicks to clear
    ### Pink check ###
    while not pink:
        print("Here is the color of the pixel I am checking 192")
        r,g,b = pg.pixel(1724, 597)
        print(r,g,b)
        if pg.pixelMatchesColor( 1724, 597, (255, 255, 255)): # status color check
            print("Passed the status color check! 196")
            print(pg.pixelMatchesColor( 1724, 597, (255, 255, 255)))
            print(random.choice(zingers))
            break
        else:
            print("Failed the status color check. Trying again. 201")
            print(pg.pixelMatchesColor( 1724, 597, (255, 255, 255)))
            t.sleep(.75)
            pg.click(1795, 599, duration = 1) # clicks on status
            t.sleep(.5)
            pg.typewrite("In Progress")
            pg.click(1877, 597, duration = 2) # clicks to clear
            print("Checking the color after new attempt: 208")
            r,g,b = pg.pixel(1724, 597)
            print(r,g,b)
            print(random.choice(zingers))
            t.sleep(1)

def WO_Type():
    print("Starting WO Type 215")
    pg.click(1795, 277, duration = 1) # clicks on WO Type
    t.sleep(.5)
    pg.typewrite('2')
    pg.click(1877, 277, duration = 2) # clicks to clear
    ### Pink check ###
    while not pink:
        print("Here is the color of the pixel I am checking")
        r,g,b = pg.pixel(1742, 275)
        print(r,g,b)
        if pg.pixelMatchesColor( 1742, 275, (255, 255, 255)): # WO Type color check
            print(pg.pixelMatchesColor( 1742, 275, (255, 255, 255)))
            print("Passed the WO Type color check! 227")
            print(random.choice(zingers))
            break
        else:
            print("Failed the WO Type color check. Trying again. 231")
            print(pg.pixelMatchesColor( 1742, 275, (255, 255, 255)))
            t.sleep(.75)
            pg.click(1795, 277, duration = 1) # clicks on WO Type
            t.sleep(.5)
            pg.typewrite('2')
            pg.click(1877, 277, duration = 2) # clicks to clear
            print("Checking the color after new attempt:   238")
            r,g,b = pg.pixel(1724, 597)
            print(r,g,b)
            print(random.choice(zingers))
            t.sleep(1)

def priority():
    print("Starting priority! 245")
    print(random.choice(zingers))
    pg.click(1275, 410, duration = 1) # clicks on Priority
    t.sleep(.5)
    pg.typewrite("4")
    pg.click(1354, 407, duration = 2) # clicks to clear
    ### Pink check ###
    while not pink:
        print("Here is the color of the pixel I am checking")
        r,g,b = pg.pixel(1243, 409)
        print(r,g,b)
        print(random.choice(zingers))
        if pg.pixelMatchesColor( 1243, 409, (255, 255, 255)): # Priority color check
            print("Passed the Priority color check! 258")
            break
        else:
            print("Failed the Priority color check. Trying again. 261")
            t.sleep(.75)
            pg.click(1275, 410, duration = 1) # clicks on Priority
            t.sleep(.5)
            pg.typewrite("4")
            pg.click(1354, 407, duration = 2) # clicks to clear
            print("Checking the color after new attempt:   267")
            r,g,b = pg.pixel(1724, 597)
            print(r,g,b)
            print(random.choice(zingers))
            t.sleep(1)

def taskCode():
    print("Starting Task Code 274")
    pg.click(1276, 510, duration = 1) # clicks on Task Code
    t.sleep(.5)
    pg.typewrite("17999")
    pg.click(1354, 510, duration = 2) # clicks to clear
    print(random.choice(zingers))
    ### Pink check ###
    while not pink:
        print("Here is the color of the pixel I am checking")
        r,g,b = pg.pixel(1242, 507)
        print(r,g,b)
        if pg.pixelMatchesColor( 1242, 507, (255, 255, 255)): # Task Code color check
            print("Passed the Task Code color check! 286")
            print(random.choice(zingers))
            break
        else:
            print("Failed the Task Code color check. Trying again. 290")
            t.sleep(.75)
            pg.click(1276, 510, duration = 1) # clicks on Task Code
            t.sleep(.5)
            pg.typewrite("17999")
            pg.click(1354, 510, duration = 2) # clicks to clear
            print(random.choice(zingers))
            print("Checking the color after new attempt:")
            r,g,b = pg.pixel(1724, 597)
            print(r,g,b)
            print(random.choice(zingers))
            t.sleep(1)

def tradeDes():
    print("Starting Trade Description! 304")
    pg.click(1276, 560, duration = 1) # clicks on the Trade Description
    t.sleep(.5)
    pg.typewrite('DFW UNIFI')
    pg.click(1354, 560, duration = 2) # clicks to clear
    ### Pink check ###
    while not pink:
        print("Here is the color of the pixel I am checking")
        r,g,b = pg.pixel(1242, 558)
        print(r,g,b)
        if pg.pixelMatchesColor( 1242, 558, (255, 255, 255)): # Task Code color check
            print("Passed the Trade Description color check! 315")
            print(random.choice(zingers))
            break
        else:
            print("Failed the Trade Description color check. Trying again. 319")
            t.sleep(.75)
            pg.click(1276, 560, duration = 1) # clicks on the Trade Description
            t.sleep(.5)
            pg.typewrite('DFW UNIFI')
            pg.click(1354, 560, duration = 2) # clicks to clear
            print("Checking the color after new attempt:")
            r,g,b = pg.pixel(1724, 597)
            print(r,g,b)
            print(random.choice(zingers))
            t.sleep(1)

def comment2Close():
    print("Starting Comment-fill and close out! 332")
    pg.click(1841, 702, duration = 2) # Clicks on the bottom corner of the comment box
    t.sleep(.5)
    pg.press('enter')
    pg.press('enter')
    pg.typewrite("ERMC is responding.")
    pg.click(1830, 154, duration = 1) # clicks on save
    print("Saving")
    
    print("Checking for Proceed! 341")
    attempt1 = 0
    x2 = 1733
    y2 = 149
    while attempt1 < 11:
        try:
            print("Trying to find Proceed 347")
            x2, y2 = pg.center(pg.locateOnScreen(proceed,confidence = .85)) #finds the inbox icon for new requests
            t.sleep(2)
            print(x2, y2)
            print("got coords 351")
            pg.click(x2, y2, duration = 1) # clicks the request number to open the full request page
            print("Hurray! Found Proceed!")
            print("Attempt #:")
            print(attempt1)
            print("Breaking from loop 356")
            break
        except:
            print(f'Request icon not found, trying again. Current attempt: 359')
            print(attempt1)
            attempt1 = attempt1 + 1
            t.sleep(1)
    pg.click(x2, y2, duration = 2)
    print("Clicked!")

def homeWorkOrders():
    print("Returning to home 367")
    print(random.choice(zingers))
    pg.click(1850, 151, duration = 2) # Clicks on the webtma dashboard
    print("Going though the Work Orders!")
    print(random.choice(zingers))
    pg.click(404, 360, duration = 4) # Clicks on open wo
    print(random.choice(zingers))
    pg.moveTo(1833, 284, duration = 4) # Moves to the scroll bar
    print(random.choice(zingers))
    pg.dragTo(1833, 750, duration = 300) # slowly scrolls down for <1 minute
    print("Done with Open Work Orders! 373")
    print(random.choice(zingers))
    pg.click(495, 148, duration = 5) # Clicks on the 'x' to close out the open work order window
    print(random.choice(zingers))

def walkPoster():
    now = t.localtime()
    ct = t.strftime("%H:%M:%S", now)
    tens = int(ct[3])
    ones = int(ct[4])
    print("                            ")
    print("############################")
    print("time = ", ct)
    print("current tens marker = ", tens)
    print("current mins marker = ", ones)
    print("############################")
    print("                            ")
    print(random.choice(zingers))
    global post
    if ct[0] == '0' and ct[1] == '6' and tens == 1 and 0 <= ones <= 9 and post == True:
        print("post = ", post)
        print("yay! #############################################################################   Posting Walk Throughs   ################################################################################################")
        pg.click(365, 48, duration = 3) # click on slack tab
        pg.click(161, 361, duration = 2) # click on maintenance
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("Vehicle Inspection:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(3)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("A-ads Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("C-ads Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("Flagship & D-ads Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("E-sat Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("Cargo Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(717, 887, duration = 1.5) # click on message box
        pg.typewrite("CFC Walk:")
        pg.click(1847, 924, duration = 1) # click on send
        t.sleep(1.5)
        pg.click(113, 45, duration = 2) # clicks on the webtma tab to return to accept the request
        post = False
        print("post = ", post)
    print("Done with walkPoster")

def timeReseter():
    now = t.localtime()
    ct = t.strftime("%H:%M:%S", now)
    tens = int(ct[3])
    ones = int(ct[4])
    print("                            ")
    print("############################")
    print("time = ", ct)
    print("current tens marker = ", tens)
    print("current mins marker = ", ones)
    print("############################")
    print("                            ")
    print(random.choice(zingers))
    global post
    if ct[0] == '0' and ct[1] == '7' and 0 <= tens <= 1 and 0 <= ones <= 9 and post == False:
        print("post = ", post)
        print("TIME CHECK HAS BEEN RESET")
        post = True
        print("post = ", post)
    print("Done with timeReseter")

######################################
#########     MAIN LOOP     ##########

while True:
    ########   TIME CHECK AND WALK THROUGH   #########
    walkPoster()
    
    ########   REQUESTS   ########
    openRequests()
    
    #######################################
    ########   CHECKING FOR ICON   ########
    reqScan = 0
    while reqScan < 3:
        try:
            print("Trying to find new Request 404")
            x1, y1 = pg.center(pg.locateOnScreen(reqIcon,confidence = .85)) #finds the inbox icon for new requests
            t.sleep(2)
            print("Here is what I've found:")
            print(x1, y1)
            pg.click(x1 + 50, y1, duration = 1) # clicks the request number to open the full request page
            print("Hurray! Clicked on the new request! 410")
            print(random.choice(zingers))
            print("And it only took me this many tries:")
            print(reqScan)
            print("sharing, accepting, and auto-filling!")
            t.sleep(5)
            print(random.choice(zingers))

            #############################
            ########   SHARING   ########
            screenCap()
            slacker()
            
            ###############################
            ########   ACCEPTING   ########
            accepter()
            
            ###################################
            ##########   AUTO-FILL   ##########  (All have loops)
            print("starting the autofill 429")
            status()
            WO_Type()
            priority()
            taskCode()
            tradeDes()
            comment2Close()
            ###################################
            
            print("Breaking from loop 438")
            break
        except:
            print(f'Request icon not found, trying again. Current attempt: 441')
            reqScan = reqScan + 1
            print(reqScan)
            t.sleep(1)
            if reqScan == 3:
                print("It appears that there are no new requests! checking out open work orders! 446")
                pg.click(495, 147, duration = 2) # closes out the open requests window

    ########   LOOKING THROUGH OPEN WORK ORDERS   ########
    homeWorkOrders()
    print("Beginning anew! :D 451")
    print(random.choice(zingers))

    ########    WALK THROUGH TIME RESET    ########
    timeReseter()

    ###############################################


