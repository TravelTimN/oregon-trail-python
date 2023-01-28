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