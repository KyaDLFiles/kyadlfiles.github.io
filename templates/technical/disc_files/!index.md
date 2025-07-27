title: Game disc files
template: _wikipage.html

# Level folders
List of all the level folders (found in /CDEURO/LEVEL/)  
*Name* is the name the level shows in the pause menu/save file menu 

|Folder|Level|Name|No. of SECTx.bin files|Info|
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
|!{+!1}LEVEL_9|Brazul's laboratory (Frank boss fight)|FORGOTTEN ISLAND|1|Pretends to be LEVEL_8 in the areas preview section of the pause menu
|LEVEL_10|Wolfun City|WOLFUN CITY|7|
|!{+!1}LEVEL_11|Brazul miniboss (The Quarry)|THE QUARRY|1|Pretends to be LEVEL_5 in the areas preview section of the pause menu<br>It being so distant from it's parent LEVEL_5 may suggest the decision to separate it was taken late in the development?
|LEVEL_12|The Fortress|THE FORTRES|3||
|!{+!2}LEVEL_13|Secret level|LEVEL TEST|5|[More info](/secrlvl)
|!{+!1}PREINTRO|Main menu|START MENU|1||
|!{+!1}CREDITS|End game credits|CREDITS|1||

# Sector files
TBA

## NATIV (Nativ City)
**Total sectors**: 26  
**Area sectors**: 11  
**Partial sectors**: 15  
**Skipped numbers**: 3  
**Always loaded elements**: Slide going from upper to lower level, tree going from lower to upper section, minigame starting areas

Not all partial sectors are loaded at the same time in sector 1 and 2, since obviously a shop can't be under construction and open at the same time. Open shop sectors unfortunately don't allow access to the items, as shops can only be interacted with (and items are only loaded in) sectors 1 and 2.

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Lower level|4, 5, 6, 7, 13, 14, 15, 16, 17, 18|!{^26}N/A||
|2|Area|Upper level|8, 9, 10, 20|||
|4|Partial|Open shop with binoculars, magic board, yellow bracelet|!{^7}N/A|||
|5|Partial|Under construction shop from sector 4||||
|6|Partial|Open shop with golden Boomy, silver bracelet||||
|7|Partial|Under construction shop from sector 6||||
|8|Partial|Open shop with extra health bar, Jamgut birdcall, blue bracelet||||
|9|Partial|Under construction shop from sector 8||||
|10|Partial|Open shop with basic Boomy, trap bombs||||
|11|Area|Right choice minigame|-|||
|12|Area|Freefall 2 minigame<br>Has a completely black backdrop|-|||
|13|Partial|Open shop with climbing gloves, electric bombs, green bracelet|!{^6}N/A|||
|14|Partial|Under construction shop from sector 13||||
|15|Partial|Open shop with extra energy bar, gold bracelet||||
|16|Partial|Under construction shop from sector 15||||
|17|Partial|Under construction shop from sector 18||||
|18|Partial|Open shop with silver Boomy, magic bouncers, brown bracelet||||
|19|Area|Freefall 1 minigame<br>Has a completely black backdrop|-|||
|20|Partial|Open shop with speed board, black bracelet|N/A|||
|21|Area|Dinner's ready minigame|-|||
|22|Partial|Under construction shop from sector 20|N/A|||
|23|Area|Klaustrophobia minigame<br>Has nodraw backdrop|-|||
|24|Area|Speed racing 1 minigame|-|||
|25|Area|Freefall 3 minigame|-|||
|26|Area|Speed racing 3 minigame|-|||
|27|Area|Speed racing 4 minigame|-|||

## LEVEL_1 (The Roots)
**Total sectors**: 13  
**Area sectors**:  6 
**Partial sectors**: 7  
**Unused**: 1  
**Always loaded elements**: some obstacles in the square "tunnel" (may be objects instead of level geometry)

