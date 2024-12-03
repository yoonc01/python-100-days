print("""
                         __
                  / \--..____
                   \ \       \-----,,,..
                    \ \       \         \--,,..
                     \ \       \         \  ,'
                      \ \       \         \ ``..
                       \ \       \         \-''
                        \ \       \__,,--'''
                         \ \       \.
                          \ \      ,/
                           \ \__..-
                            \ \\
                             \ \\
                              \ \   :F_P:
                               \ \\
                                \ \\
                                 \ \\
                                  \ \\
                                   \ \\
                                    \ \\
      """)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Left or Right? ")
if (direction.lower() == "left"):
    action = input("Swim or Wait? ")
    if (action.lower() == "wait"):
        color = input("Which door? Red? Yellow? Blue? ")
        lower_case_color = color.lower()
        if (lower_case_color == "Red"):
            print("Burned by fire\nGame Over.")
        elif (lower_case_color == "Blue"):
            print("Eaten by beasts.\nGame Over")
        elif (lower_case_color == "Yellow"):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
