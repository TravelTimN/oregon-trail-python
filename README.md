![Oregon Trail Wagon](documentation/ot-logo-python.png)

# The Oregon Trail (Python)

## Features

### Wagon Animation

Using [text-image](https://www.text-image.com/convert/ascii.html) to convert an image to ASCII art, I've created a 4-second animation of the traditional "Oregon Trail ox and wagon" trekking across the screen.

Original image used:

![Oregon Trail Wagon](documentation/ot-wagon-02.jpg)

Output:

```
          .^7?!^...      :~7~~:    .~~^~:..         . .:^!JY7::::.              
 .^..:^~!?YGPYPG5PP?7~~7JY5PPBGY77YPG#BBBYGPY7:.:^~!~~7JJYPGG55P5Y?~~^.   .:^~^7
JYY??JYY5YYY7~?JJJ?~!?JYYYYJ?~^~7JYJJJYYYYPPYJ!~7!?Y?!?YYY?7JJJYYJYY5G55G5Y5P55P
J??!!!!!!!^^:  ........^^^^..   ......:^^^^~:.!!^!????7!!!!!!~^~~!!?YYJJJ7!~^^^^
                                                                    ...         
                                              :YGGBGGBPJJ!^.~~~.^?JJYGGGBY      
                                              .GG!B@@@@@@@#G@@@G#@@@@@@@@P      
                                               :#7 Y@@@@@@#B@@@B#@@@@@@@G       
                             :^.:7.             !&~ #@@@@@#B@@@B#@@@@@@G:       
                             ~5##@J75P557Y5Y!.  .J~:5PPGBG55GGG5PPPGBGG!        
                             7J5BBB&@@@@@@@@G^^^^7J?~?5?JPJJ7JY?~J5?JPJ7        
                                .J@@BY5Y7##&5    :~ ^Y?GG5JY.~! ^GJGG55G.       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~G555^::JB!5&J^^^^:^^7PG?PY~^^:^^!PBJ5P!^^^^^^^^
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

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

## Random Names

Should you decide not to select your family/friends' names, there's a predefined list of names:

| Females | Males |
| --- | --- |
| Anna | Henry |
| Beth | Jed |
| Emily | Joey |
| Mary | John |
| Sara | Zeke |

---

## Supplies

You will be required to carry supplies with you to help make the arduous journey to Oregon.

| Resource | Min | Max | Notes |
| --- | :---: | :---: | --- |
| wagon | 1 | 1 | |
| oxen yoke | 1 | 9 | 1 yoke = 2 oxen |
| food | 1,000 | 2,000 | pounds of food |
| clothing | 10 | 99 | sets of clothing |
| ammunition | 1 | 99 | 1 box = 20 bullets |
| wagon wheel | 0 | 3 | |
| wagon axel | 0 | 3 | |
| wagon tongue | 0 | 3 | |

---

## Health

While alive, there are four (4) different health states you and your party can encounter:

- good
- fair
- poor
- very poor

---

## Travel Pace

During game play, you are able to adjust the pace at which your party travels to Oregon.

| Pace | Distance (miles per day) |
| --- | :---: |
| steady | 18 mi/day |
| strenuous | 30 mi/day |
| grueling | 36 mi/day |

---

## Food Consumption

During game play, you are able to adjust the food rationing; the rate at which your party consumes food.

| Ration | Amount | Consumed (pounds per day) |
| --- | --- | :---: |
| filling | meals are large and generous | 15 lbs/day |
| meager | meals are small, but adequate | 10 lbs/day |
| bare bones | meals are very small; everyone stays hungry | 5 lbs/day |

---

## Weather

As the player travels along the trail, each day’s weather is based on the current month,
and the player’s current location along the trail.

The simulation retrieves the corresponding average temperature, and adds or subtracts a random deviation.
The simulation also retrieves the odds of rainfall, and then generates conditions that may be
dry, rainy, or very rainy.

If the weather is very cold, then snow replaces rain.

- cool
- hot
- warm
- cold
- rainy / snowy
- very rainy / very snowy
- severe thunderstorm (lose 1 day)

---

## Landmarks

There are three branch points in the game, where the player must decide whether to go left or right.
Consequently there are 20 trail segments in the network connecting these 18 points.
However, in a typical game, the player passes just 16 landmarks and travels 15 trail segments.

| ID | Landmark | Type | Next Landmark | Next Landmark | Buy Supplies | Hire Indian | Hire Ferry |
| :--: | --- | :---: | --- | :---: | :---: | :---: | :---: |
| L01 | Independence, Missouri | START | Kansas River Crossing | 102 miles | ✅ | | |
| L02 | Kansas River Crossing | River | Big Blue River Crossing | 82 miles | | ❌ | ✅ |
| L03 | Big Blue River Crossing | River | Fort Kearney | 118 miles | | ❌ | ❌ |
| L04 | Fort Kearney | Fort | Chimney Rock | 250 miles | ✅ | | |
| L05 | Chimney Rock | Misc | Fort Laramie | 86 miles | | | |
| L06 | Fort Laramie | Fort | Independence Rock | 190 miles | ✅ | | |
| L07 | Independence Rock | Misc | South Pass | 102 miles | | | |
| L08 | South Pass | Misc | Green River Crossing | 57 miles | | | |
| | | Fort Bridger | 125 miles | | | |
| L09 | Green River Crossing | River | Soda Springs | 143 miles | | ❌ | ✅ |
| L10 | Fort Bridger | Fort | Soda Springs | 162 miles | ✅ | | |
| L11 | Soda Springs | Misc | Fort Hall | 57 miles | | | |
| L12 | Fort Hall | Fort | Snake River Crossing | 182 miles | ✅ | | |
| L13 | Snake River Crossing | River | Fort Boise | 113 miles | | ✅ | ❌ |
| L14 | Fort Boise | Fort | Blue Mountains | 160 miles | ✅ | | |
| L15 | Blue Mountains | Misc | Fort Walla Walla | 55 miles | | |
| | | The Dalles | 125 miles | | | |
| L16 | Fort Walla Walla | Fort | The Dalles | 120 miles | ✅ | | |
| L17 | The Dalles | Misc | Willamette Valley, Oregon | 100 miles | | | |
| L18 | Willamette Valley, Oregon | END | | | | | |

### **Independence, Missouri**
- The start of your journey to Oregon!

#### Attempt to Trade

- You meet another emigrant who wants 2 wagon tongues. He will trade you 1 ox.
- You meet another emigrant who wants 1 wagon wheel. He will trade you 76 bullets.
- You meet another emigrant who wants 391 bullets. She will trade you 1 ox.

#### Talk to People

- A town resident tells you:
    - "Some folks seem to think that two oxen are enough to get them to Oregon! Two oxen can barely move a fully loaded wagon, and if one of them gets sick or dies, you won't be going anywhere. I wouldn't go overland with less than six."
- A trader named Jim tells you:
    - "Better take extra sets of clothing. Trade 'em to Indians for fresh vegetables, fish, or meat. It's well worth hiring an Indian guide at river crossings. Expect to pay them! They're sharp traders, not easily cheated."
- A traveler, Miles Hendricks, tells you:
    - "Did you read the Missouri Republican today? --Says some folk start for Oregon without carrying spare parts, not even an extra wagon axle. Must think they grow on trees! Hope they're lucky enough to find an abandoned wagon."

#### Buy Supplies

| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $20.00 | per ox |
| Clothing | $10.00 | per set |
| Ammunition | $2.00 | per box of 20 |
| Wagon wheels | $10.00 | per wheel |
| Wagon axles | $10.00 | per axle |
| Wagon tongues | $10.00 | per tongue |
| Food | $0.20 | per pound |

### **Kansas River**
- weather: cool/hot
- width: between 608-648 feet wide
- depth: between 2.1-7.4 feet deep

Choices:
- ford
- caulk/float
- ferry ($5.00 + wait 2-6 days)
- wait (between 1-6 days)

#### Attempt to Trade

- You meet another emigrant who wants 1 wagon wheel. He will trade you 1 set of clothing.
- You meet another emigrant who wants 120 pounds of food. He will trade you 1 ox.
- You meet another emigrant who wants 216 pounds of food. She will trade you 1 ox.

#### Talk to People

- A stranger tells you:
    - "Can't afford to take a ferry We're making our wagon into a boat. We'll turn it over, caulk the bottom and sides with pitch, and use it to float our goods across. Have to swim the animals. Hope it doesn't rain -- the river's high enough!"
- A ferry operator tells you:
    - "Don't try to ford any river deeper than the wagon bed -- about two and a half feet. You'll swamp your wagon and lose your supplies. You can caulk the wagon bed and float it -- or be smart and hire me to take your wagon on my ferry!"
- Aunt Rebecca Sims tells you:
    - "With the crowds of people waiting to get on the ferry, we could be stranded here for days! Hope there's enough graze for all those animals -- not many people carry feed! I'd rather wait, though, than cross in a rickety wagon boat!"

### **Big Blue River**
- weather: cool/warm
- width: between 221-248 feet wide
- depth: between 1.1-4.8 feet deep

Choices:
- ford
- caulk/float
- wait (between 1-6 days)

#### Attempt to Trade

- You meet another emigrant who wants 1 ox. He will trade you 135 bullets.
- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon tongue. She will trade you 1 set of clothing.
- You meet another emigrant who wants 1 wagon axle. He will trade you 1 set of clothing.

#### Talk to People

- A lady, Marnie Stewart, tells you:
    - "This prairie is mighty pretty with all the wild flowers, and tall grasses. But there's too much of it! I miss not having a town nearby. I wonder how many days until I see a town -- a town with real shops, a church, people..."
- Big Louie, a trail driver, tells you:
    - "Be careful you don't push those animals too hard! Keep 'em moving but set them a fair pace. Can't keep driving 'em so fast or you'll end up with lame-footed animals. A lame ox is about as good to you as a dead one!"
- A party leader heading east tells you:
    - "We've had enough! Pesky flies all day and mosquitoes all night! It's either baking sun or oceans of mud -- and sometimes both. Worry over Indians attacking -- haven't seen any yet, but still a worry."

### **Fort Kearney**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 54 bullets.
- You meet another emigrant who wants 1 ox. He will trade you 81 pounds of food.

#### Talk to People

- A fort soldier tells you:
    - "The trials from the jumping off places -- Independence, St. Joseph, Council Bluffs -- come together at Fort Kearney. This new fort was built by the U.S. Army to protect those bound for California and Oregon."
- Big Louie tells you:
    - "The Platte River valley forms a natural roadway from Fort Kearney to Fort Laramie. Travelers bound for California, Utah, and Oregon all takes this road. Could be the easiest stretch of the whole trip. Should see antelope and plenty of buffalo."
- A Fort Kearney scout tells you:
    - "The game is still plentiful along here, but gettin' harder to find. Wish so many overlanders, I don't expect it to last more'n a few years. Folks shoot the game for sport, take a small piece, and let the rest rot in the sun."

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $25.00 | per ox |
| Clothing | $12.50 | per set |
| Ammunition | $2.50 | per box of 20 |
| Wagon wheels | $12.50 | per wheel |
| Wagon axles | $12.50 | per axle |
| Wagon tongues | $12.50 | per tongue |
| Food | $0.25 | per pound |

### **Chimney Rock**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon wheel. She will trade you 50 bullets.
- You meet another emigrant who wants 2 wagon wheels. She will trade you 1 ox.
- You meet another emigrant who wants 1 wagon wheel. He will trade you 23 pounds of food.
- You meet another emigrant who wants 4 sets of clothing. He will trade you 1 ox.

#### Talk to People

- Alonzo Delano tells you:
    - "About noon yesterday we came in sight of Chimney Rock looming up in the distance like the lofty tower of some town. We did not tire gazing on it. It was about 20 miles from us, and stayed in sight 'til we reached it today."
- Aunt Rebecca Sims tells you:
    - "I hear terrible stories about wagon parties running out of food before Oregon -- the whole party starving to death. We must check our supplies often; we might not get there as soon as we think. Always plan for the worst, I say."
- Celinda Hines tells you:
    - "Chimney Rock by moonlight is awfully sublime. Many Indians came to our wagon with fish to exchange for clothing. We bought a number. They understand 'swap' and 'no swap'. Seem most anxious to get shirts and socks."

### **Fort Laramie**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 4 wagon wheels. You don't have this.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 28 pounds of food.
- You meet another emigrant who wants 1 wagon wheel. She will trade you 1 set of clothing.

#### Talk to People

- A mountain man tells you:
    - "These greenhorns heading across the Rockies know nothing about surviving in the mountains. It gets awful cold up there, even in summer. Many a traveler crossing the mountains too late in the year has gotten snowbound and died!"
- A Sioux brave tells you:
    - "The Pawnee are the mortal enemies of the Sioux. I would not hesitate to kill any Pawnee I met. But I have never killed a white man. All I ask from the white man is to leave me alone, and to leave my buffalo alone."
- A woman traveler tells you:
    - "Be warned, stranger. Don't dig a water hole! Drink only river water. Salty as the Platte River is -- it's better than cholera. We buried my husband last week. Could use some help with this harness, if you can spare the time."

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $30.00 | per ox |
| Clothing | $15.00 | per set |
| Ammunition | $3.00 | per box of 20 |
| Wagon wheels | $15.00 | per wheel |
| Wagon axles | $15.00 | per axle |
| Wagon tongues | $15.00 | per tongue |
| Food | $0.30 | per pound |

### **Independence Rock**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon wheel. He will trade you 27 pounds of food.
- You meet another emigrant who wants 1 set of clothing. He will trade you 35 pounds of food.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 1 set of clothing.
- You meet another emigrant who wants 2 wagon wheels. He will trade you 1 ox.

#### Talk to People

- Aunt Rebecca Sims tells you:
    - "No butter or cheese or fresh fruit since Fort Laramie! Bless me, but I'd rather have my larder full of food back East than have our names carved on that rock! Well, tis a sight more cheery than all the graves we passed."
- Big Louie tells you:
    - "Goodbye Platte River! Goodbye sand hills and white buffalo skulls! Now we climb the Sweetwater valley to cross the Continental Divide at South Pass. Once across the Rockies, we'll make a steep descent into the Green River valley."
- A young boy tells you:
    - "I carved my name way up the side of Independence Rock, near the top. There are hundreds of names up there! The oldest ones were carved by mountain men and fur trappers -- famous names like Fremont, Bonneville, and DeSmet!"

### **South Pass**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 ox. She will trade you 95 bullets.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 49 pounds of food.
- You meet another emigrant who wants 2 wagon tongues. She will trade you 1 set of clothing.

#### Talk to People

- A Mormon traveler tells you:
    - "My family and I travel with 40 other families to the valley of the Great Salt Lake to seek religious freedom. Back east, Mormons are prosecuted. In Utah, we'll join together to build a new community, changing desert into farm land."
- An Arapaho Indian tells you:
    - "When the white man first crossed out lands their wagons were few. Now they crowd the trail in great numbers. The land is overgrazed with their many animals. Do any white men still live in the East? My people talk of moving."
- A young girl tells you:
    - "My father is very sick and we are resting here until he gets better. We have been pushing too hard and our health has suffered. When my father is able to travel again, we will go at a slower pace."

**The trail divides here. You may:**
- 1. head for Green River crossing
- 2. head for Fort Bridger
- 3. see the map

What is your choice?

### **Green River Crossing**
- weather: warm/hot
- width: between 404-438 feet wide
- depth: between 20.6-25.1 feet deep

Choices:
- ford
- caulk/float
- ferry ($5 plus 2-6 days wait)
- wait (between 1-6 days)

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 144 bullets. He will trade you 1 set of clothing.
- You meet another emigrant who wants 1 set of clothing. He will trade you 62 bullets.
- You meet another emigrant who wants 3 wagon wheels. You don't have this.
- You meet another emigrant who wants 3 sets of clothing. He will trade you 1 ox.
- You meet another emigrant who wants 2 wagon wheels. He will trade you 1 set of clothing.

#### Talk to People

- Big Louie tells you:
    - "Five dollars to ferry us over the Green River? Those ferrymen'll make a hundred dollars before breakfast! We'll keep down river until we find a place to ford our wagon and animals. What little money we have left, we'll keep!"
- A young boy tells you:
    - "My family didn't buy enough food in Independence. We have been eating very small rations since Fort Laramie. Because of that our health is poor. My sister has mountain fever, so we're stopped here for a while."
- A Shoshoni Indian tells you:
    - "When wagons first started coming through here, we did not mind. We even found it good to trade game and fish with the travelers and help them cross the rivers. Now there are too many white men and too little land for gazing."

### **Fort Bridger**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 4 wagon wheels. You don't have this.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 28 pounds of food.
- You meet another emigrant who wants 1 wagon wheel. She will trade you 1 set of clothing.

#### Talk to People

- Aunt Rebecca Sims tells you:
    - "We should've taken the Sublette Cutoff! Not enough at this fort worth the time it took to get here. And the outrageous prices! Food's not fit to eat, much less pay for. Some folks'd sell the clothes off our backs if we'd let them!"
- A tired-looking woman tells you:
    - "One child drowned in a swollen creek east of Fort Laramie. My husband died of typhoid near Independence Rock. Now I travel alone with my five children. The eldest, Caleb, is eleven. I fear he'll be a man before we reach Oregon."
- A trader tells you:
    - "This fort was built by Jim Bridger. Jim was a mountain man before he put in this blacksmith shop and small store to supply the overlanders. Does a big trade in horses, Jim and his partner, Vasquez."

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $35.00 | per ox |
| Clothing | $17.50 | per set |
| Ammunition | $3.50 | per box of 20 |
| Wagon wheels | $17.50 | per wheel |
| Wagon axles | $17.50 | per axle |
| Wagon tongues | $17.50 | per tongue |
| Food | $0.35 | per pound |

### **Soda Springs**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 ox. He will trade you 112 bullets.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 49 pounds of food.
- You meet another emigrant who wants 2 wagon tongues. She will trade you 1 set of clothing.

#### Talk to People

- Celinda Hines tells you:
    - "My, the Soda Springs are so pretty! Seem to spout at regular intervals. Felt good to just rest and not be jostled in the wagon all day. When I get to Oregon, I'll have a soft feather bed and never sleep in a wagon again!"
- A young boy tells you:
    - "My job every day is to find wood for the cook fire. Sometimes it's very hard to find enough, so I store extra pieces in a box under the wagon. On the prairie I gather buffalo chips to burn when there wasn't any wood."
- Miles Hendrick tells you:
    - "I've heard it said that there are many cutoffs to take to shorten the journey -- that by taking all the shortcuts, you can save many days on the trail. And why not? Saving time and provisions is worth the risk!"

### **Fort Hall**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 ox. He will trade you 54 pounds of food.
- You meet another emigrant who wants 1 wagon tongue. You don't have this.

#### Talk to People

- Aunt Rebecca Sims tells you:
    - "Hear there's mountain sheep around here. Enough water too, buy hardly a stick of wood. Thank heaven for Fort Hall! But I'm real sorry to be saying goodbye to cousin Miles and all the folks heading for California."
- A fellow traveler tells you:
    - "Fort Hall is a busy fort! The wide stretches of meadow grass here are just what our tired animals need. As for me, I'll fix up the wagon leaks. Amanda's real anxious to wash all the clothes and linens in one of those clear streams."
- Miles Hendrick tells you:
    - "Well, friend, this is where we part. I'm bound for California with an imposing desert to cross. And you -- you've got the Snake River to cross, which I hear is no picnic! Write us, you or the Missus, just as soon as you reach Oregon!"

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $40.00 | per ox |
| Clothing | $20.00 | per set |
| Ammunition | $4.00 | per box of 20 |
| Wagon wheels | $20.00 | per wheel |
| Wagon axles | $20.00 | per axle |
| Wagon tongues | $20.0 | per tongue |
| Food | $0.40 | per pound |

### **Snake River**
- weather: cool/cold
- width: between 1000-1016 feet wide
- depth: between 6.0-8.1 feet deep

Choices:
- ford
- caulk/float
- indian (3 sets of clothing mostly, but once I got it for 2 sets only!)
- wait (between 1-6 days)

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 144 bullets. He will trade you 1 set of clothing.
- You meet another emigrant who wants 1 set of clothing. He will trade you 62 bullets.
- You meet another emigrant who wants 3 wagon wheels. You don't have this.
- You meet another emigrant who wants 3 sets of clothing. He will trade you 1 ox.
- You meet another emigrant who wants 2 wagon wheels. He will trade you 1 set of clothing.

#### Talk to People

- Big Louie tells you:
    - "See that wild river? That's the Snake. Many a craft's been swamped in her foaming rapids. Her waters travel all the way to Oregon! We'll be crossing her soon, and then again after Fort Boise. Take care at the crossing!"
- A frantic wife tells you:
    - "It says right here in the Shively guidebook: "You must hire an Indian to pilot you at the crossings of the Snake river, it being dangerous if not perfectly understood." But my husband insists on crossing without a guide!"
- An overlander tells you:
    - "Down there between those steep lava gorges, twisting and writhing, is the Snake River. So much water -- and so hard to get to! We've got many miles of desert before Oregon, so be sure to fill your water kegs at the crossing!"

### **Fort Boise**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon axle. He will trade you 75 bullets.
- You meet another emigrant who wants 1 wagon tongue. You don't have this.

#### Talk to People

- A trader with 6 mules tells you:
    - "You'll not get your wagon over them Blue Mountains, mister. Leave it! Cross yer goods over with pack animals. Get yerself a couple of good mules. Pieces of wagon litter the trail -- left by them folks who don't heed good advice!"
- Aunt Rebecca tells you:
    - "At every fort along the trail, prices have been higher than at the previous fort! This is outrageous! They're taking advantage of us! If I had the chance to do it again, I'd buy more supplies in Independence."
- Jacob Hofsteader tells you:
    - "Every night, even though I ache from the day's toils, my head is filled with dreams of the rich farm land of the Willamette Valley. I will build myself a fine, handsome homestead -- and I'm certain I'll be rich within five years."

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $45.00 | per ox |
| Clothing | $22.50 | per set |
| Ammunition | $4.50 | per box of 20 |
| Wagon wheels | $22.50 | per wheel |
| Wagon axles | $22.50 | per axle |
| Wagon tongues | $22.50 | per tongue |
| Food | $0.45 | per pound |

### **Blue Mountains**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon tongue. He will trade you 47 bullets.
- You meet another emigrant who wants 4 wagon tongues. You don't have this.
- You meet another emigrant who wants 147 bullets. She will trade you 1 wagon axle.
- You meet another emigrant who wants 1 set of clothing. He will trade you 1 wagon wheel.

#### Talk to People

- A tired overlander tells you:
    - "Since crossing the Snake at Fort Boise, it's been just mountains and desert. Dust deeper each day -- six inches at times. No tracks, just clouds of dust. Many cattle choked on the dust after swimming the river, then bled and died."
- Marnie Stewart tells you:
    - "We followed the edge of the desert from Fort Boise to the forbidding wall of the Blue Mountains. The hills were dreadful steep! Locking both wheels and coming down slow, we got down safe. Poor animals! No grass or water for days."
- Jacob Hofsteader tells you:
    - "This valley of the Grande Ronde is the most beautiful sight I've seen in months. Water and graze in abundance! And if this valley is so fine, the Willamette must be twice as fine! We'll be sittin' pretty in our new homestead!"

**The trail divides here. You may:**
- 1. head for Fort Walla Walla
- 2. head for The Dalles
- 3. see the map

What is your choice?

### **Fort Walla Walla**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 1 wagon axle. He will trade you 75 bullets.
- You meet another emigrant who wants 1 wagon tongue. You don't have this.

#### Talk to People

- A Cayuse Indian tells you:
    - "You ask about the Whitman massacre. I ask you why Doctor Whitman's medicines did not cure my people's children? Many caught the measles from the strangers. Why did the medicine poison our children and cure the children of white people?"
- A young mother tells you:
    - "I've traveled in fear of Indians since our journey began. As of yet we've seen few. Those we met helped us cross rivers or sold us vegetables. Still I fear. I've read grave markers and heard stories of killings in these mountains."
- Amy Witherspoon tells you:
    - "My cousin Catherine was one of six children orphaned and left at Whitman's Mission. Lived with them for three years -- until the massacre last November. She has survived snakebites, stampedes, falls, fights -- not to mention a massacre."

#### Buy Supplies
| Resource | Price | Amount |
| --- | --- | --- |
| Oxen | $50.00 | per ox |
| Clothing | $25.00 | per set |
| Ammunition | $5.00 | per box of 20 |
| Wagon wheels | $25.00 | per wheel |
| Wagon axles | $25.00 | per axle |
| Wagon tongues | $25.00 | per tongue |
| Food | $0.50 | per pound |

### **The Dalles**

#### Attempt to Trade

- No one wants to trade with you today.
- You meet another emigrant who wants 130 bullets. He will trade you 1 wagon axle.
- You meet another emigrant who wants 189 pounds of food. She will trade you 1 ox.
- You meet another emigrant who wants 1 set of clothing. He will trade you 26 pounds of food.
- You meet another emigrant who wants 147 bullets. She will trade you 1 wagon axle.

#### Talk to People

- Amy Witherspoon tells you:
    - "My cousin Lydia engaged passage down the Columbia with Indians -- a canoe with 17 people and luggage! The wind blew so heavy they had to lay by. Near dark, high waves came up over their heads! Finally, they made it to shore safely."
- A toll collector tells you:
    - "I collect the tolls for the Barlow Road -- a bargain at twice the price! Until last year the overlander had no choice -- everyone floated the Columbia. Now with Mr. Barlow's new road, you can drive your wagon right into Oregon City!"
- A mountain man tells you:
    - "These last hundred miles to the Willamette Valley are the roughest -- either rafting down the swift and turbulent Columbia River or driving your wagon over the steep Cascade Mountains. Hire an Indian guide if you take the river."

**The trail divides here. You may:**
- 1. float down the Columbia River
- 2. take the Barlow Toll Road

What is your choice?

- Floating requires using keys, which might not work well in this Python application.
- Hitting a rock causes heavy loss (2 drowned, 4 oxen, large amounts of clothing/bullets/spare parts/food)

- Toll road still requires 100 miles of travel, so you'll need plenty of food/etc.
- The toll road fee varies (randomized: $12-$14, but have seen down to $8 and up to $20).
- If you select "no" to pay it, the price doesn't change.

### **Willamette Valley, Oregon**

If you get to the end and your points aren't enough to make the top 10,
then you get the following message:

You have accumulated XXXX points.
This is not enough to qualify for
the Oregon Top Ten.

---

## Scoring

On arriving in Oregon, your most important resources is the people you have with you.
You receive points for each member of your party who arrives safely;
you receive more points if they arrive in good health!

| Health of Party | Points per Person |
| --- | :---: |
| good | 500 |
| fair | 400 |
| poor | 300 |
| very poor | 200 |

On arriving in Oregon, the resources you arrive with will help you get started in the new land.
You receive points for each item you bring safely to Oregon.

| Resources of Party | Points per Item |
| --- | :---: |
| wagon | 50 |
| ox | 4 |
| spare wagon part | 2 |
| set of clothing | 2 |
| bullets (each 50) | 1 |
| food (each 25 pounds) | 1 |
| cash (each 5 dollars) | 1 |

On arriving in Oregon, you receive points for your occupation in the new land.
Because more farmers and carpenters were needed than bankers, you receive **double** points upon
arriving in Oregon as a carpenter, and **triple** points for arriving as a farmer.

---

## Credits

| Source (URL) | Notes |
| --- | --- |
| [fontspace](https://www.fontspace.com/category/oregon-trail) | The Oregon Trail logo |
| [Wikimedia](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png) | Python logo |
| [text-image](https://www.text-image.com/convert/ascii.html) | ASCII ox/wagon |
| [StackOverflow](https://stackoverflow.com/a/45391019) | Centering text 80-wide |
| [StackOverflow](https://stackoverflow.com/a/2084628) | Clearing the terminal |

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