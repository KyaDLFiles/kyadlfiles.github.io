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

Not all partial sectors are loaded at the same time in sector 1 and 2, since obviously a shop can't be under construction and open at the same time. Open shop sectors don't allow access to the items, as shops can only be interacted with (and items are only loaded in) in sectors 1 and 2.

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Lower level|4, 5, 6, 7, 13, 14, 15, 16, 17, 18|!{^26}N/A||
|2|Area|Upper level|8, 9, 10, 20, 22|||
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
**Unused sectors**: 1  
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
|5|Area|Freefall section and island with rune, up until the wind tunnel|9, 10, 13|3||
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
**Unused sectors**: 1  
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

## LEVEL_4 ("Nativ City" the first time it's entered)
**Total sectors**: 11  
**Area sectors**: 1  
**Partial sectors**: 10  
**Skipped numbers**: 2, 3, 8-12  
**Always loaded elements**: Slide going from upper to lower level, tree going from lower to upper section

Based on NATIV, but possibly a slighly earlier version of it (it's very similar to it but not identical, and the sector files have a last edit timestamp of 17 days earlier on disc)  
The whole upper level and all shops on it were removed, as were all minigames (along with the starting areas)   
Shop sectors work like in NATIV

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Lower level|4, 5, 6, 7, 13, 14, 15, 16, 17, 18|!{^26}N/A||
|4|Partial|Open shop with binoculars, magic board, magic bouncers (rendered as yellow bracelet), regeneration|!{^7}N/A|||
|5|Partial|Under construction shop from sector 4||||
|6|Partial|Open empty shop||||
|7|Partial|Under construction shop from sector 6||||
|13|Partial|Open shop with silver Boomy, golden Boomy, speed board|!{^6}N/A|||
|14|Partial|Under construction shop from sector 13||||
|15|Partial|Open empty shop||||
|16|Partial|Under construction shop from sector 15||||
|17|Partial|Under construction shop from sector 18||||
|18|Partial|Open shop with climbing gloves, electric bomb, magic bouncers (rendered as green bracelet)||||

## LEVEL_5 (The Quarry)
**Total sectors**: 14  
**Area sectors**: 7  
**Partial sectors**: 7  
**Unused sectors**: 2 
**Always loaded elements**: None?

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area, including the map and rare monster path, up until the path going to the convoy|7, 12|1||
|2|Area|Convoy|7, 8|-||
|3|Area|Outise area near second shell elevator|8, 9, 11|2||
|4|Area|First part of path going to Brazul's laboratory, up until the freefall section<br>Has a nodraw backdrop|9, 14|-|
|5|Area|Slide going to the rune, and room with rune|11|3||
|6|Area|Unused, leftover from prototype builds<br>Brazul's laboratory, which was eventually separated in it's own level (LEVEL_11) for unknown reasons<br>After the separation, this sector was probably left as-is in an unfinished state, as evident the many missing elements (including the shell elevator), some misplaced elements, missing textures on the wall leaving the nodraw backdrop visible, and the fact that it doesn't even call for sector 10 to be loaded<br>Outside backdrop geometry|!{^7}N/A|!{^7}N/A|
|7|Partial|Path connecting sectors 1 and 2|||
|8|Partial|Tunnel connecting sectors 2 and 3 (where the convoy stops)|||
|9|Partial|Initial section of tunnel connecting sectors 3 and 4|||
|10|Partial|Unused, lefover from prototype builds<br>Earlier version of tunnel supposed to connect sectors 13 and 6, but in the final game the tunnel is part of sector 13 and looks very different||||
|11|Partial|Initial section of slide connecting sectors 3 and 5|||
|12|Partial|Elevator shaft at the start of sector 1|||
|13|Area|Second part of path going to Brazul's laboratory, freefall section<br>Has a nodraw backdrop|14|-||
|14|Partial|Initial section of freefall section connecting sectors 4 and 13<br>Has a nodraw backdrop|N/A|N/A|

# LEVEL_6 (Destroyed Nativ City)
**Total sectors**: 3  
**Area sectors**: 2  
**Partial sectors**: 1

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area<br>Only the lower level of the city exist, with unreachable/unseeable parts removed|2|!{^3}N/A|
|2|Partial|Tunnel connecting sector 1 and 3|N/A||
|3|Area|Path where you chase the airship|2||

## LEVEL_7 (The Air Post)
**Total sectors**: 14  
**Area sectors**: 7  
**Partial sectors**: 7  
**Unused sectors**: 2 
**Always loaded elements**: None?

|Number|Type|Description|Loaded partial sectors|Shell elevator|Picture|
|-|-|-|-|-|-|
|1|Area|Starting area, up until after the fan room|X|1||
|2|Area|Second shell elevator area, containing the path to the rune and the train to the extra energy bar area|X|2||
|3|Area|Area after the train in sector 5, up until the room with the Woofs|X|4||
|4|Area|Area after sector 5, containing the cannon to the Forgotten Island|X|-||
|5|Area|Third shell elevator area, up until after the train<br>For some reason many "rooms" stop rendering immediately after leaving them, making it extremely difficult to take snapshots of them|X|3||
|6|Area|Extra enery bar area|X|-||
|7|?|Unused, leftover from prototype builds<br>Original purpose unknown, all that remains in the final build is a single flat rectangular-ish model with a reflection effect|||
|8|Area|Wind tunnel going from the starting area to the rune/extra energy bar area|X|-|
|9|Area?|Unused, leftover from prototype builds<br>Path that originally connected the rune island with the "main" island with the shell elevator<br>The edges of the path have broken textures<br>Notably sector 2 unloads completely in the May 1y prototype when this sector is loaded, and there's no low LOD of the surrounding islands and no decorative elements, suggesting it was scrapped early as low LOD and decorations would've likely been added otherwise|N/A|N/A|
|10|Partial|Area where you land after taking the air cannon to go to sector 2<br>The amortos and air cannon are part of sector 1||||
|11|Partial|Room with Wolfuns and elevator connecting sectors 1 and 5|||
|12|Partial|Section connecting sectors 2 and 6|||
|13|Partial|Shell elevator connecting sectors 5 and 3|||
|14|Partial|Last section of the wind tunnel connecting sectors 8 and 2|||
|15|Partial|Section connecting sectors 3 and 4
|16|Partial|Unused<br>The central rock formation of the level, but with somewhat unpolished lighting<br>It notably contains the whole model of the formation all around, which no other sector does (as polygons not visible from the respective areas are removed in each sector), suggesting it might've been used as a reference for those|||
|17|Partial|Unused, leftover from prototype builds<br>Sections of the path connecting sectors 2 and 9|||
|18|?|Unused, leftover from prototype builds<br>Original purpose unknown, all that remains in the final build is a single flat rectangular-ish model with plain black color||test 6|
|19|?|Unused, leftover from prototype builds<br>Original purpose unknown, consists of a path with solid geometry (albeit missing some textures) but it's unknown what it was supposed to connect to or be part of|||