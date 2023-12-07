# # Scope

# enemies = 1

# # local scope
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# # global scope
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Python does not have block scope
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombies", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# create_enemy()

# Modifying global scope(not recommended for good practice)
enemies = 1

def increase_enemies():
    # global enemies
    # enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")