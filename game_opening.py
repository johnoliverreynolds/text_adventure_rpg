from character_templates import character_class
import battle_system_fn



if __name__ == "__main__":
  while(True):

      character_classtype = input("\nWhat profession will you choose? \nKnight\nBowman\nMage\nTheif\nMinstrel\n")
      character_classtype = str.lower(character_classtype)


      if character_classtype == "knight" or "bowman" or "mage" or "theif" or "minstrel":
          profession = character_class(character_classtype)
          reselect = input("\nWould you like to choose as your profession? (Y/N) ")
          reselect = str.lower(reselect)
          if reselect == "y":
              break
          else:
              continue
      
          
          
      else:
          print("\nThe profession you chose was invalid \nPlease try again\n")
          
      
      