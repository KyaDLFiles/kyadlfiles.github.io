title: Game disc files
template: _wikipage.html

# Level folders
List of all the level folders (found in */CDEURO/LEVEL/*)  
*Name* is the name the level shows in the pause menu/save file menu 

|Folder|Level|Name|Numer of sectors|Info|
|-|-|-|-|-|
|NATIV|Nativ City|NATIV CITY|26|SECT3.bnk doesn't exist|
|LEVEL_1|The Roots|THE ROOTS|13||
|LEVEL_2|Flying Forest|FLYING FOREST|11|SECT11.bnk doesn't exist|
|LEVEL_3|Hunter's Domain|HUNTER'S DOMAIN|19|SECT9.bnk, SECT19.bnk and SECT20.bnk don't exist|
|!{+!1}LEVEL_4|"Nativ City" the first time it's entered at the start of the game|NATIV CITY|11|SECTs 2-4, 8-12 don't exist (the whole upper level and minigame areas don't exist)<br>The icons for shops, elevators and other things are not shown in the L1 map<br>The game silently loads in the real NATIV level during the cutscene where Atea tells Kya to follow the signs to the Boomy shop|
|LEVEL_5|The Quarry|THE QUARRY|14|
|!{+!1}LEVEL_6|Destroyed Nativ City|NATIV CITY|3|
|LEVEL_7|The Air Post|THE AIR POST|19|
|LEVEL_8|Forgotten Island|FORGOTTEN ISLAND|9
|!{+!1}LEVEL_9|Brazul's laboratory (Frank boss fight)|FORGOTTEN ISLAND|1|Pretends to be LEVEL_8 in the pause menu
|LEVEL_10|Wolfun City|WOLFUN CITY|7|
|!{+!1}LEVEL_11|Brazul miniboss (The Quarry)|THE QUARRY|1|Pretends to be LEVEL_5 in the pause menu<br>It being so distant from it's parent LEVEL_5 may suggest the decision to separate it was taken late in the development?
|LEVEL_12|The Fortress|THE FORTRES|3||
|!{+!1}LEVEL_13|Secret level|LEVEL TEST|5|[More info](/secrlvl)
|!{+!1}PREINTRO|Main menu|START MENU|1||
|!{+!1}CREDITS|End game credits|CREDITS|1||

# Sector files
Each level is divided in several *sectors*, each contained in a separate file named *SECTx.bnk*, where *x* is a number and corresponds to the sector ID (the sector IDs don't have to be continuous, and some levels skip some numbers, indicating scrapped sectors that were deleted).  

Some sectors contain big sections of a level, while other sectors contain smaller elements (tunnels, small portions of paths or enclosed areas, etc) that are used to connect two bigger sections: in this document, the first category is referred to as *area sectors*, while the second category is referred to as *partial sectors*; this distinction is made to aid in discussing the different sectors, but so far **there's no evidence of such a distinction actually existing in the game code or in the sector files**.  

The sectors of a level can be configured, through an external file located at */CDEURO/LEVEL/INFO/<level name\>.BIN* (file structure yet to be completely reversed and documented), to load in additional sectors at the same time; this is almost exclusively done to have area sectors load in partial sectors that lead to another area sector (which is also configured to keep the same partial sector loaded) (for example, in the Quarry, the whole section where the first shell elevator is is an area sector, the section with the convoy chase is another sector, and the enclosed path connecting the two is a partial sector, which both area sectors call for to also load in).  

Some levels also contain elements or sections that never ever unload (even when forcing the game to load an empty or non-existing sector): most of these consist of interactive elements (boxes, Wolfuns, doors, buttons, pressure plates, mana orbs, etc), but some are part of the level geometry or sections connecting two area sectors; the latter are listed for each level, while **always loaded interactive elements are not listed**.  

Pictures for all sectors are available [here](./sector_pictures). 


## NATIV (Nativ City)
**Total sectors**: 26  
**Area sectors**: 11  
**Partial sectors**: 15  
**Skipped numbers**: 3  
**Always loaded sections**: Slide going from upper to lower level, tree going from lower to upper section, minigame starting areas

Not all partial sectors are loaded at the same time in sector 1 and 2, since obviously a shop can't be under construction and open at the same time.  
Items can't be bought by loading partial shop sectors, as shops can only be interacted with (and items and the Nativ are only loaded in) in sectors 1 and 2.

|Number|Type|Description|Loaded partial sectors|Shell elevators|
|-|-|-|-|-|
|1|!{!1}Area|Lower level|4, 5, 6, 7, 13, 14, 15, 16, 17, 18|!{^26}N/A|
|2|!{!1}Area|Upper level|8, 9, 10, 20, 22||
|4|!{!2}Partial|Open shop with binoculars, magic board, yellow bracelet|!{^7}N/A||
|5|!{!2}Partial|Under construction shop from sector 4|||
|6|!{!2}Partial|Open shop with golden Boomy, silver bracelet|||
|7|!{!2}Partial|Under construction shop from sector 6|||
|8|!{!2}Partial|Open shop with extra health bar, Jamgut birdcall, blue bracelet|||
|9|!{!2}Partial|Under construction shop from sector 8|||
|10|!{!2}Partial|Open shop with basic Boomy, trap bombs|||
|11|!{!1}Area|Right choice minigame|-||
|12|!{!1}Area|Freefall 2 minigame<br>Has a completely black backdrop|-||
|13|!{!2}Partial|Open shop with climbing gloves, electric bombs, green bracelet|!{^6}N/A||
|14|!{!2}Partial|Under construction shop from sector 13|||
|15|!{!2}Partial|Open shop with extra energy bar, gold bracelet|||
|16|!{!2}Partial|Under construction shop from sector 15|||
|17|!{!2}Partial|Under construction shop from sector 18|||
|18|!{!2}Partial|Open shop with silver Boomy, magic bouncers, brown bracelet|||
|19|!{!1}Area|Freefall 1 minigame<br>Has a completely black backdrop|-||
|20|!{!2}Partial|Open shop with speed board, black bracelet|N/A||
|21|!{!1}Area|Dinner's ready minigame|-||
|22|!{!2}Partial|Under construction shop from sector 20|N/A||
|23|!{!1}Area|Klaustrophobia minigame<br>Has a nodraw backdrop|-||
|24|!{!1}Area|Speed racing 1 minigame|-||
|25|!{!1}Area|Freefall 3 minigame|-||
|26|!{!1}Area|Speed racing 3 minigame|-||
|27|!{!1}Area|Speed racing 4 minigame|-||

## LEVEL_1 (The Roots)
**Total sectors**: 13  
**Area sectors**:  6 
**Partial sectors**: 7  
**Unused sectors**: 1  
**Always loaded sections**: some obstacles in the square "tunnel" in the freefall section (may be objects instead of level geometry)

The default backdrop (which is used if a partial sector is forcibly loaded, or if an invalid value is specified) is one that's not found in any area sector, and is possibly an older version leftover from earlier builds.  
It's similar to the ones used in area 2 and 4, but not the same.  
It also has issues with positioning, as moving vertically causes the geometry to move in the opposite direction, and horizontal movement also causes it to move around erratically.

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area, up until before the slide|7|1||
|2|!{!1}Area|Wolfun camp with map, from after the slide up until before the tunnel|8, 10|2||
|3|!{!1}Area|Wind tunnel and area with elevator to Nativ City|11|4||
|4|!{!1}Area|Slide (excluding very beginning and very ends)|7, 8, 9|-||
|5|!{!1}Area|First part of freefall section, including island with rune, up until before enclosed square "tunnel"|9, 10, 13|3||
|!{+!4}6|!{!2}Partial|Unused, leftover from prototype builds<br>The tunnel that was seen in the May 12 prototype in the starting area (unknown purpose)|!{!0^6}N/A|!{!0^6}N/A||
|7|!{!2}Parital|Very beginning of the slide, connecting sectors 1 and 4<br>Some geometry changes based on distance, possibly hinting at earlier geometry that wasn't properly updated for low LOD||||
|8|!{!2}Partial|Very end of the slide going to the Wolfun camp, connecting sectors 4 and 2||||
|9|!{!2}Partial|Very end of the slide going to the rune island, connecting sectors 4 and 5 ||||
|10|!{!2}Partial|Tunnel connecting sectors 2 and 5||||
|11|!{!2}Parital|Very end of freefall section, connecting sector 5 and 3|||||
|12|!{!1}Area|Square "tunnel" from the freefall section<br>Uses a backdrop based on the default one (with the same positioning issues), but rotated (the section the player is in during normal gameplay is outside the backdrop sphere, so it appears as a solid color)|11, 13|-||
|13|!{!2}Partial|Initial part of the square "tunnel" in the freefall section|N/A|N/A||


## LEVEL_2 (Flying Forest)
**Total sectors**: 11  
**Area sectors**: 6  
**Partial sectors**: 4  
**Skipped numbers**: 11  
**Always loaded sections**: Enclosed path going to the Air Post elevator (connecting sectors 3 and 12)

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area, up until and including the very beginning slide|6|1||
|2|!{!1}Area|Second shell elevator area, up until after the wind tunnel (including the lever and first small wind cannon)|6, 7|2||
|3|!{!1}Area|Wolfun camp and surrounding area, and other floating island before the camp|7, 8, 10|3||
|4|!{!1}Area|First part of the slide with the bird (excluding the very beginning), up until the enclosed tunnel|8, 9|-||
|5|!{!1}Area|Second part of the slide with the bird and fourth shell elevator area|9|4||
|6|!{!2}Partial|Slide connecting sectors 1 and 2<br>The beginning of the slide is part of sector 1|!{^5}N/A|!{^5}N/A||
|7|!{!2}Partial|Section after the sector 2 wind tunnel, connecting sectors 2 and 3, containing the small area with the Wolfun to be launched in the air|||
|8|!{!2}Partial|Area the bird and beginning of the slide, connecting sectors 3 and 4|||
|9|!{!2}Partial|Tunnel connecting sectors 4 and 5|||
|10|!{!2}Partial|Worm miniboss area<br>The lava, rune and boss fight trigger are part of sector 2|||
|12|!{!1}Area|Elevator to the Air Post|-|-|

## LEVEL_3 (Hunter's Domain)
**Total sectors**: 19  
**Area sectors**: 10  
**Partial sectors**: 9  
**Unused sectors**: 1  
**Skipped numbers**: 11, 19, 20  
**Always loaded sections**: None

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area, up until before the big tunnel|14|1||
|2|!{!1}Area|Wind tower|15|3||
|3|!{!1}Area|Wolfun camp with safes and room to the slide|12, 18|5||
|4|!{!1}Area|Big "room" where Atea is found caged and subsequent wind tunnel going to the Hunter, up until before the very end|13, 22|-|
|5|!{!1}Area|Section where the fourth shell elevator and the rare monsters are (and the path to bypass that part), starting from the shell elevator platform up until before the big tunnel|15, 16|4|
|6|!{!1}Area|Path going from the rare monsters area to the Wolfun camp with safes, from after the tunnel up until the mini camp with the three gates|16, 18|-|
|7|!{!1}Area|Section with second shell elevator, Wolfuns guarding Jamgut, Wolfuns with lasers, Woof, up until before the path that splits going to the fourth shell elevator or the wind tower<br> The low LOD of sector 1 is misaligned|14, 15|2|
|8|!{!1}Area|First section of the slide going to the Hunter, from after the very beginning of the slide up until before the section with the Amortos|11, 12|-|
|10|!{!1}Area|Second section of the slide going to the Hunter, from after the area with the Amortos and moving obstacles up until before the area where Atea is found caged|11, 13|-|
|11|!{!2}Partial|Section with Amortos and moving obstacles connecting sectors 8 and 10 (level geometry only, Amortos and moving obstacles are part of sector 10)|!{^8}N/A|!{^8}N/A|||
|12|!{!2}Partial|Very beginning of the slide going to the Hunter, connecting sectors 3 and 8|||
|13|!{!2}Partial|Very end of slide connecting sectors 10 and 4|||
|14|!{!2}Partial|Tunnel connecting sectors 1 and 7|||
|15|!{!2}Partial|Path and tunnel connecting sector 7 to sector 5 or 2|||
|16|!{!2}Partial|Tunnel connecting sectors 5 and 6|||
|!{+!4}17|!{!2}Partial|Unused, leftover from prototype builds<br>Tunnel connecting the top of the wind tower to the scrapped section of the Wolfun camp with safes seen in the May 12 prototype (only the low LOD of this last part is still present in sector 3)|||
|18|!{!2}Partial|Enclosed path connecting sectors 6 and 3|||
|21|!{!1}Area|The Hunter boss fight|22|6|
|22|!{!2}Partial|Very final section of wind tunnel connecting sectors 4 and 21|N/A|N/A|

## LEVEL_4 ("Nativ City" the first time it's entered)
**Total sectors**: 11  
**Area sectors**: 1  
**Partial sectors**: 10  
**Skipped numbers**: 2, 3, 8-12  
**Always loaded sections**: Slide going from upper to lower level (broken), tree going from lower to upper section (broken)

Based on NATIV, but possibly on a slighly earlier version (it's very similar to it but not identical, and the sector files have a last edit timestamp of 17 days earlier on the game disc).  
The whole upper level and all shops on it were removed, as were all minigames (along with the starting areas).   
Many interactive elements are also broken (slides, Amata's shop, shell elevators).  
Shop sectors work like in NATIV, but with different items and prices (usually lower or just 1 Nootie), which can be exploited during speedruns using the save warp glitch.

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Lower level|4, 5, 6, 7, 13, 14, 15, 16, 17, 18|!{^11}N/A||
|4|!{!2}Partial|Open shop with binoculars, magic board, magic bouncers (rendered as yellow bracelet), regeneration|!{^10}N/A|||
|5|!{!2}Partial|Under construction shop from sector 4||||
|6|!{!2}Partial|Open empty shop||||
|7|!{!2}Partial|Under construction shop from sector 6||||
|13|!{!2}Partial|Open shop with silver Boomy, golden Boomy, speed board||||
|14|!{!2}Partial|Under construction shop from sector 13||||
|15|!{!2}Partial|Open empty shop||||
|16|!{!2}Partial|Under construction shop from sector 15||||
|17|!{!2}Partial|Under construction shop from sector 18||||
|18|!{!2}Partial|Open shop with climbing gloves, electric bomb, magic bouncers (rendered as green bracelet)||||

## LEVEL_5 (The Quarry)
**Total sectors**: 14  
**Area sectors**: 7  
**Partial sectors**: 7  
**Unused sectors**: 2   
**Always loaded sections**: None

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area, including the map and rare monster path, up until before the path going to the convoy|7, 12|1||
|2|!{!1}Area|Convoy section|7, 8|-||
|3|!{!1}Area|Outise area where the second shell elevator is, up until before the slide or cave|8, 9, 11|2||
|4|!{!1}Area|First part of cave going to Brazul's laboratory, up until the freefall section<br>Has a nodraw backdrop|9, 14|-|
|5|!{!1}Area|Slide going to the rune (except very beginning) and room with rune|11|3||
|!{+!4}6|!{!1}Area|Unused, leftover from prototype builds<br>Brazul's laboratory, which was eventually separated in it's own level (LEVEL_11) for unknown reasons<br>After the separation, this sector was left in an unfinished state, as evident the missing elements (including the shell elevator), some misplaced elements, the nodraw backdrop being visible from inside, and the fact that it doesn't call for sector 10 to be loaded|!{!0^7}N/A|!{!0^7}N/A|
|7|!{!2}Partial|Enclosed path connecting sectors 1 and 2|||
|8|!{!2}Partial|Tunnel connecting sectors 2 and 3 (where the convoy stops)|||
|9|!{!2}Partial|Very beginning of the cave connecting sectors 3 and 4|||
|!{+!4}10|!{!2}Partial|Unused, lefover from prototype builds<br>Earlier version of tunnel supposed to connect sectors 13 and 6, but in the final game the tunnel is part of sector 13 (and LEVEL_11) and looks very different||||
|11|!{!2}Partial|Very beginning of slide connecting sectors 3 and 5|||
|12|!{!2}Partial|Elevator shaft at the start of the level<br>Notably not used to connect two different sectors|||
|13|!{!1}Area|Second part of cave going to Brazul's laboratory, freefall section (except the very beginning)<br>Has a nodraw backdrop|14|-||
|14|!{!2}Partial|Very beginning of freefall section connecting sectors 4 and 13<br>Has a nodraw backdrop|N/A|N/A|

## LEVEL_6 (Destroyed Nativ City)
**Total sectors**: 3  
**Area sectors**: 2  
**Partial sectors**: 1
**Always loaded sections**: None

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area (lower level of the city)<br>Only the lower level of the city exist, with unreachable/unseeable sections removed (mostly elevated areas)|2|!{^3}N/A|
|2|!{!2}Partial|Tunnel connecting sector 1 and 3|N/A||
|3|!{!1}Area|Path where you chase the airship|2||

## LEVEL_7 (The Air Post)
**Total sectors**: 19  
**Area sectors**: 8  
**Partial sectors**: 8  
**Unknown sectors**: 3  
**Unused sectors**: 3  
**Always loaded sections**: None

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting area, including the fan room and elevator after it|10, 11|1||
|2|!{!1}Area|Second shell elevator area, including the path to the rune and the train to the extra energy bar section|12, 14|2||
|3|!{!1}Area|Section after the train in sector 5 with the fourth shell elevator, up until and including the structure with the Woofs and the snipers|13, 15|4||
|4|!{!1}Area|Outisde section after sector 5, including the cannon to the Forgotten Island|15|-||
|5|!{!1}Area|Third shell elevator area, up until and including the train<br>Many "rooms" have an extremely short draw distance, becoming invisible almost as soon as going outside of them, making it extremely difficult to take good snapshots|11, 13|3||
|6|!{!1}Area|Extra energy bar section|12|-||
|!{+!4}7|!{!3}?|Unused, leftover from prototype builds<br>Original purpose unknown, all that remains in the final build is a single rectangular-ish model with a reflection effect|!{!0}N/A|!{!0}N/A|
|8|!{!1}Area|Wind tunnel going from the starting area to the second shell elevator section|10, 14|-|
|!{+!4}9|!{!1}Area|Unused, leftover from prototype builds<br>Path that originally connected the rune island and the "main" island with the shell elevator<br>The edges of the path have broken textures, probably due to the sector no longer being maintained after it was scrapped<br>Notably, in the May 12 prototype, sector 2 unloads completely when this path is taken, and like in the final build there's no low LOD of the surrounding islands and no decorative elements, suggesting it was scrapped soon after that build as low LOD and decorations would've likely been added otherwise (the very primitive and flat geometry, which seems to not have changed since the prototype, also hints to it being scrapped soon after)|!{!0^11}N/A|!{!0^11}N/A|
|10|!{!2}Partial|Area where you land after taking the air cannon to go to sector 2<br>The amortos and air cannon are part of sector 1||||
|11|!{!2}Partial|Room with Wolfuns and elevator connecting sectors 1 and 5|||
|12|!{!2}Partial|Section connecting sectors 2 and 6|||
|13|!{!2}Partial|Elevator connecting sectors 3 and 5|||
|14|!{!2}Partial|Last section of the wind tunnel connecting sectors 8 and 2|||
|15|!{!2}Partial|Section connecting sectors 3 and 4
|!{+!4}16|!{!2}Partial|Unused<br>Most of the central rock formation of the level, but with somewhat unpolished lighting<br>In the May 12 prototype it's used by some, but not all, area sectors as part of decorative geometry, but this approach was eventually scrapped in favour of every area sector having it's own simplified decorative geometry (with parts that aren't visible completely removed), leaving this sector abandoned|||
|!{+!4}17|!{!2}Partial|Unused, leftover from prototype builds<br>Sections of the path connecting sectors 2 and 9|||
|!{+!4}18|!{!3}?|Unused, leftover from prototype builds<br>Original purpose unknown, all that remains in the final build is a single rectangular-ish model with plain black color|||
|!{+!4}19|!{!3}?|Unused, leftover from prototype builds<br>Original purpose unknown, consists of a path (or just part of a path) with solid geometry (albeit missing some textures) but it's unknown what it was supposed to connect to or be part of|||

### Known info about sectors 7, 18 and 19
These three sectors appear in a very similar, if not identical, form in the May 12 prototype, suggesting they were scrapped even before that build; it's possible, although unlikely, that sectors 7 and 18 never contained much of anything.

## LEVEL_8 (Forgotten Island)
**Total sectors**: 9  
**Area sectors**: 4  
**Partial sectors**: 2  
**Unknown sectors**: 2  
**Unused sectors**: 3  
**Always loaded sections**: Some of the lava on the initial slide, and a random nonsolid mesh


|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting section, up until and before the tunnel on the slide and the curve before it|6|1||
|2|!{!1}Area|Tunnel section of the slide (excluding very beginning) and freefall section, up until the outside area|6, 7|-|
|3|!{!1}Area|Whole outside area of the level (excluding the area where the second shell elevator is)<br>Some sections have a relatively short draw distance, while most of the level has no draw distance|7, 8, 9|2, 3, 4||
|!{+!4}4|!{!3}?|Unused and completely empty <br>The texture and model files archived inside (*SECT4.g2d* and *SECT4.g3d*) don't contain anything apart from the standard data structures present for those file types (but with no actual data being present in any segment), and no collision file (*.col*) is present at all<br>The files inside are identical to those found in sector 9 (apart from the filenames that change accordingly                                                                                  <br>Even if the sector is competely empty, it's configured to also load sector 8)|4|!{^6}N/A||
|!{+!4}5|!{!1}Area|Unused, leftover from prototype builds<br>Brazul's laboratory with Frank boss fight, which was eventually separated in it's own level (LEVEL_9) for unknown reasons<br>After the separation, this sector was likely left in an unfinished state and was no longer mantained, as evident by all textures being severely broken and that change as you move around the area|!{^5}N/A||
|6|!{!2}Partial|Section of the slide connecting sectors 1 and 2|||
|7|!{!2}Partial|Last section of freefall and initial part with shell elevator of the outside section (shell elevator is part of sector 3), connecting sectors 2 and 3|||
|8|!{!2}Partial|Air cannon going to outside of Brazul's laboratory, and the area where you land before it<br>Notably not used to connect two different sectors, as it's used to travel between two different sections of sector 3|||
|!{+!4}9|!{!3}?|Unused and completely empty <br>The texture and model files archived inside (*SECT9.g2d* and *SECT9.g3d*) don't contain anything apart from the standard data structures present for those file types (but with no actual data being present in any segment), and no collision file (*.col*) is present at all<br>The files inside are identical to those found in sector 4 (apart from the filenames that change accordingly)

### Known info and speculation about sectors 4 and 9
This part mixes objective facts and subjective speculation, **speculations are not confirmed and should not be taken as facts**.

Sector 4 used to contain the scrapped section that can be seen in the May 12 prototype, while sector 9 was probably a partial sector connecting sector 4 to another zone.

The original purpose of sector 4 can be confirmed by the September 29 prototype: in that build, sector 4 has already been stripped of all models and textures, but still contains collision data, and the location of it perfectly matches with the scrapped section; sector 9 also still contains collision data, but since the coordinates of it are unknown (and there are currently no tools to parse or visualize collision data) it's still unknown what it actually contains.

The theory of sector 9 containing a connection between sector 4 and somewhere else is supported by the fact that sector 3 calls for sector 9 to be loaded; this may seem unusual as sector 4 does not call for sector 9 to be loaded, but that could be explained in several ways: 
- the reference was never there in the first place due to a mistake
- the reference might've been removed at one point (although it would be strange to have only one reference removed and keep all others)
- there might've been even more sectors after 9 that were completely deleted (but it too would be strange to delete some sectors and keep others)
- sector 9 connected to sector 4 with some sort of one-way path/passage, which means there wouldn't have been a need to keep sector 9 loaded as it was impossible to go back to it or even see it once inside (this is supported by the fact that in the May 12 beta, the entrance to the scrapped section is one-way, and the whole section needs to be traversed to get out of it).  

(the "strange" possibilities are more likely than one may think, as I have a strong impression supported by multiple fators that the game was rushed at the end of it's development for one reason or another, thus making "mistakes" and "slapdash" decisions more likely; the fact that these two sectors were emptied and not deleted entirely, and that they still contained collision data mere weeks before the final build of the game was compiled, also suggests that the decision to so was taken late in development).  

It is noteworthy that, in the May 12 prototype, the scrapped section is in the same sector as the outside area; however the level overall contains less sectors compared to the final release, point to the fact that some sections, including the scrapped one, were eventually moved to their own separate sectors (the whole level in the May 12 prototype appears to be one of the levels in the earliest phases of development, with plenty of missing or nonfunctional elements, earlier layouts, no Wolfuns in the whole level apart from Wolfun Frank, so it's possible that the split happened as the level continued to grow larger and more resource intensive) (in fact, the scrapped section in particular appears to be in an extremely early phase of development even compared to the rest of the level, with very primitive and placeholder geometry, no interactive elements at all apart from an Amortos and air cannon, which are the strictly required elements to enter and leave the section, and there are a bunch of weird elements consisting of a W with a circle around it, which I speculate were used as placeholders for Wolfuns).

## LEVEL_9 (Forgotten Island Wolfun Frank boss fight)
**Total sectors**: 1  
**Area sectors**: 1  
**Always loaded sections**: Vertical tunnel entering the level

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|The whole level is contained in a single sector|-|5 (Forgotten Island)|

## LEVEL_10 (Wolfun City)
**Total sectors**: 7  
**Area sectors**: 4  
**Partial sectors**: 3  
**Always loaded sections**: Elevator shaft connecting the assembly line and stealth section, and the other side including the bridge and surrounding level geometry

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Outside section|6|1, 3|
|2|!{!1}Area|Part of the inside section, up until the stealth section with snipers and alarm bell|4|-|
|3|!{!1}Area|Part of the inside section, from the assembly line up until the path going to the section with the second shell elevator|4, 7|-|
|4|!{!2}Partial|Section connecting setors 2 and 3 (in tandem with the always loaded section)<br>Contains the two rooms with the pressure plate and the lever|N/A|N/A|
|5|!{!1}Area|Second shell elevator area|6, 7|2|
|6|!{!2}Partial|Room connecting sectors 1 and 5<br> The interactive elements inside the room (and bomb dispenser outside) are always loaded and not part of the sector|!{^2}N/A|!{^2}N/A|
|7|!{!2}Partial|Room connecting sectors 3 and 5<br>The interactive elements inside the room are always loaded and not part of the sector|||

## LEVEL_11 (The Quarry Brazul miniboss)
**Total sectors**: 1  
**Area sectors**: 1  
**Always loaded sections**: None

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|The whole level is contained in a single sector|-|4 (The Quarry)|

## LEVEL_12 (The Fortress)
**Total sectors**: 3  
**Area sectors**: 2  
**Partial sectors**: 1  
**Always loaded sections**: Slide and room with crushing walls, connecting sectors 1 and 2

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Outside section|3|1|
|2|!{!1}Area|Inside the fortress|3|-|
|!{+!4}3|!{!3}?|Unused, completely empty and unknown purpose<br>The texture and model files archived inside (*SECT3.g2d* and *SECT3.g3d*) don't contain anything apart from the standard data structures present for those file types (but with no actual data being present in any segment), and no collision file (*.col*) is present at all|N/A|N/A|

### Known info about sector 3
Unlike LEVEL_8, by the time the September 29 prototype was compiled, sector 3 had already been stripped of all models, textures and collision data.  

In the May 12 prototype, the level consists of three sectors, with the inside of the fortress being contained in sector 3, while sector 2 contained a slide connecting sectors 1 and 3 (with the slide being very different compared to the final one, and strikingly similar to the one in LEVEL_13); notably in this prototype the level (mostly sector 1) also contains a lot of extra elements seemingly scattered around the level or misaligned with the rest of the level (both interactive elements, many of which appear to have had the surrounding level geometry removed, and level geometry making up small "rooms").

Ultimately, given the information we currently have access to, and not having access to any builds in between 12 May 2003 and 29 September 2003, no assertion about the original purpose of the now empty sector can be made.

## LEVEL_13 (Level Test)
**Total sectors**: 5  
**Area sectors**: 5  
**Always loaded sections**: Tube at the end of the maze, and "shafts" of elevators going to the slide and maze

|Number|Type|Description|Loaded partial sectors|Shell elevator|
|-|-|-|-|-|
|1|!{!1}Area|Starting room|-|!{^5}N/A|
|2|!{!1}Area|Soccer|-||
|3|!{!1}Area|PVP arena ("fight")|-||
|4|!{!1}Area|Maze|-||
|5|!{!1}Area|Slide ("tobo")|-||

