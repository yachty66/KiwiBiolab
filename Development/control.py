'''
Notes:
# Machine process
1. Drive to rails 43 - 
2. Pick up tip at position 0 (in every iteration move one position further)
3. Drive to rails 26 
4. Aspirate 1000 ul from tip at position 0 
5. Drive to rail 1 and dispense 1000 ul at position 0 
6. Dispose tip
7. Repeat three times 

Ideas for improvement
- init
- use 


comparing logs 

creating a program on venus which is doing the same like what I do. get the log and send it via email to me.
repeat the same on my laptop and safe the log. post both logs into the forum 

for adding new carrier type i need to know how for example plate carrier was implemented. when init a tube carrier ressource the robot needs to know where to drive to. 

How can I add tube carrier to the project?

- [ ] make a list of paths where platecarrier.py appears (https://docs.pylabrobot.org/pylabrobot.liquid_handling.resources.html?highlight=from%20scratch%20you%20can%20define%20your%20own%20resources)
    - pylabrobot.liquid_handling.resources.ml_star.plate_carriers
    - pylabrobot.liquid_handling.resources.abstract
    - /Users/maxhager/Projects2022/KiwiBiolab/PyLabRobot/pylabrobot/pylabrobot/liquid_handling/resources/ml_star/__init__.py
- [ ] go to every path and make a appropriate change for tube carrier



Everything what has something to do with ressources is in the folder /Users/maxhager/Projects2022/KiwiBiolab/PyLabRobot/pylabrobot/pylabrobot/liquid_handling/resources. There the following for me relevant folders/files exist:
- abstract
- hamilton
- ml_star
- __init__.py
- one path above is another __init__.py where I need to import new created resources 
'''
from pylabrobot.pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.pylabrobot.liquid_handling.backends import STAR
from pylabrobot.pylabrobot.liquid_handling.resources.abstract import tip_rack
from pylabrobot.pylabrobot.liquid_handling.resources.abstract.tip_rack import TipRack
from pylabrobot.pylabrobot.liquid_handling.resources.hamilton import STARDeck
#from pylabrobot.liquid_handling.resources.hamilton import STARLetDeck
#import logging
#logging.getLogger("pylabrobot").setLevel(logging.DEBUG)

backend = STAR()
lh = LiquidHandler(backend=backend, deck=STARDeck())
lh.setup()
#check again if tips are correct
from pylabrobot.pylabrobot.liquid_handling.resources import (
    MFX_CAR_5Tip,
    VER_ST,
    SMP_CAR_32_12x75_A00,
    test   
)

#tip is on wrong height i.e. i need to move it up. I 
tip_car = MFX_CAR_5Tip(name='tip carrier')
tip_car[1] = VER_ST(name='tips_01')
lh.deck.assign_child_resource(tip_car, rails=43)

plt_car = test(name='plate carrier')
plt_car[0] = SMP_CAR_32_12x75_A00(name='plate_01')
lh.deck.assign_child_resource(plt_car, rails=26)

lh.summary()
    
tiprack = lh.get_resource("tips_01")
lh.pick_up_tips(tiprack["A1"])

plate = lh.get_resource("plate_01")
lh.aspirate(plate["A1"], vols=[100.0])




#lh.discard_tips(tiprack["A1:C1"])


#plt_car = MFX_CAR_5Tip(name='plate carrier')
#plt_car[1] = Cos_96_DW_1mL(name='plate_01')

#lh.deck.assign_child_resource(plt_car, rails=15)

#i dotn think that the issue is because of wrong resources but rather because of somethin which went wrong in the backend
#i can compare my logs with the logs with the machine. problem is that the logs of the machine look a little bit different than my perhaps i can create my own step on the computer which is identical to what I do. Without throwing the tip away