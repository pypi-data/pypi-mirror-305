# FIX RAIDEN BOSS
[![PyPI](https://img.shields.io/pypi/pyversions/FixRaidenBoss2)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/FixRaidenBoss2)](https://pypi.org/project/FixRaidenBoss2/)
[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/nhok0169/Fix-Raiden-Boss/total?label=Github%20Downloads)](https://github.com/nhok0169/Fix-Raiden-Boss)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/FixRaidenBoss2?label=Pypi%20Downloads)](https://pypi.org/project/FixRaidenBoss2/)
[![Documentation Status](https://readthedocs.org/projects/fix-raiden-boss/badge/?version=latest)](https://fix-raiden-boss.readthedocs.io/en/latest/?badge=latest)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nhok0169/Fix-Raiden-Boss/unit-tests.yml?label=Unit%20Tests)](https://github.com/nhok0169/Fix-Raiden-Boss/actions/workflows/unit-tests.yml)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nhok0169/Fix-Raiden-Boss/integration-tests.yml?label=Integration%20Tests)](https://github.com/nhok0169/Fix-Raiden-Boss/actions/workflows/integration-tests.yml)


<a href=""><img alt="" src="https://github.com/nhok0169/Fix-Raiden-Boss/blob/nhok0169/Docs/src/_static/images/raiden.jpg" style="width:750px; height: auto;"></a>
- Author Ideal [NK#1321](https://discordapp.com/users/277117247523389450)
- Thank [SilentNightSound#7430](https://github.com/SilentNightSound) for the logic rewrite
- Thank HazrateGolabi#1364 for combine and make final script
- Thank [Albert Gold#2696](https://github.com/Alex-Au1) for update the code for merged mods
## Requirements 
- [Python (version 3.6 and up)](https://www.python.org/downloads/)

<br>

> [!WARNING]  
> Remapping mods is overall a hacky process. Please see a mod's [remap grading](https://fix-raiden-boss.readthedocs.io/en/latest/remapGrading.html) for the current limitations
> of remapping a particular mod before posting an issue

<br>

## VIDEO TUTORIAL AND EXAMPLES:

### Quickstart
**Individual Mod:** https://www.youtube.com/watch?v=29FM0GywcWA  
**Merged Mods:** https://www.youtube.com/watch?v=nEyMYIHdrQM  
**Mega Merged Mods:** https://www.youtube.com/watch?v=08co5ct7zeg  

### More Features
[More examples here](https://github.com/nhok0169/Fix-Raiden-Boss/tree/nhok0169/Examples)

<br>

## How to Run
- Choose your pick of which way to run the script:

  - **Choice A:** &nbsp; [Quickstart!](#choice-a-lets-start--) 🟢 &nbsp;&nbsp; (for beginners)
  - **Choice B:** &nbsp; [CMD WITHOUT a Script](#choice-b-run-on-cmd-without-a-script-) 🟡 &nbsp;&nbsp; (recommended if you run by CMD)
  - **Choice C:** &nbsp; [CMD with a Script](#choice-c-run-on-cmd-with-a-script-) 🟡 &nbsp;&nbsp; (the convention that other GIMI scripts follow)
  - **Choice D:** &nbsp; [API](#choice-d-api-usage-)  🟠 &nbsp;&nbsp; (for expert coders)

<br>

## Choice A: Let's Start ! 🟢
### STEP 1:
- Go to the [Latest Release](https://github.com/nhok0169/Fix-Raiden-Boss/releases/latest) and click on the ``FixRaidenBoss2.py`` link to download the script into your Raiden Mod folder or GIMI's `Mod` folder.

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 2:
- Double click on the script
### STEP 3:
- Open the game and enjoy it

## Choice B: Run on CMD Without a Script 🟡
### STEP 1:
- Install the module onto your computer by [opening cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) and typing :
```python
python -m pip install -U FixRaidenBoss2
```
then enter

*( you can now run the program anywhere without copying a script! )*

### STEP 2:
- [open cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) in your Raiden Mod folder or GIMI's `Mod` folder and type:
```python
python -m FixRaidenBoss2
```
then enter

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 3:
- Open the game and enjoy it

## Choice C: Run on CMD With a Script 🟡
### STEP 1:
- Go to the [Latest Release](https://github.com/nhok0169/Fix-Raiden-Boss/releases/latest) and click on the ``FixRaidenBoss2.py`` link to download the script into your Raiden Mod folder or GIMI's `Mod` folder.

### STEP 2:
- [open cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) and type
```python
python FixRaidenBoss2.py
```
then enter

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 3:
- Open the game and enjoy it

## Command Options
| Options | Description |
| --- | --- |
| -h, --help | show this help message and exit |
| -s str, --src str | The starting path to run this fix. If this option is not specified, then will run the fix from the current directory. |
| -v str, --version str | The game version we want the fix to be compatible with. If this option is not specified, then will use the latest game version. |
| -d, --deleteBackup | deletes backup copies of the original .ini files |
| -f, --fixOnly | only fixes the mod without cleaning any previous runs of the script |
| -u, --undo | Undo the previous runs of the script |
| -l str, --log str | The folder location to log the printed out text into a seperate .txt file. If this option is not specified, then will not log the printed out text. |
| -a, --all | Parses all *.ini files that the program encounters. This option supersedes the --types |
| -dt str, --defaultType str | The default mod type to use if the *.ini file belongs to some unknown mod <br> If the --all option is set to True, then this argument will be 'raiden'. <br> Otherwise, if this value is not specified, then any mods with unknown types will be skipped <br> <br> See below for the different names/aliases of the supported types of mods. |
| -t str, --types str | Parses *.ini files that the program encounters for only specific types of mods. If the --all option has been specified, this option has no effect. <br> By default, if this option is not specified, will parse the *.ini files for all the supported types of mods. <br> <br> Please specify the types of mods using the the mod type's name or alias, then seperate each name/alias with a comma(,) <br> &nbsp; &nbsp; &nbsp; *eg. raiden,arlecchino,ayaya* |
| -rt str, --remappedTypes str |  From all the mods to fix, specified by the --types option, will specifically remap those mods to the mods specified by this option. <br> For a mod specified by the --types option, if none of its corresponding remapped mods are specified by this option, then the mod specified by the --types option will be remapped to all its corresponding mods. <br> <br> ------------------- <br> eg. <br> If this program was ran with the following options: <br> --types kequeen,jean <br> --remappedTypes jeanSea <br> <br> the program will do the following remap: <br> keqing --> keqingOpulent <br> Jean --> JeanSea <br> <br> Note that Jean will not remap to JeanCN <br> ------------------- <br> <br> By default, if this option is not specified, will remap all the mods specified in --types to their corresponding remapped mods. <br> <br> Please specify the types of mods using the the mod type's name or alias, then seperate each name/alias with a comma(,) <br> eg. raiden,arlecchino,ayaya <br> <br> See below for the different names/aliases of the supported types of mods. |

<br>

## Mod Types
Below are the supported types of mods

| Name | Aliases | Description |
| --- | --- | ---|
| Amber | BaronBunny, ColleisBestie | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Amber)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| AmberCN | BaronBunnyCN, ColleisBestieCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(AmberCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Arlecchino | Father, Harlequin, Knave, Perrie, Peruere | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Arlecchino)((?!RemapBlend).)*Blend.*\s*\]` |
| Barbara | Healer, Idol | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Barbara)((?!RemapBlend|Summertime).)*Blend.*\s*\]` |
| BarabaraSummertime | BarbaraBikini, HealerSummertime, IdolSummertime | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(BarbaraSummertime)((?!RemapBlend).)*Blend.*\s*\]` |
| Ganyu | Cocogoat | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Ganyu)((?!(RemapBlend|Twilight)).)*Blend.*\s*\]` |
| GanyuTwilight | CocogoatLanternRite, CocogoatTwilight, GanyuLanternRite, LanternRiteCocogoat, LanternRiteGanyu | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(GanyuTwilight)((?!(RemapBlend)).)*Blend.*\s*\]` |
| Jean | ActingGrandMaster, KleesBabySitter | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Jean)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| JeanCN | ActingGrandMasterCN, KleesBabySitterCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(JeanCN)((?!RemapBlend).)*Blend.*\s*\]` |
| JeanSea | ActingGrandMasterSea, KleesBabySitterSea | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(JeanSea)((?!RemapBlend|CN).)*Blend.*\s*\]` |
| Keqing | Kequeen, MoraxSimp, ZhongliSimp | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Keqing)((?!(RemapBlend|Opulent)).)*Blend.*\s*\]` |
| KeqingOpulent | CuterKeqing, CuterKequeen, KeqingLaternRite, KequeenLanternRite, KequeenOpulent, LanternRiteKeqing, LanternRiteKequeen, LaternRiteMoraxSimp, LaternRiteZhongliSimp, MoraxSimpLaternRite, MoraxSimpOpulent, ZhongliSimpLaternRite, ZhongliSimpOpulent | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(KeqingOpulent)((?!RemapBlend).)*Blend.*\s*\]` |
| Mona | BigHat, NoMora | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Mona)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| MonaCN | BigHatCN, NoMoraCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(MonaCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Ningguang | GeoMommy, SugarMommy | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Ningguang)((?!(RemapBlend|Orchid)).)*Blend.*\s*\]` |
| NingguangOrchid | GeoMommyLaternRite, GeoMommyOrchid, LanternRiteNingguang, LanternRiteSugarMommy, LaternRiteGeoMommy, NingguangLanternRite, SugarMommyLanternRite, SugarMommyOrchid | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(NingguangOrchid)((?!RemapBlend).)*Blend.*\s*\]` |
| Raiden | Cryden, CrydenShogun, Ei, RaidenEi, RaidenShogun, RaidenShotgun, Shogun, Shotgun, SmolEi | check if the .ini file contains a section matching the regex, `^\s\*\[\s\*TextureOverride.\*(Raiden\|Shogun)((?!RemapBlend).)\*Blend.\*\s\*\]` |
| Rosaria | GothGirl | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Rosaria)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| RosariaCN | GothGirlCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(RosariaCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Shenhe | RedRopes, YelansBestie | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Shenhe)((?!RemapBlend|FrostFlower).)*Blend.*\s*\]` |
| ShenheFrostFlower | LanternRiteRedRopes, LanternRiteShenhe, LanternRiteYelansBestie, RedRopesFrostFlower, RedRopesLanternRite, ShenheLanternRite, YelansBestieFrostFlower, YelansBestieLanternRite | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(ShenheFrostFlower)((?!RemapBlend).)*Blend.*\s*\]` |
<br>
<br>

## Choice D: API Usage 🟠

Tool developpers can now include the fix within their code!

### API Documentation
For more info about how to use the API, visit the documentation at https://fix-raiden-boss.readthedocs.io/en/latest/

<br>

### API Setup

<br>

*Make sure you first install the module by typing into [cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd):*
```bash
python -m pip install -U FixRaidenBoss2
```
<br>

### API Examples

See the documentation for more detailed [examples](https://fix-raiden-boss.readthedocs.io/en/latest/apiExamples.html) on how to use the API.

<br>

Below is a ***preview*** that gives a feel of using the API

<br>

*eg. Running the following code under [this folder](https://github.com/nhok0169/Fix-Raiden-Boss/tree/nhok0169/Testing/Integration%20Tester/Tests/MixedModsTests/inputs/Mods)*

```python
import FixRaidenBoss2 as FRB

fixService = FRB.RemapService(keepBackups = False)
fixService.fix()

print("The Raiden Mod is fixed!")
```
<br>

<details>
<summary>Example Result</summary>
<br>

```
===== Types of Mods To Fix =====

- Raiden

================================


# Mods/Ayaka/Raiden --> Removing any previous changes from this script in raiden.ini
# Mods/Ayaka/Raiden --> 
# Mods/Ayaka/Raiden --> Parsing raiden.ini...
# Mods/Ayaka/Raiden --> Fixing the Blend.buf files for raiden.ini...
# Mods/Ayaka/Raiden --> Making the fixed ini file for raiden.ini
# Mods/Ayaka/Raiden --> 

# Mods/Ei/Raiden --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/Body/BodyEntityRemapBlend.buf
# Mods/Ei/Raiden --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/leftWing/LeftWingEntityRemapBlend.buf
# Mods/Ei/Raiden --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/rightWing/RightWingEntityRemapBlend.buf
# Mods/Ei/Raiden --> 
# Mods/Ei/Raiden --> Removing any previous changes from this script in tri_merge_core.ini
# Mods/Ei/Raiden --> 
# Mods/Ei/Raiden --> Parsing tri_merge_core.ini...
# Mods/Ei/Raiden --> Fixing the Blend.buf files for tri_merge_core.ini...
# Mods/Ei/Raiden --> Blend file correction done at absolute/path/Mods/Ei/Raiden/Body/BodyEntityRemapBlend.buf
# Mods/Ei/Raiden --> Blend file correction done at absolute/path/Mods/Ei/Raiden/leftWing/LeftWingEntityRemapBlend.buf
# Mods/Ei/Raiden --> Blend file correction done at absolute/path/Mods/Ei/Raiden/rightWing/RightWingEntityRemapBlend.buf
# Mods/Ei/Raiden --> Making the fixed ini file for tri_merge_core.ini
# Mods/Ei/Raiden --> 

# Mods/Ei/Raiden/leftWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/rightWing/listeners/rightWingListenerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/Body/listeners/heartListenerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/rightWing/controllers/rightWingControllerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/Body/controllers/heartPumpControllerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> 
# Mods/Ei/Raiden/leftWing --> Removing any previous changes from this script in left_wing_merge.ini
# Mods/Ei/Raiden/leftWing --> 
# Mods/Ei/Raiden/leftWing --> Parsing left_wing_merge.ini...
# Mods/Ei/Raiden/leftWing --> Fixing the Blend.buf files for left_wing_merge.ini...
# Mods/Ei/Raiden/leftWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/rightWing/listeners/rightWingListenerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/Body/listeners/heartListenerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/leftWing/LeftWingEntityRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/rightWing/controllers/rightWingControllerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/Body/controllers/heartPumpControllerRemapBlend.buf
# Mods/Ei/Raiden/leftWing --> Making the fixed ini file for left_wing_merge.ini
# Mods/Ei/Raiden/leftWing --> 

# Mods/Ei/Raiden/rightWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/leftWing/listeners/leftWingListenerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/leftWing/controllers/leftWingControllerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> 
# Mods/Ei/Raiden/rightWing --> Removing any previous changes from this script in right_wing_merge.ini
# Mods/Ei/Raiden/rightWing --> 
# Mods/Ei/Raiden/rightWing --> Parsing right_wing_merge.ini...
# Mods/Ei/Raiden/rightWing --> Fixing the Blend.buf files for right_wing_merge.ini...
# Mods/Ei/Raiden/rightWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/leftWing/listeners/leftWingListenerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/Body/listeners/heartListenerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/rightWing/RightWingEntityRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> Blend file correction done at absolute/path/Mods/Ei/Raiden/leftWing/controllers/leftWingControllerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/Body/controllers/heartPumpControllerRemapBlend.buf
# Mods/Ei/Raiden/rightWing --> Making the fixed ini file for right_wing_merge.ini
# Mods/Ei/Raiden/rightWing --> 

# Mods/Ei/Raiden/Body/Center --> No Previous RemapBlend.buf found at absolute/path/Makoto/MakotoRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> No Previous RemapBlend.buf found at absolute/path/Mods/Ei/Raiden/Body/whoopsIReferencedTheWrongThingRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> Removing any previous changes from this script in heart.ini
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> Parsing heart.ini...
# Mods/Ei/Raiden/Body/Center --> Fixing the Blend.buf files for heart.ini...
# Mods/Ei/Raiden/Body/Center --> Blend file correction done at absolute/path/Makoto/MakotoRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/rightWing/listeners/rightWingListenerRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/leftWing/listeners/leftWingListenerRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> FileNotFoundError: [Errno 2] No such file or directory: 'absolute/path/Mods/Ei/Raiden/Body/whoopsIReferencedTheWrongThing.buf'
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> Traceback (most recent call last):
# Mods/Ei/Raiden/Body/Center -->   File "absolute/path/../../Fix-Raiden-Boss 2.0 (for all user )/api/src/FixRaidenBoss2/FixRaidenBoss2.py", line 4241, in correctBlend
# Mods/Ei/Raiden/Body/Center -->     correctedBlendPath = self.blendCorrection(origFullPath, modType, fixedBlendFile = fixedFullPath)
# Mods/Ei/Raiden/Body/Center -->   File "absolute/path/../../Fix-Raiden-Boss 2.0 (for all user )/api/src/FixRaidenBoss2/FixRaidenBoss2.py", line 4120, in blendCorrection
# Mods/Ei/Raiden/Body/Center -->     with open(blendFile, "rb") as f:
# Mods/Ei/Raiden/Body/Center --> FileNotFoundError: [Errno 2] No such file or directory: 'absolute/path/Mods/Ei/Raiden/Body/whoopsIReferencedTheWrongThing.buf'
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods/Ei/Raiden/Body/Center --> 
# Mods/Ei/Raiden/Body/Center --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/rightWing/controllers/rightWingControllerRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> Blend file has already been corrected at absolute/path/Mods/Ei/Raiden/leftWing/controllers/leftWingControllerRemapBlend.buf
# Mods/Ei/Raiden/Body/Center --> Making the fixed ini file for heart.ini
# Mods/Ei/Raiden/Body/Center --> 

# Mods --> 
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods --> 
# Mods --> WARNING: The following Blend.buf files were skipped due to warnings (see log above):
# Mods --> 
# Mods --> ===== Mod: Mods/Ei/Raiden/Body/Center =====
# Mods --> 
# Mods --> - Ei/Raiden/Body/whoopsIReferencedTheWrongThingRemapBlend.buf:
# Mods --> 	--- FileNotFoundError ---
# Mods --> 	[Errno 2] No such file or directory: 'absolute/path/Mods/Ei/Raiden/Body/whoopsIReferencedTheWrongThing.buf'
# Mods --> 
# Mods --> ===========================================
# Mods --> 
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods --> 
# Mods --> 
# Mods --> 
# Mods --> ========== Summary ==========
# Mods --> 
# Mods --> - Out of 5 found mods, fixed 5 mods and skipped 0 mods
# Mods --> - Out of the 5 *.ini files within the found mods, fixed 5 *.ini files and skipped 0 *.ini file files
# Mods --> - Out of the 11 Blend.buf files within the found mods, fixed 10 Blend.buf files and skipped 1 Blend.buf files
# Mods --> 
# Mods --> =============================
# Mods --> 

The Raiden Mod is fixed!
```
</details>
<br>