The default backdrop (which is used if a partial sector is forcibly loaded, or if an invalid value is specified) is one that's not found in any area sector, and is possibly an older version leftover from earlier builds.  
It is notably similar to the ones used in area 2 and 4, but not the same.  
It also has issues with positioning, as moving vertically causes the geometry to move in the opposite direction, and horizontal movement also causes it to move around erratically.

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area up until the slide|7|1||
|2|Area|Wolfun camp with map, from the end of the slide up until the tunnel|8, 10|2||
|3|Area|Wind tunnel and elevator to Nativ City (final area)|11|4||
|4|Area|Slide|7, 8, 9|-||
|5|Area|Freefall section and island with rune, up until the wind tunnel|10, 13|3||
|6|Partial|Unused, leftover from prototype builds<br>The tunnel that was seen in the May 12 prototype in the starting area (position coincides with it)|!{^6}N/A|!{^6}N/A||
|7|Parital|Initial part of the slide, connecting sectors 1 and 4<br>Some geometry changes based on distance, possibly hinting to earlier geometry that wasn't properly updated for low LOD||||
|8|Partial|Final part of the slide going to the Wolfun camp, connecting sectors 4 and 2||||
|9|Partial|Final part of the slide going to the rune island, connecting sectors 4 and 5 ||||
|10|Partial|Tunnel connecting sectors 2 and 5||||
|11|Parital|Very end of freefall section, connecting sector 5 and 3|||||
|12|Area|Middle part of the square "tunnel" in the freefall section<br>Notably uses the default backdrop, with the same issues with positioning, but is also rotated compared to partial sectors|11, 13|-||
|13|Partial|Initial part of the square "tunnel" in the freefall section|N/A|N/A||

## LEVEL_2 (Flying Forest)
**Total sectors**: 11  
**Area sectors**: 6  
**Partial sectors**: 4  
**Skipped numbers**: 11  
**Always loaded elements**: Tunnel going to the Air Post elevator (connecting sectors 3 and 12)

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area, up until the slide|6|1||
|2|Area|Second shell elevator area, up until after the wind tunnel|6, 7|2||
|3|Area|Wolfun camp, worm miniboss, starting area of the slide with the bird, and area before the camp|7|3, 8, 10||
|4|Area|First part of the slide with the bird, up until the closed tunnel|8, 9|-||
|5|Area|Second part of the slide with the bird and ending area|9|4||
|6|Partial|Slide connecting sectors 1 and 2<br>The beginning of the slide is part of sector 1|!{^5}N/A|!{^5}N/A||
|7|Partial|Section after the sector 2 wind tunnel, connecting sectors 2 and 3, containing the Wolfun to be launched in the air|||
|8|Partial|Slide with bird starting area and very small section of the slide, connecting sectors 3 and 4|||
|9|Partial|Tunnel connecting sectors 4 and 5|||
|10|Partial|Worm miniboss area<br>The lava, rune and boss fight trigger are part of sector 2|||
|12|Area|Elevator to the Air Post|-|-|

## LEVEL_3 (Hunter's Domain)
**Total sectors**: 19  
**Area sectors**: 10  
**Partial sectors**: 9  
**Skipped numbers**: 11, 19, 20  
**Always loaded elements**: None?

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area, up until the tunnel|14|1||
|2|Area|Wind tower|15|3||
|3|Area|Wolfun camp with safes|12, 18|5||
|4|Area|Area where Atea is found caged and subsequent wind tunnel going to the Hunter, up until before the area with him|13, 22|-|
|5|Area|Section where the fourth shell elevator and the rare monsters are (and the path to bypass that part), starting from about the shell elevator up until the big tunnel|15, 16|4|
|6|Area|Path going from the rare monsters area to the Wolfun camp with safes, from the tunnel up until the door to the camp|16, 18|-|
|7|Area|Section with second shell elevator, Wolfuns guarding Jamgut, Wolfuns with lasers, Woof, up until tunnel going to the wind tower or path going to the rare monsters section|14, 15|2|
|8|Area|First section of the slide going to the Hunter, from the beginning of the slide up until the section with the Amortos|11, 12|-|
|10|Area|Second section of the slide going to the Hunter, from the area with the Amortos and moving obstacles up until before the area where Atea is found caged|11, 13|-|
|11|Partial|Section with Amortos and moving obstacles connecting sectors 8 and 10 (level geometry only, Amortos and moving obstacles are actually part of sector 10)|!{^8}N/A|!{^8}N/A|||
|12|Partial|Very beginning section of the slide to the Hunter, connecting sectors 3 and 8|||
|13|Partial|Section of slide connecting sectors 10 and 4|||
|14|Partial|Tunnel connecting sectors 1 and 7|||
|15|Partial|Path and tunnel connecting sector 7 to sector 5 or 2|||
|16|Partial|Tunnel connecting sectors 5 and 6|||
|17|Partial|Unused, leftover from prototype builds<br>Tunnel connecting the top of the wind tower to the scrapped (with no files of it surviving) area above the Wolfun camp with safes seen in the May 12 prototype|||
|18|Partial|Section connecting sectors 6 and 3|||
|21|Area|The Hunter boss fight|22|6|
|22|Partial|Section of tunnel connecting sectors 4 and 21|N/A|N/A|