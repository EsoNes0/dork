# """Test the various usable items"""

# import dork.repl


# def test_player_has_none(player):
#     """Tests race case where player contains None"""

#     test_dict = {"name": "leather belt",
#                  "equipped": "leather belt", "inventory": [None, None]}
#     test_player = player
#     test_player.make(test_dict)
#     assert test_player.items == dict(),\
#         "Player copied None object as item"


# def test_look(run):
#     """testing _look for display items and description"""

#     out = run(dork.repl.repl, \
# input_side_effect=["name", "look around", ".rq"])
#     assert "Items:\nsoggy waffle\ntorn parchment\nbroken quill" in out[0],\
#            "item are not found on entrance room"
#     test_game = types.Game()
#     assert test_game._look() == (None, False)


# def test_take(run):
#     """testing _take the method takes all and specific item"""

#     out = run(dork.repl.repl, input_side_effect=["name", "take", ".rq"])
#     assert "You took all item. You took them well." in out[0],\
#            "item are not found on entrance room"
#     out = run(dork.repl.repl, input_side_effect=["name",
#                                                  "take soggy waffle",
#                                                  ".rq"])
#     assert "You took the soggy waffle. You took it well." in out[0],\
#            "item are not found on entrance room"


# def test_drop_item(run):
#     """testing _drop_item the method takes all and specific item"""

#     out = run(dork.repl.repl, input_side_effect=["name", "take soggy waffle",
#                                                  "drop soggy waffle", ".rq"])
#     assert "Oops, you dropped something!" in out[0],\
#            "item are not found on entrance room"


# def test_sword_can_swing(run):
#     """Tests that a sword object calls swingable"""

#     test_sword = types.Item()
#     test_sword.make({"name": "test sword",
#                      "description": "sword of boring",
#                      "stats": [+1, "attack"]})
#     out = run(test_sword.use, "player", test_sword.name)
#     assert out[0] == "You swing the test sword at player\n",\
#                      "use method failed for sword items"


# def test_key_can_open(run):
#     """Tests that a key object calls openable"""

#     test_key = types.Item()
#     test_key.make({"name": "test key",
#                    "description": "jingly keys",
#                    "stats": [+1, "key"]})
#     out = run(test_key.use, "rock", test_key.name)
#     assert out[0] == "You insert the test key into rock\n",\
#                      "use method failed for key items"


# def test_potion_can_speed_up(run):
#     """Tests that a stat changing object calls statable"""

#     test_potion = types.Item()
#     test_potion.make({"name": "test potion",
#                       "description": "Looks like booze to me",
#                       "stats": [-100, "speed"]})
#     out = run(test_potion.use, "player", test_potion.name)
#     assert out[0] == "The test potion takes effect on player\n",\
#                      "use method failed for stat changing items"


# def test_gem_can_be_inserted(run):
#     """Calls that a gem object calls puzzleable"""

#     test_emerald = types.Item()
#     test_emerald.make({"name": "shiny emerald",
#                        "description": "POWERFUL",
#                        "stats": [+1, "emerald"]})
#     out = run(test_emerald.use, "rock", test_emerald.name)
#     assert out[0] == "You try to fit the shiny emerald into the rock\n",\
#                      "use method failed for puzzle items"


# def test_gold_can_pay(run):
#     """Checks that a gold object calls payable"""

#     test_key = types.Item()
#     test_key.make({"name": "bag 'o MOLTEN GOOOLD",
#                    "description": "der bee gould een dem der bag",
#                    "stats": [+100, "gold"]})
#     out = run(test_key.use, "player", test_key.name)
#     assert out[0] == "You use the bag 'o MOLTEN GOOOLD to pay player\n",\
#                      "use method failed for gold items"


# def test_none_item(run):
#     """Checks that an object with none is unusable"""

#     test_key = types.Item()
#     test_key.make({"name": "empty thing",
#                    "description": "nothin",
#                    "stats": None})
#     out = run(test_key.use, "player", "player")
#     assert out[0] == "You find no use of this item\n",\
#                      "use method failed for gold items"


# def test_only_stat(run):
#     """Checks that an object with only a stat is unusable"""

#     test_key = types.Item()
#     test_key.make({"name": "empty thing",
#                    "description": "nothin",
#                    "stats": [+1]})
#     out = run(test_key.use, "player", "player")
#     assert out[0] == "You find no use of this item\n",\
#                      "use method failed for gold items"


# def test_runtime_items(run):
#     """Tests the functionality of items in runtime"""

#     out = run(dork.repl.repl, input_side_effect=["tester",
#                                                  "use sword", ".rq"])
#     assert "You don't have that item...\n" in out[0],\
#            "Failed to decline use on non-existant item"
#     test_item = dork.types.Item()
#     test_item.make({"name": "sword",
#                     "description": "its made of foam",
#                     "stats": [+0, "attack"]})
#     test_game = dork.types.Game()
#     test_game.hero.items["sword"] = test_item
#     out = run(test_game._use_item, "sword", input_side_effect=["player"])
#     assert "You swing the sword at player" in out[0],\
#            "Failed to use item in runtime"


# def test_use_has_target_input(run):
#     """Testing that use takes an input"""

#     out = run(dork.repl.repl, input_side_effect=["tester",
#                                                  "use sword", ".rq"])
#     assert "You don't have that item...\n" in out[0],\
#            "Failed to decline use on non-existant item"
#     test_item = dork.types.Item()
#     test_item.make({"name": "sword",
#                     "description": "its made of foam",
#                     "stats": [+0, "attack"]})
#     test_game = dork.types.Game()
#     test_game.hero.items["sword"] = test_item
#     out = run(test_game._use_item, "sword", input_side_effect=["player"])
#     assert "You swing the sword at player" in out[0],\
#            "failed to contain a target argument"