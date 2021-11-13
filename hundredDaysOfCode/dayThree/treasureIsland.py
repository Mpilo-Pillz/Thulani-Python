print('''
            .--------------------------------------------.
           ( DO YOU KNOW HOW HARD IT IS TO DRAW AN OKAPI? )
          //'--------------------------------------------'
         /      , _.-~~-.__            __.,----.
      (';    __( )         ~~~'--..--~~         '.
(    . \"..-'  ')|                     .       \  '.
 \\. |\.'                    ;       .  ;       ;   ;
  \ \'"   /9)                 '       .  ;           ;
   ; )           )    (        '       .  ;     '    .
    )    _  __.-'-._   ;       '       . ,     /\    ;
    '-'"'--'      ; "-. '.    '            _.-(  ".  (
                  ;    \,)    )--,..----';'    >  ;   .
                   \   ( |   /           (    /   .   ;
     ,   ,          )  | ; .(      .    , )  /     \  ;
,;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,
''')



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("left or right?")


if direction.lower() == "right":
    print("Fall into hole. GAME OVER!")

elif direction.lower() == "left":
    action = input("swim or wait?")

    if action.lower() == "wait":
        print("Attacked by trout. Game Over")

    elif action.lower() == "swim":
        door = input("Which door? Left, right or center")

        if door.lower() == "left":
            print("burned by fire. GAME OVER")

        elif door.lower() == "right":
            print("Eaten by beasts")

        else:
            print("You win")




print('''
          _                 __                 
             __.--**"""**--...__..--**""""*-.            
           .'                                `-.         
         .'                         _           \        
        /                         .'        .    \   _._ 
       :                         :          :`*.  :-'.' ;
       ;    `                    ;          `.) \   /.-' 
       :     `                             ; ' -*   ;    
              :.    \           :       :  :        :    
        ;     ; `.   `.         ;     ` |  '             
        |         `.            `. -*"*\; /        :     
        |    :     /`-.           `.    \/`.'  _    `.   
        :    ;    :    `*-.__.-*""":`.   \ ;  'o` `. /   
              ;   ;                ;  \   ;:       ;:   ,/
         |  | |            [bug]      /`  | ,      `*-*'/ 
         `  : :  :                /  /    | : .    ._.-'  
          \  \ ,  \              :   `.   :  \ \   .'     
           :  *:   ;             :    |`*-'   `*+-*       
           `**-*`""               *---*
''')