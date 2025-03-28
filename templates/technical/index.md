title: Technical information

# Preface
## Cheat Engine, cheat tables and PCSX2
Me and other members who are investigating the inner workings of Kya DL use [Cheat Engine](https://www.cheatengine.org/) to find variables and save the findings in a cheat table file, because it's a very powerful and flexible program.

I'll be uploading my cheat tables (which also include contributions from other members of the server) in [a separate repository](https://github.com/KyaDLFiles/Kya_DL_cheat_tables), which includes instructions on how to use CE with PCSX2 >1.6

## Wording regarding pointers, addresses and offsets
All addresses and offsets are always hexadecimal.

When talking about a pointer address, this page uses a terminology similar to CE: to get to the desired address, take the 4-byte number **stored** at the *pointer base address*, add the *offset* to that number, and the result is the actual memory address storing that particular variable.  
(eg: *pointer base address* `10` & *offset* `+2` = take value stored at `10` (X), add `+2` to it, actual address is `X+2`)

When talking about a "normal" address that doesn't use pointers (for example, the controller readings), you simply take the *starting address* and add the *offset* to it to get the actual address.  
(eg: beginning address `20` & offset `6` = actual address `26`)

# Variables and RAM
*!**Important!** The addresses refer to the final NTSC build of the game.  
The PAL version has different values, which will eventually be documented.!*

## Controller readings (player 1)
**Starting address**: `0495B30`/`0495B9C`/`0495C1C`

The difference between these three locations needs to be investigated

### Joker commands

**Type**: 2 byte "integer"  
**Offset**: `+00`

Joker commands store the button readings from one of the controllers as 2 bytes, with each bit corresponding to a button.

In Kya DL, the codes have the following values:

|Button|7|6|5|4|3|2|1|0|7|6|5|4|3|2|1|0|Hex   |
|------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|------|
|@!!q  |!{!1}0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|`7FFF`|
|@!!x  |1|!{!1}0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|`BFFF`|
|@!!o  |1|1|!{!1}0|1|1|1|1|1|1|1|1|1|1|1|1|1|`DFFF`|
|@!!t  |1|1|1|!{!1}0|1|1|1|1|1|1|1|1|1|1|1|1|`EFFF`|
|@!!r1 |1|1|1|1|!{!1}0|1|1|1|1|1|1|1|1|1|1|1|`F7FF`|
|@!!l1 |1|1|1|1|1|!{!1}0|1|1|1|1|1|1|1|1|1|1|`FBFF`|
|@!!r2 |1|1|1|1|1|1|!{!1}0|1|1|1|1|1|1|1|1|1|`FDFF`|
|@!!l2 |1|1|1|1|1|1|1|!{!1}0|1|1|1|1|1|1|1|1|`FEFF`|
|@!!dl |1|1|1|1|1|1|1|1|!{!1}0|1|1|1|1|1|1|1|`FF7F`|
|@!!dd |1|1|1|1|1|1|1|1|1|!{!1}0|1|1|1|1|1|1|`FFBF`|
|@!!dr |1|1|1|1|1|1|1|1|1|1|!{!1}0|1|1|1|1|1|`FFDF`|
|@!!du |1|1|1|1|1|1|1|1|1|1|1|!{!1}0|1|1|1|1|`FFEF`|
|@!!st |1|1|1|1|1|1|1|1|1|1|1|1|!{!1}0|1|1|1|`FFF7`|
|@!!r3 |1|1|1|1|1|1|1|1|1|1|1|1|1|!{!1}0|1|1|`FFFB`|
|@!!l3 |1|1|1|1|1|1|1|1|1|1|1|1|1|1|!{!1}0|1|`FFFD`|
|@!!se |1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|!{!1}0|`FFFE`|


When multiple buttons are pressed, the value gets set to [Button 1] *AND* [Button 2] *AND* ... [Button N]; for example when pressing @!r2 + @!t + @!o the value gets set to `FDFF` *AND* `EFFF` *AND* `DFFF` == `CDFF` (`1100 1101 1111 1111`)

Other PS1/PS2 games may store these values in a different way. [More info here](https://www.cheatcc.com/psx/codes/jokercom.html)
#### Joker command calculator
????
### Stick readings
**Type**: 1 byte unsigned integers  
**Length:** 4 \* 1 byte = 4 bytes total

|Offset|Stick|Axis|
|------|-----|----|
|`+02` |Right|X   |
|`+03` |Right|Y   |
|`+04` |Left |X   |
|`+05` |Left |Y   |


### Button pressure
For those who didn't know: [the DualShock 2 (and DS3) has pressure sensitive buttons](https://en.wikipedia.org/wiki/DualShock#DualShock_2) (except for Select, Start, L3 and R3), meaning that games can tell how hard a button is being pressed.  
Kya: DL requires a DualShock 2 and won't work with an original PS1 DualShock.  
This is usually a sign that a game requires the pressure sensitive buttons, but it's currently unknown in which way the pressure info is used in Kya DL (if at all).  
Regardless, this gives us another way of checking for buttons being pressed (apart from Select, Start, L3 and R3), which, depending on the situation, might be easier or better to use.

**Type**: 1 byte unsigned integers  
**Size**: 12 * 1 byte = 12 bytes total  
`00` equals not being pressed at all, `01` barely pressed and `FF` fully pressed

|Offset|Button|
|------|------|
|`+06` |@!dr  |
|`+07` |@!dl  |
|`+08` |@!du  |
|`+09` |@!dd  |
|`+0A` |@!t   |
|`+0B` |@!o   |
|`+0C` |@!x   |
|`+0D` |@!q   |
|`+0E` |@!l1  |
|`+0F` |@!r1  |
|`+10` |@!l2  |
|`+11` |@!r2  |
### Recap
|Offset|Length (bytes)|Content|
|------|--------------|-------|
|`+00` |`02`          |`Joker command`|
|`+02` |`01`          |`Right analog X axis`|
|`+03` |`01`          |`Right analog Y axis`|
|`+04` |`01`          |`Left analog X axis`|
|`+05` |`01`          |`Left analog Y axis`|
|`+06` |`01`          |`D-pad right pressure`|
|`+07` |`01`          |`D-pad left pressure`|
|`+08` |`01`          |`D-pad up pressure`|
|`+09` |`01`          |`D-pad down pressure`|
|`+0A` |`01`          |`Triangle pressure`|
|`+0B` |`01`          |`Circle pressure`|
|`+0C` |`01`          |`X pressure`|
|`+0D` |`01`          |`Square pressure`|
|`+0E` |`01`          |`L1 pressure`|
|`+0F` |`01`          |`R1 pressure`|
|`+10` |`01`          |`L2 pressure`|
|`+11` |`01`          |`R2 pressure`|
## Controller readings (player 2)

**Address**: `0495CB0`/`0495D1C`/`0495D9C`

The information stored and the order it's stored in is the same as player one.  
Note that the game also requires a DualShock 2 for player two: if you try plugging in an original DualShock in port 2 and try to control P2 in the secret level nothing will happen.
# Kya's position and movement
**Pointer base address**: 06F2D90
## Position
**Type**: floats
**Offset (X)**: `+30`
**Offset (Y)**: `+34`
**Offset (Z)**: `+38`

To give a sense of scale, when Kya jumps by pressing @!x she peaks at around +1.71 Y.  
(it's actually currently unknown which value the game considers to be X and which one to be Z, the notation has been chosen based on their order in memory).
## Settings read from BWITCH.ini
Some "settings" are stored in the file *BWITCH.ini* in the root of the game DVD.  
It's possible (and easier) to change these by editing the variables used for storing them after being read from the disc.
## Starting level (AddLevel)
This controls the level the game should load when starting a new game.

Removing the setting completely from the config file causes it to default to NATIV (even though a comment inside the file states that the default level is *LEVEL_T*, very likely a leftover from the development stages of the game).

The folder is set by SetPath, which is set to *CdEuro/Level/* in the final game (regardless of the region).

If set to a value different from the default value of The Roots, when starting a new game, the intro movie will be skipped, the lines *"Hey, look at this"..."Is it dead?"* will be played, and then the player will be immediately thrown in the level.

**Type**: 4 bytes *?signed?* integer (only last byte shown in table)  
**Address**: `06DA5B4`

|Value|Level folder|Level|Info|
|-----|------------|-----|----|
|`00` |NATIV       |Nativ City|
|`01` |LEVEL_1     |The Roots|Default value
|`02` |LEVEL_2     |Flying Forest|
|`03` |LEVEL_3     |Hunter's Domain|
|`04` |LEVEL_4     |Nativ City when first visiting with Aton|
|`05` |LEVEL_5     |The Quarry|
|`06` |LEVEL_6     |Destroyed Nativ City|
|`07` |LEVEL_7     |The Air Post|
|`08` |LEVEL_8     |Forgotten Island|
|`09` |LEVEL_9     |Brazul Lab (Forgotten Island)|
|`0A` |LEVEL_10    |Wolfun City|
|`0B` |LEVEL_11    |The Quarry Brazul miniboss|
|`0C` |LEVEL_12    |The Fortress|
|`0D` |LEVEL_13    |Level Test (secret level)|
|`0E` |PREINTRO|Main menu|If this is chosen, the intro movie will be played, followed by the opening lines, and then the main menu will be reloaded|
|`0F` |CREDITS|Ending credits|
|!{>4}Values after 15 make the game try to load levels that don't exist, causing unexpected behaviours<br>Usually the save file gets set to "UNKNOWN LEVEL (number of level as signed integer)"<br>Below are other more unique examples||||
|`10` |||The game returns to the save file selector, deleting the save file that was selected (resetting it to EMPTY)
|`11` |||The game immediately freezes after starting new game, without playing the intro lines and without showing any signs of trying to load anything from the disc (observed through PCSX2 logs)
|`12` |||Causes the selected save file to be set to an empty level name

!![Examples of unusual levels in the file load menu](/img/weirdlvls.jpg)

## Dormant debug features/cheats
There are dormant debug features/cheats left over from when the game was in development; a working implementation of the cheat options menu can most prominently be seen in the [September 29 prototype](https://hiddenpalace.org/Kya:_Dark_Lineage_(Sep_29,_2003_prototype)).

Strings pertaining to this menu have been found in the final build, but it's currently unknown if and how the menu can be accessed in the final build.

However, it is possible to enable the flying cheat and the invincibility cheat by manually writing to the respective values in RAM (the cheat options menu is coded weirdly, as there are two separate variables for these two cheats: the first one only controls if the cheat is displayed as enabled or disabled in the menu, and the second one (the "enable" variables) is what the code actually checks to see if the cheat effect should apply (for example, the game checks the enable variable for the flying cheat when @!r2+@!r3 is pressed), and the first variable gets copied to the enable variable any moment the cheat options menu is being viewed).

With the aid of the PCSX2 debugger and the September 29 prototype, the code that handles checking the enable variables was found in the final game, and it was confirmed that they work in the final build too.  
(Keep in mind that the locations in RAM vary from build to build and version to version, so the values in this page won't work for the September 29 prototype).

These are stored next to each other and are accessed via a pointer.

## Flying and invincibility

**Pointer base address**: `0448AA0`  
**Offset (flying)**: `+AA0`  
**Offset (invincibility)**: `+AA4`  

Once the flying cheat is enabled, it can be toggled by pressing @!r2+@!r3

## Other

Another dormant debug menu is documented at [tcrf](https://tcrf.net/Kya:_Dark_Lineage#Debug_Menu) 

# Game disc files
## Level folders
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
|!{+!2}LEVEL_13|Secret level|LEVEL TEST|5|More info
|!{+!1}PREINTRO|Main menu|START MENU|1||
|!{+!1}CREDITS|End game credits|CREDITS|1||

# Save files

*!Important!!* Data (numerical values, checksums etc) is saved as little endian (LE).  
So for example an int32 value of 9 will be saved as 09 00 00 00 inside the file.

Note: files that are standard for all PS2 saves (icon.sys, *.ico) won't be discussed
## Save header

All KDL .dat save files start with a header containing at least two checksums.  
*?Even though the header has a size field inside it, due to the fact that the number of data sections it can contain info for is hardcoded to two in the game code, it can be considered as having a fixed size in practice.?*

|Offset|Size (bytes)|Type|Content|
|-|-|-|-|
|`+00`|`04`|String|`NEDE` ("EDEN" in reverse)|
|`+04`|`04`|Unsigned int32|Header checksum (Starting from `08`, as to exclude NEDE and the checksum itself, to the address stored in the header size)|
|`+08`|`04`|*?Unsigned?* int32|Header size (in practice always `1C`)|
|`+0C`|`04`|Unsigned int32|First data block checksum|
|`+10`|`04`|*?Unsigned?* int32|First data block size|
|`+14`|`04`|Unsigned int32|Second data block checksum<br>All zeroes if there's no second data block|
|`+18`|`04`|*?Unsigned?* int32|Second data block size|

Reverse engineered checksum code can be found here 
## Settings file (settings.dat)
In the table below, the offset starts from after the header.

|Offset|Size (bytes)|Type|Info|
|-|-|-|-|
|`+00`|`04`|String|`STGS`
|`+04`|`04`|Unknown|Unknown<br>Set to 03 by the game|
|`+08`|`04`|Signed? int32|Language setting (PAL release) (`00` - `04`)<br>In order: English, French, German, Spanish, Italian<br>The NTSC-U/C release ignores this setting|
|`+0C`|`04`|*?Signed?* int32|Audio (`00` = mono, `01` = stereo, `02` = surround)|
|`+10`|`04`|Signed? int32|Music volume (`00` - `0C`)|
|`+14`|`04`|Signed? int32|SFX volume (`00` - `0C`)|
|`+1C`|`04`|Signed int32|X axis screen adjust|
|`+20`|`04`|Signed int32|Y axis screen adjust<br>Stored in negative - in-game negative values are stored as positive values and vice versa|
|`+24`|`01`|Boolean (byte)|Enable vibration|
|`+25`|`01`|Boolean (byte)|Enable subtitles|
|`+26`|`01`|Unknown byte value|Unknown|
|`+27`|`01`|Boolean (byte)|Aspect ratio<br>`00` = 4:3, `01` = 16:9|
|`+28`|`D8`|!{>2}Unknown<br>Won't affect the game if filled with garbage, won't even get reset to a default value|
|`+110`|`1C`|!{>2}Unknown<br>Outside of the data block size set in the header, thus doesn't affect checksum<br>Won't affect the game if filled with garbage or even completely removed|
