title: Cheat codes
template: _wikipage.html

?[Link to download](https://github.com/KyaDLFiles/Kya_DL_cheats)

# Cheats list
## Final builds (both regions)
### Dormant debug features/cheats
+ **Enable flying cheat** - Enable the dormant flying cheat, toggled by pressing @@r2+@@r3
+ **Invincibility** - Enable the dormant invincibility cheat (always active)  
+ **R2+Right/Left toggle invincibility** - @@r2+@@dr to activate invinicibility, @@r2+@@dl to deactivate it
### Misc
+ **Circle+Triangle+Left teleport to the maze in LEVEL_13** - Teleport to the maze and increase the mana limit in LEVEL_13  
## Prototypes
Documentation coming soon

# How to use
## PCSX2 (≥2.x)
In the emulator, open *Settings* > *Folders*, then click *Open* next to the *Cheats folder*.  
Copy the cheat file you downloaded in that folder, then go back to the emulator, open the *Game Properties*, then the *Cheats* tab, then enable cheats and *Reload Cheats*.  
I recommend **un**ticking the *All CRCs* setting, otherwise there may be conflicts between the retail NTSC build and the various prototype builds.  
### Note about legacy PCSX2 versions
Older PCSX2 versions don't have a cheat management system.  
The cheats can still work on them, but you need to manually edit the .pnach file.   
All the lines with square brackets and the *author* lines have to be removed, and unwanted cheats have to be removed from the file (cheats have to be manually added and removed when needed) (you can use *//* to mark a line as a comment, so the emulator will ignore it).  

## Console
The console cheats are designed for ?[Cheat Device for PS2](https://github.com/israpps/CheatDevicePS2) and [OpenPS2Loader (OPL)](https://github.com/ps2homebrew/Open-PS2-Loader), which require a mod (soft or hard) to run homebrews (I haven't yet created the *.cht* files for OPL, but in the meantime you can create them manually as the cheat codes are the same).  
Instructions to configure CDfPS2 are available ?[here](https://github.com/root670/CheatDevicePS2/wiki/Cheats) (these instructions are from the original, now unmantained fork of the program, but also apply to the active fork linked above).  
### Note about other (commercial) cheat devices
Providing support for commercial cheat devices (ARMAX, GameShark, etc.) is extremely annoying.  
Most of those devices use their own "encrypted" format for cheat codes, which would require manual conversion for each type that exists (some of them even change their cheat code format from one revision to another!).  
Additionally, I've previously encountered issues with some of these devices not properly supporting all code types, which leads to broken cheats that may even crash the game.  
Meanwhile, CDfPS2 and OPL use a plain and easy to write code format and actually supports everything properly.  
For there reasons, I won't be supporting any of the commercial cheat devices, and instead recommend you mod your PS2 to run CDfPS2 or OPL (which cheat devices can help in doing) (resources below).  

# Modding resources
## Softmods
Technically, it's not even required to *install* any mod to run homebrew, a temporary exploit can be used too (but you may as well install a more convenient softmod while you're at it, eg FMCB/FHDB or OpenTuna).  
The easiest way to achieve that would be ?[FreeDVDBoot](https://github.com/CTurt/FreeDVDBoot?tab=readme-ov-file), but it's not compatible with all models.  
Note that, on the PS2, a softmod by itself does **not** allow to run burned or out-of-region discs, **but OPL can run out-of-region games out of the box**.  
For other methods, check ?[this](https://www.psx-place.com/threads/how-to-hack-playstation-2-in-2025-roadmap.37271/), ?[this](https://consolemods.org/wiki/PS2:PS2_Mods_Wiki) and ?[this](https://www.ps2-home.com/forum/viewtopic.php?p=6434#p6434) (while this one is presented as a guide to install FMCB/FHDB, after you get to the point where you have homebrew running, you can adapt it to run whatever you want). Also note that if there really are no options, it's always possible to buy a memory card preconfigured with your exploit of choice.  
The easiest thing to do in case you have a modded PS2, but want to run homebrew on another one that can't run FDVDB, would be to use the modded PS2 to install FMCB (or OpenTuna) on a memory card and use it to run homebrew on the other console.

## Bypassing region lock and copy protection
Important: as stated above, this is only required for discs; with OPL, you can run out-of-region games without any additional steps.  
If your console is compatible, you can use ?[MechaPwn](https://github.com/MechaResearch/MechaPwn) to run out-of-region and burned discs; or you can use ?[ESR](https://www.psx-place.com/threads/esr.30217/); or you can ?[hardmod](https://quade.co/ps2-modchip-guide/modbo/) if you dare.

# Technical resources
?[WIP technical information about the game](https://kyadlfiles.github.io/technical/)  
?[Cheat code types](https://github.com/mlafeldt/ps2rd/blob/master/Documentation/code_types.txt)  
How .pnach files work: ?[part 1](https://forums.pcsx2.net/Thread-How-PNACH-files-work-2-0 ), ?[part 2](https://forums.pcsx2.net/Thread-Sticky-Important-Patching-Notes-1-7-4546-Pnach-2-0)  
?[Tool to find *hook codes*/*enable codes*](https://www.psx-place.com/resources/freemastercodefinder.1351/)