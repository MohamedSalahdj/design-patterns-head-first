from characters import Knight, Queen, King

from behaviors import BowAndArrowBehavior

if __name__ == "__main__":
    knight = Knight()
    queen = Queen()
    king = King()

    knight.fight()
    print("-> Change weapon to Bow and Arrow")
    knight.set_weapon_behavior(BowAndArrowBehavior())
    knight.fight()
    print("-"*25)

    queen.fight()
    king.fight()

