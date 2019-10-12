
def character_class(class_type):

    health = 0
    attack = 0
    defence = 0
    evasion = 0
    sneak = 0
    persuasion = 0
    magic = 0
    intelligence = 0
    
    if class_type == "knight":
        
        print("  ________\n**|KNIGHT|**\n  --------")
        print("High health, attack, and defence with reasonable persuasion and intelligence; Knights are well rounded characters")
        print("Although, careful if retreating from battle and don't expect to sneak by many enemys")
        
        health = 20
        attack = 15
        defence = 15
        evasion = 3
        sneak = 2
        persuasion = 7
        magic = 1
        intelligence = 10
        
        print("  ________\n**|STATS|**\n  --------")
        print("Hp",health,"\nAtk",attack,"\nDef",defence,"\nEvasion",evasion,"\nSneak",sneak,"\nPersuasion",persuasion)
        print("Magic",magic,"\nIntelligence",intelligence)
        
    
    elif class_type == "mage":
        
        print("  _______\n**|MAGE|**\n  -------")
        print("The Mage has oppertunities to gain experience by reading magic books and recipies. Can use magic to play the game uniquly")
        print("Low attack early game means relying on magic and non combat options to  level up")
        
        health = 15
        attack = 5
        defence = 5
        evasion = 10
        sneak = 7
        persuasion = 10
        magic = 20
        intelligence = 15
        
        print("  ________\n**|STATS|**\n  --------")
        print("Hp",health,"\nAtk",attack,"\nDef",defence,"\nEvasion",evasion,"\nSneak",sneak,"\nPersuasion",persuasion)
        print("Magic",magic,"\nIntelligence",intelligence)
    
    
    elif class_type == "theif":
        
        print("  ________\n**|THEIF|**\n  --------")
        print("Theifs use higher stealth and evasion to pass or trap enemys")
        print("In battle, they avoid attack and can usually escape combat in difficult situations")
        
        health = 10
        attack = 10
        defence = 5
        evasion = 20
        sneak = 20
        persuasion = 10
        magic = 5
        intelligence = 5
        
        print("  ________\n**|STATS|**\n  --------")
        print("Hp",health,"\nAtk",attack,"\nDef",defence,"\nEvasion",evasion,"\nSneak",sneak,"\nPersuasion",persuasion)
        print("Magic",magic,"\nIntelligence",intelligence)
        
        
    elif class_type == "minstrel":
        
        print("  __________\n**|MINSTREL|**\n  ----------")
        print("The Minstrel uses charm, wit, and stealth to progress through their objectives")
        print("Make sure to avoid stright forward fights and retreat if suprised or cought off guard")
        
        health = 5
        attack = 5
        defence = 5
        evasion = 15
        sneak = 12
        persuasion = 30
        magic = 5
        intelligence = 12
        
        print("  ________\n**|STATS|**\n  -------")
        print("Hp",health,"\nAtk",attack,"\nDef",defence,"\nEvasion",evasion,"\nSneak",sneak,"\nPersuasion",persuasion)
        print("Magic",magic,"\nIntelligence",intelligence)
        
        
    elif class_type == "bowman":
        
        print("  ________\n**|ARCHER|**\n  --------")
        print("The Archer can use their bow to defeat enemys head on, or with stealth. Try using the bow to play the game unconventionally")
        print("Your defence and health are low so remeber to evade taking damage at all cost")
        
        health = 10
        attack = 15
        defence = 5
        evasion = 15
        sneak = 15
        persuasion = 5
        magic = 1
        intelligence = 5
        
        print("  ________\n**|STATS|**\n  --------")
        print("\nHp",health,"\nAtk",attack,"\nDef",defence,"\nEvasion",evasion,"\nSneak",sneak,"\nPersuasion",persuasion)
        print("Magic",magic,"\nIntelligence",intelligence)
        
    return health, attack, defence, evasion, sneak, persuasion, magic, intelligence

    

    



