# Python Oregon Trail

![Oregon Trail Wagon](documentation/ot-wagon-02.jpg)

## Objects / Classes

### **Player**
* extends **Person**
- profession (banker $1600, carpenter $800, farmer $400)
- family members (4 others)
- cash (int | in $)
- food (in lbs. min: 1000 lbs / max: 2000 lbs)
- ammunition (in boxes of 20. min: 1 box / max: 99 boxes)
- oxen (2 per yoke. min: 1 yoke / max: 9 yokes)
- clothing (in sets. min: 10 sets / max: 99 sets)
- spare parts / misc supplies
    - wagon wheels (0-3 wheels)
    - wagon axels (0-3 axels)
    - wagon tongues (0-3 tongues)

### **Person**
- name
- illness
- accidents
- health (from: good / fair / poor / very poor)

### **Landmark**
- id
- name
- type (from: start / end / river / fort / misc)
- next_landmark (some have split paths!!!)
- distance_to_next_landmark (in miles)
- can_buy_supplies? (bool)

---

## Stopping to Rest

During game play, you can stop to rest between 1-9 days.

Resting will continue to deplete your food, and the normal day/weather cycles persist for each day.

## Trading

During game play, you can attempt to trade.

- No one wants to trade with you today.
- You meet another emigrant who wants 1 set of clothing. He will trade you 30 pounds of food.
- You meet another emigrant who wants 1 ox. He will trade you 1 set of clothing.
- You meet another emigrant who wants 1 wagon wheel. He will trade you 26 pounds of food.
- You meet another emigrant who wants 1 ox. She will trade you 104 bullets.
- You meet another emigrant who wants 1 set of clothing. She will trade you 47 bullets.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 73 bullets.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 25 pounds of food.
- You meet another emigrant who wants 1 ox. She will trade you 1 set of clothing.


## Crossing Rivers

During game play, there are four (4) river crossings.
Depending on the weather and river data, the crossing can vary anywhere between harmless and cause of death.

Possible river crossing outcomes:

- safe crossing
- swamping
- overturning
- swept away
- stuck in mud (It was a muddy crossing, but you did not get stuck.)

https://www.died-of-dysentery.com/stories/crossing-rivers.html

![fording a river](documentation/ot-river-fording.png)

Algorithm for fording a river:
- **D** = depth
- **BT** = bottom type (smooth and firm || muddy || rocky and uneven)

![fording algorithm](documentation/ot-river-fording-algorithm.png)

Hiring an Indian:
- **D** = depth
- **S** = swiftness
- **BT** = bottom type (smooth and firm || muddy || rocky and uneven)

![river swiftness](documentation/ot-river-hire-indian.png)


### Caulking the Wagon

The chances of successfully caulking the wagon to cross a river depends on the water level,
speed of the current, and condition of the wagon, but can be raised if the player uses pelt to seal the wagon.
The maximum amount of pelts that can be used depends on the river being crossed.
Also, like the "ford" option, the player can rest before crossing the river to wait for more suitable crossing conditions.

### Fording

Unless the player is crossing an extremely shallow river, **fording** a river always has a 0% chance of success.
The chance of success can be raised using the same methods as when the player caulks the wagon.

### Ferry

The ferry costs money to use, although it is the only method that immediately has a 100% chance of success.
The cost of a ferry crossing starts at $5 per oxen and person, although can be lowered through haggling.
There is also a three day interval between the player paying for the ferry, and actually crossing.

---
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!