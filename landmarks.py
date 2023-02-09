from utils import CENT


landmarks = [
    {
        "id": "L01",
        "name": "Independence, Missouri",
        "category": "start",
        "weather_zone": 1,
        "next_destination_id": "L02",
        "next_destination_name": "Kansas River crossing",
        "next_destination_distance": 102,
        "conversations": [
            {
                "person": "a town resident",
                "speech": f"""
{CENT("Some folks seem to think that")}
{CENT("two oxen are enough to get them to Oregon!")}
{CENT("Two oxen can barely move a fully loaded wagon,")}
{CENT("and if one of them gets sick or dies,")}
{CENT("you won't be going anywhere.")}
{CENT("I wouldn't go overland with less than six.")}
                """
            },
            {
                "person": "a trader named Jim",
                "speech": f"""
{CENT("Better take extra sets of clothing.")}
{CENT("Trade 'em to Indians for fresh vegetables, fish, or meat.")}
{CENT("It's well worth hiring an Indian guide at river crossings.")}
{CENT("Expect to pay them!")}
{CENT("They're sharp traders, not easily cheated.")}
                """
            },
            {
                "person": "a traveler named Miles Hendricks",
                "speech": f"""
{CENT("Did you read the Missouri Republican today?")}
{CENT("Says some folk start for Oregon without carrying spare parts,")}
{CENT("not even an extra wagon axle.")}
{CENT("Must think they grow on trees!")}
{CENT("Hope they're lucky enough to find an abandoned wagon.")}
                """
            }
        ],
        "cost_oxen": 20.00,
        "cost_food": 0.20,
        "cost_clothing": 10.00,
        "cost_bullets": 2.00,
        "cost_wagon_wheels": 10.00,
        "cost_wagon_axles": 10.00,
        "cost_wagon_tongues": 10.00
    },



    {
        "id": "L02",
        "name": "Kansas River crossing",
        "category": "river",
        "weather_zone": 1,
        "next_destination_id": "L03",
        "next_destination_name": "Big Blue River crossing",
        "next_destination_distance": 82,
        "can_hire_ferry": True,
        "can_hire_indian": False,
        "depth_min": 2.2,
        "depth_max": 7.4,
        "width_min": 0,
        "width_max": 0,
        "swiftness": 0,
        "bottom_type": "",
        "conversations": [
            {
                "person": "a stranger",
                "speech": f"""
{CENT("Can't afford to take a ferry.")}
{CENT("We're making our wagon into a boat.")}
{CENT("We'll turn it over, caulk the bottom and sides with pitch,")}
{CENT("and use it to float our goods across.")}
{CENT("Have to swim the animals.")}
{CENT("Hope it doesn't rain -- the river's high enough!")}
                """
            },
            {
                "person": "a ferry operator",
                "speech": f"""
{CENT("Don't try to ford any river deeper than the wagon bed;")}
{CENT("about two and a half feet.")}
{CENT("You'll swamp your wagon and lose your supplies.")}
{CENT("You can caulk the wagon bed and float it,")}
{CENT("or be smart and hire me to take your wagon on my ferry!")}
                """
            },
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("With the crowds of people waiting to get on the ferry,")}
{CENT("we could be stranded here for days!")}
{CENT("Hope there's enough graze for all those animals.")}
{CENT("Not many people carry feed!")}
{CENT("I'd rather wait, though, than cross in a rickety wagon boat!")}
                """
            }
        ]
    },



    {
        "id": "L03",
        "name": "Big Blue River crossing",
        "category": "river",
        "weather_zone": 1,
        "next_destination_id": "L04",
        "next_destination_name": "Fort Kearney",
        "next_destination_distance": 118,
        "can_hire_ferry": False,
        "can_hire_indian": False,
        "depth_min": 0,
        "depth_max": 0,
        "width_min": 0,
        "width_max": 0,
        "swiftness": 0,
        "bottom_type": "",
        "conversations": [
            {
                "person": "a lady, Marnie Stewart",
                "speech": f"""
{CENT("This prairie is mighty pretty with all the wild flowers,")}
{CENT("and tall grasses. But there's too much of it!")}
{CENT("I miss not having a town nearby.")}
{CENT("I wonder how many days until I see a town;")}
{CENT("a town with real shops, a church, people...")}
                """
            },
            {
                "person": "Big Louie, a trail driver",
                "speech": f"""
{CENT("Be careful you don't push those animals too hard!")}
{CENT("Keep 'em moving, but set them a fair pace.")}
{CENT("Can't keep driving 'em so fast, or you'll")}
{CENT("end up with lame-footed animals.")}
{CENT("A lame ox is about as good to you as a dead one!")}
                """
            },
            {
                "person": "a party leader heading east",
                "speech": f"""
{CENT("We've had enough! Pesky flies all day and mosquitoes all night!")}
{CENT("It's either baking sun, or oceans of mud, and sometimes both.")}
{CENT("Worry over Indians attacking...")}
{CENT("haven't seen any yet, but still a worry.")}
                """
            }
        ]
    },



    {
        "id": "L04",
        "name": "Fort Kearney",
        "category": "fort",
        "weather_zone": 2,
        "next_destination_id": "L05",
        "next_destination_name": "Chimney Rock",
        "next_destination_distance": 250,
        "conversations": [
            {
                "person": "a fort soldier",
                "speech": f"""
{CENT("The trials from the jumping off places,")}
{CENT("Independence, St. Joseph, Council Bluffs,")}
{CENT("come together at Fort Kearney.")}
{CENT("This new fort was built by the U.S. Army to")}
{CENT("protect those bound for California and Oregon.")}
                """
            },
            {
                "person": "Big Louie",
                "speech": f"""
{CENT("The Platte River valley forms a natural roadway")}
{CENT("from Fort Kearney to Fort Laramie. Travelers bound for")}
{CENT("California, Utah, and Oregon all takes this road.")}
{CENT("Could be the easiest stretch of the whole trip.")}
{CENT("Should see antelope and plenty of buffalo.")}
                """
            },
            {
                "person": "a Fort Kearney scout",
                "speech": f"""
{CENT("The game is still plentiful along here, but gettin' harder to find.")}
{CENT("With so many overlanders, I don't expect it to last more'n a few years.")}
{CENT("Folks shoot the game for sport, take a small piece,")}
{CENT("and let the rest rot in the sun.")}
                """  # noqa
            }
        ],
        "cost_oxen": 25.00,
        "cost_food": 0.25,
        "cost_clothing": 12.50,
        "cost_bullets": 2.50,
        "cost_wagon_wheels": 12.50,
        "cost_wagon_axles": 12.50,
        "cost_wagon_tongues": 12.50
    },



    {
        "id": "L05",
        "name": "Chimney Rock",
        "category": "misc",
        "weather_zone": 2,
        "next_destination_id": "L06",
        "next_destination_name": "Fort Laramie",
        "next_destination_distance": 86,
        "conversations": [
            {
                "person": "Alonzo Delano",
                "speech": f"""
{CENT("About noon yesterday, we came in sight of Chimney Rock")}
{CENT("looming up in the distance like the lofty tower of some town.")}
{CENT("We did not tire gazing on it.")}
{CENT("It was about 20 miles from us,")}
{CENT("and stayed in sight 'til we reached it today.")}
                """
            },
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("I hear terrible stories about wagon parties running")}
{CENT("out of food before Oregon -- the whole party starving to death.")}
{CENT("We must check our supplies often;")}
{CENT("we might not get there as soon as we think.")}
{CENT("Always plan for the worst, I say.")}
                """
            },
            {
                "person": "Celinda Hines",
                "speech": f"""
{CENT("Chimney Rock by moonlight is awfully sublime.")}
{CENT("Many Indians came to our wagon with fish to exchange for clothing.")}
{CENT("We bought a number. They understand 'swap' and 'no swap'.")}
{CENT("Seem most anxious to get shirts and socks.")}
                """
            }
        ]
    },



    {
        "id": "L06",
        "name": "Fort Laramie",
        "category": "fort",
        "weather_zone": 3,
        "next_destination_id": "L07",
        "next_destination_name": "Independence Rock",
        "next_destination_distance": 190,
        "conversations": [
            {
                "person": "a mountain man",
                "speech": f"""
{CENT("These greenhorns heading across the Rockies know")}
{CENT("nothing about surviving in the mountains.")}
{CENT("It gets awful cold up there, even in summer.")}
{CENT("Many a traveler crossing the mountains too late in the year")}
{CENT("has gotten snowbound and died!")}
                """
            },
            {
                "person": "a Sioux brave",
                "speech": f"""
{CENT("The Pawnee are the mortal enemies of the Sioux.")}
{CENT("I would not hesitate to kill any Pawnee I met.")}
{CENT("But I have never killed a white man.")}
{CENT("All I ask from the white man is to leave me alone,")}
{CENT("and to leave my buffalo alone.")}
                """
            },
            {
                "person": "a woman traveler",
                "speech": f"""
{CENT("Be warned, stranger.")}
{CENT("Don't dig a water hole! Drink only river water.")}
{CENT("Salty as the Platte River is, it's better than cholera.")}
{CENT("We buried my husband last week.")}
{CENT("Could use some help with this harness, if you can spare the time.")}
                """
            }
        ],
        "cost_oxen": 30.00,
        "cost_food": 0.30,
        "cost_clothing": 15.00,
        "cost_bullets": 3.00,
        "cost_wagon_wheels": 15.00,
        "cost_wagon_axles": 15.00,
        "cost_wagon_tongues": 15.00
    },



    {
        "id": "L07",
        "name": "Independence Rock",
        "category": "misc",
        "weather_zone": 3,
        "next_destination_id": "L08",
        "next_destination_name": "South Pass",
        "next_destination_distance": 102,
        "conversations": [
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("No butter or cheese or fresh fruit since Fort Laramie!")}
{CENT("Bless me, but I'd rather have my larder full of food")}
{CENT("back East, than have our names carved on that rock!")}
{CENT("Well, tis a sight more cheery than all the graves we passed.")}
                """
            },
            {
                "person": "Big Louie",
                "speech": f"""
{CENT("Goodbye Platte River!")}
{CENT("Goodbye sand hills and white buffalo skulls!")}
{CENT("Now we climb the Sweetwater valley to cross the")}
{CENT("Continental Divide at South Pass. Once across the Rockies,")}
{CENT("we'll make a steep descent into the Green River valley.")}
                """
            },
            {
                "person": "a young boy",
                "speech": f"""
{CENT("I carved my name way up the side of Independence Rock, near the top.")}
{CENT("There are hundreds of names up there!")}
{CENT("The oldest ones were carved by mountain men and fur trappers.")}
{CENT("Famous names like Fremont, Bonneville, and DeSmet!")}
                """
            }
        ]
    },



    {
        "id": "L08",
        "name": "South Pass",
        "category": "misc",
        "weather_zone": 4,
        "next_destination_id": ["L09", "L10"],
        "next_destination_name": ["Green River crossing", "Fort Bridger"],
        "next_destination_distance": [57, 125],
        "conversations": [
            {
                "person": "a Mormon traveler",
                "speech": f"""
{CENT("My family and I travel with 40 other families to the")}
{CENT("valley of the Great Salt Lake to seek religious freedom.")}
{CENT("Back east, Mormons are prosecuted.")}
{CENT("In Utah, we'll join together to build a new community,")}
{CENT("changing desert into farm land.")}
                """
            },
            {
                "person": "an Arapaho Indian",
                "speech": f"""
{CENT("When the white man first crossed out lands, their wagons were few.")}
{CENT("Now they crowd the trail in great numbers.")}
{CENT("The land is overgrazed with their many animals.")}
{CENT("Do any white men still live in the East?")}
{CENT("My people talk of moving.")}
                """
            },
            {
                "person": "a young girl",
                "speech": f"""
{CENT("My father is very sick, and we are resting here until he gets better.")}
{CENT("We have been pushing too hard, and our health has suffered.")}
{CENT("When my father is able to travel again, we will go at a slower pace.")}
                """
            }
        ]
    },



    {
        "id": "L09",
        "name": "Green River crossing",
        "category": "river",
        "weather_zone": 4,
        "next_destination_id": "L11",
        "next_destination_name": "Soda Springs",
        "next_destination_distance": 143,
        "can_hire_ferry": True,
        "can_hire_indian": False,
        "depth_min": 0,
        "depth_max": 0,
        "width_min": 0,
        "width_max": 0,
        "swiftness": 0,
        "bottom_type": "",
        "conversations": [
            {
                "person": "Big Louie",
                "speech": f"""
{CENT("Five dollars to ferry us over the Green River?")}
{CENT("Those ferrymen'll make a hundred dollars before breakfast!")}
{CENT("We'll keep down river until we find a place")}
{CENT("to ford our wagon and animals.")}
{CENT("What little money we have left, we'll keep!")}
                """
            },
            {
                "person": "a young boy",
                "speech": f"""
{CENT("My family didn't buy enough food in Independence.")}
{CENT("We have been eating very small rations since Fort Laramie.")}
{CENT("Because of that, our health is poor.")}
{CENT("My sister has mountain fever, so we're stopped here for a while.")}
                """
            },
            {
                "person": "a Shoshoni Indian",
                "speech": f"""
{CENT("When wagons first started coming through here, we did not mind.")}
{CENT("We even found it good to trade game and fish with the travelers,")}
{CENT("and help them cross the rivers.")}
{CENT("Now there are too many white men, and too little land for grazing.")}
{CENT("")}
                """
            }
        ]
    },



    {
        "id": "L10",
        "name": "Fort Bridger",
        "category": "fort",
        "weather_zone": 4,
        "next_destination_id": "L11",
        "next_destination_name": "Soda Springs",
        "next_destination_distance": 162,
        "conversations": [
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("We should've taken the Sublette Cutoff!")}
{CENT("Not enough at this fort worth the time it took to get here.")}
{CENT("And the outrageous prices! Food's not fit to eat, much less pay for.")}
{CENT("Some folks'd sell the clothes off our backs if we'd let them!")}
                """
            },
            {
                "person": "a tired-looking woman",
                "speech": f"""
{CENT("One child drowned in a swollen creek east of Fort Laramie.")}
{CENT("My husband died of typhoid near Independence Rock.")}
{CENT("Now I travel alone with my five children.")}
{CENT("The eldest, Caleb, is eleven.")}
{CENT("I fear he'll be a man before we reach Oregon.")}
                """
            },
            {
                "person": "a trader",
                "speech": f"""
{CENT("This fort was built by Jim Bridger.")}
{CENT("Jim was a mountain man before he put in this blacksmith shop")}
{CENT("and small store to supply the overlanders.")}
{CENT("Does a big trade in horses, Jim and his partner, Vasquez.")}
                """
            }
        ],
        "cost_oxen": 35.00,
        "cost_food": 0.35,
        "cost_clothing": 17.50,
        "cost_bullets": 3.50,
        "cost_wagon_wheels": 17.50,
        "cost_wagon_axles": 17.50,
        "cost_wagon_tongues": 17.50
    },



    {
        "id": "L11",
        "name": "Soda Springs",
        "category": "misc",
        "weather_zone": 4,
        "next_destination_id": "L12",
        "next_destination_name": "Fort Hall",
        "next_destination_distance": 57,
        "conversations": [
            {
                "person": "Celinda Hines",
                "speech": f"""
{CENT("My, the Soda Springs are so pretty!")}
{CENT("Seem to spout at regular intervals.")}
{CENT("Felt good to just rest and not be jostled in the wagon all day.")}
{CENT("When I get to Oregon, I'll have a soft feather bed")}
{CENT("and never sleep in a wagon again!")}
                """
            },
            {
                "person": "a young boy",
                "speech": f"""
{CENT("My job every day is to find wood for the cook fire.")}
{CENT("Sometimes it's very hard to find enough,")}
{CENT("so I store extra pieces in a box under the wagon.")}
{CENT("On the prairie, I gather buffalo chips")}
{CENT("to burn when there wasn't any wood.")}
                """
            },
            {
                "person": "Miles Hendrick",
                "speech": f"""
{CENT("I've heard it said that there are many cutoffs")}
{CENT("to take to shorten the journey; that by taking all the shortcuts,")}
{CENT("you can save many days on the trail.")}
{CENT("And why not?")}
{CENT("Saving time and provisions is worth the risk!")}
                """
            }
        ]
    },



    {
        "id": "L12",
        "name": "Fort Hall",
        "category": "fort",
        "weather_zone": 5,
        "next_destination_id": "L13",
        "next_destination_name": "Snake River crossing",
        "next_destination_distance": 182,
        "conversations": [
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("Hear there's mountain sheep around here.")}
{CENT("Enough water too, but hardly a stick of wood.")}
{CENT("Thank heavens for Fort Hall!")}
{CENT("But I'm real sorry to be saying goodbye to")}
{CENT("cousin Miles, and all the folks heading for California.")}
                """
            },
            {
                "person": "a fellow traveler",
                "speech": f"""
{CENT("Fort Hall is a busy fort!")}
{CENT("The wide stretches of meadow grass here are just what our")}
{CENT("tired animals need. As for me, I'll fix up the wagon leaks.")}
{CENT("Amanda's real anxious to wash all the clothes")}
{CENT("and linens in one of those clear streams.")}
                """
            },
            {
                "person": "Miles Hendrick",
                "speech": f"""
{CENT("Well, friend, this is where we part.")}
{CENT("I'm bound for California with an imposing desert to cross.")}
{CENT("And you've got the Snake River to cross, which I hear is no picnic!")}
{CENT("Write us, you or the Missus, just as soon as you reach Oregon!")}
                """
            }
        ],
        "cost_oxen": 40.00,
        "cost_food": 0.40,
        "cost_clothing": 20.00,
        "cost_bullets": 4.00,
        "cost_wagon_wheels": 20.00,
        "cost_wagon_axles": 20.00,
        "cost_wagon_tongues": 20.00
    },



    {
        "id": "L13",
        "name": "Snake River crossing",
        "category": "river",
        "weather_zone": 5,
        "next_destination_id": "L14",
        "next_destination_name": "Fort Boise",
        "next_destination_distance": 113,
        "can_hire_ferry": False,
        "can_hire_indian": True,
        "depth_min": 0,
        "depth_max": 0,
        "width_min": 0,
        "width_max": 0,
        "swiftness": 0,
        "bottom_type": "",
        "conversations": [
            {
                "person": "Big Louie",
                "speech": f"""
{CENT("See that wild river? That's the Snake.")}
{CENT("Many a craft's been swamped in her foaming rapids.")}
{CENT("Her waters travel all the way to Oregon!")}
{CENT("We'll be crossing her soon, and then again after Fort Boise.")}
{CENT("Take care at the crossing!")}
                """
            },
            {
                "person": "a frantic wife",
                "speech": f"""
{CENT("It says right here in the Shively guidebook:")}
{CENT('"You must hire an Indian to pilot you at')}
{CENT("the crossings of the Snake river,")}
{CENT('it being dangerous if not perfectly understood."')}
{CENT("But my husband insists on crossing without a guide!")}
                """
            },
            {
                "person": "an overlander",
                "speech": f"""
{CENT("Down there between those steep lava gorges,")}
{CENT("twisting and writhing, is the Snake River.")}
{CENT("So much water, and so hard to get to!")}
{CENT("We've got many miles of desert before Oregon,")}
{CENT("so be sure to fill your water kegs at the crossing!")}
                """
            }
        ]
    },



    {
        "id": "L14",
        "name": "Fort Boise",
        "category": "fort",
        "weather_zone": 5,
        "next_destination_id": "L15",
        "next_destination_name": "Blue Mountains",
        "next_destination_distance": 160,
        "conversations": [
            {
                "person": "a trader with 6 mules",
                "speech": f"""
{CENT("You'll not get your wagon over them Blue Mountains, mister.")}
{CENT("Leave it! Cross yer goods over with pack animals.")}
{CENT("Get yerself a couple of good mules.")}
{CENT("Pieces of wagon litter the trail,")}
{CENT("left by them folks who don't heed good advice!")}
                """
            },
            {
                "person": "Aunt Rebecca Sims",
                "speech": f"""
{CENT("At every fort along the trail,")}
{CENT("prices have been higher than at the previous fort!")}
{CENT("This is outrageous! They're taking advantage of us!")}
{CENT("If I had the chance to do it again,")}
{CENT("I'd buy more supplies in Independence.")}
                """
            },
            {
                "person": "Jacob Hofsteader",
                "speech": f"""
{CENT("Every night, even though I ache from the day's toils,")}
{CENT("my head is filled with dreams of the")}
{CENT("rich farm land of the Willamette Valley.")}
{CENT("I will build myself a fine, handsome homestead,")}
{CENT("and I'm certain I'll be rich within five years.")}
                """
            }
        ],
        "cost_oxen": 45.00,
        "cost_food": 0.45,
        "cost_clothing": 22.50,
        "cost_bullets": 4.50,
        "cost_wagon_wheels": 22.50,
        "cost_wagon_axles": 22.50,
        "cost_wagon_tongues": 22.50
    },



    {
        "id": "L15",
        "name": "Blue Mountains",
        "category": "misc",
        "weather_zone": 5,
        "next_destination_id": ["L16", "L17"],
        "next_destination_name": ["Fort Walla Walla", "The Dalles"],
        "next_destination_distance": [55, 125],
        "conversations": [
            {
                "person": "a tired overlander",
                "speech": f"""
{CENT("Since crossing the Snake at Fort Boise,")}
{CENT("it's been just mountains and desert.")}
{CENT("Dust deeper each day, six inches at times.")}
{CENT("No tracks, just clouds of dust. Many cattle choked")}
{CENT("on the dust after swimming the river, then bled and died.")}
                """
            },
            {
                "person": "Marnie Stewart",
                "speech": f"""
{CENT("We followed the edge of the desert from Fort Boise")}
{CENT("to the forbidding wall of the Blue Mountains.")}
{CENT("The hills were dreadful steep!")}
{CENT("Locking both wheels and coming down slow, we got down safe.")}
{CENT("Poor animals! No grass or water for days.")}
                """
            },
            {
                "person": "Jacob Hofsteader",
                "speech": f"""
{CENT("This valley of the Grande Ronde is the most")}
{CENT("beautiful sight I've seen in months.")}
{CENT("Water and graze in abundance! And if this valley is so fine,")}
{CENT("the Willamette must be twice as fine!")}
{CENT("We'll be sittin' pretty in our new homestead!")}
                """
            }
        ]
    },



    {
        "id": "L16",
        "name": "Fort Walla Walla",
        "category": "fort",
        "weather_zone": 6,
        "next_destination_id": "L17",
        "next_destination_name": "The Dalles",
        "next_destination_distance": 120,
        "conversations": [
            {
                "person": "a Cayuse Indian",
                "speech": f"""
{CENT("You ask about the Whitman massacre? I ask you why")}
{CENT("Doctor Whitman's medicines did not cure my people's children?")}
{CENT("Many caught the measles from the strangers.")}
{CENT("Why did the medicine poison our children,")}
{CENT("yet cure the children of white people?")}
                """
            },
            {
                "person": "a young mother",
                "speech": f"""
{CENT("I've traveled in fear of Indians since our journey began.")}
{CENT("As of yet, we've seen few.")}
{CENT("Those we met, helped us cross rivers, or sold us vegetables.")}
{CENT("Still, I fear. I've read grave markers and heard")}
{CENT("stories of killings in these mountains.")}
                """
            },
            {
                "person": "Amy Witherspoon",
                "speech": f"""
{CENT("My cousin Catherine was one of six children orphaned")}
{CENT("and left at Whitman's Mission. Lived with them for three years,")}
{CENT("until the massacre last November.")}
{CENT("She has survived snakebites, stampedes, falls, fights;")}
{CENT("not to mention a massacre.")}
                """
            }
        ],
        "cost_oxen": 50.00,
        "cost_food": 0.50,
        "cost_clothing": 25.00,
        "cost_bullets": 5.00,
        "cost_wagon_wheels": 25.00,
        "cost_wagon_axles": 25.00,
        "cost_wagon_tongues": 25.00
    },



    {
        "id": "L17",
        "name": "The Dalles",
        "category": "misc",
        "weather_zone": 6,
        "next_destination_id": "L18",
        "next_destination_name": "Willamette Valley, Oregon",
        "next_destination_distance": 100,
        "conversations": [
            {
                "person": "Amy Witherspoon",
                "speech": f"""
{CENT("My cousin Lydia engaged passage down the Columbia with Indians;")}
{CENT("a canoe with 17 people and luggage!")}
{CENT("The wind blew so heavy, they had to lay by.")}
{CENT("Near dark, high waves came up over their heads!")}
{CENT("Finally, they made it to shore safely.")}
                """
            },
            {
                "person": "a toll collector",
                "speech": f"""
{CENT("I collect the tolls for the Barlow Road;")}
{CENT("a bargain at twice the price!")}
{CENT("Until last year, the overlander had no choice;")}
{CENT("everyone floated the Columbia. Now, with Mr. Barlow's new road,")}
{CENT("you can drive your wagon right into Oregon City!")}
                """
            },
            {
                "person": "a mountain man",
                "speech": f"""
{CENT("These last hundred miles to the Willamette Valley are the roughest;")}
{CENT("either rafting down the swift and turbulent Columbia River,")}
{CENT("or driving your wagon over the steep Cascade Mountains.")}
{CENT("Hire an Indian guide if you take the river.")}
                """
            }
        ]
    },



    {
        "id": "L18",
        "name": "Willamette Valley, Oregon",
        "category": "end",
        "weather_zone": 6,
        "next_destination_id": "L01",
        "next_destination_name": "Independence, Missouri",
        "next_destination_distance": 0,
    }
]
