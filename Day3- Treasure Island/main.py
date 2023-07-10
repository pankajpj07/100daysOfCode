print('''
      .-.
          [.-''-.,
          |  //`~\)
          (<| 0\0|>_
          ";\  _"/ \\_ _,
         __\|'._/_  \ '='-,
        /\ \    || )_///_\>>
       (  '._ T |\ | _/),-'
        '.   '._.-' /'/ |
        | '._   _.'`-.._/
  snd   ,\ / '-' |/
        [_/\-----j
   _.--.__[_.--'_\__
  /         `--'    '---._
 /  '---.  -'. .'  _.--   '.
 \_      '--.___ _;.-o     /
   '.__ ___/______.__8----'
     c-'----'
      ''')

# above ascii art taken from https://www.asciiart.eu/movies/aladdin by Shanaka Dias

print("Welcome to Treasure Island")
print("Your mission is to find the treasure..")
direction = input("You are at a cross road. Where do you wanna go? 'left' or 'right'\n").lower()
if direction=="left":
    swimOrWait=input("you came to a lake. You wanna swim or wait for a boat?\n").lower()
    if swimOrWait=="wait":
        door=input("Now you need to choose one door. Which one would you choose. yellow, red or blue?\n").lower()
        if door=="yellow":
            print("Congratulations!!! You found the treasure")
        else:
            print("You chose the wrong door, Karen. ☹   Game Over  ☹")
    else:
        print("You got killed by a crocodile. ☹   Game Over  ☹")
else:
    print("You Fell into a Hole. ☹   Game Over  ☹")
    
