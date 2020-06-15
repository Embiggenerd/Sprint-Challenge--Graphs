from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph_dict = {}



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

def get_blind_exit_bfs(starting_room):
    q = []
    visited = set()
    q.append([starting_room])
    # BFS algo
    while len(q) > 0:
        path_to_current_room = q.pop(0)
        current_room = path_to_current_room[-1]
        # Here we check if our graph_dict[room] contains any blind exits, in which case we're good and we return path
        # This is what makes this a search, not a traversal
        for key in graph_dict[current_room]:
            if graph_dict[current_room][key] == "?":
                return path_to_current_room
        if current_room not in visited:
            visited.add(current_room)
            # After current room added to visted, we need queue up rooms that needs to check for unexplored exits
            # Important to remember, that we are exploring the already explored graph that we are building, not
            # trabeling in breadth first fashion
            for room in graph_dict[current_room]:
                q.append([*path_to_current_room, room])

# This step creates a room in our graph_dict


def create_vertex(room):
    room_dict = {}
    for e in room.get_exits():
        room_dict[e] = "?"
    graph_dict[room.id] = room

# Here we append any room which is unknown to a list, and select
# one randomly

def get_random_blind_exit(room):
    blind = []
    for e in room.get_exits():
        # rooms in our graph_dict are refernced by id
        if graph_dict[room.id][e] == "?":
            blind.append(e)

    return random.choice(blind)

def room_has_blind_exits(room):
    has_blind_exits = False
    for e in graph_dict[room.id].get_exits():
        if e == "?":
            had_blind_exits = True
            break
    return has_blind_exits


create_vertex(player.current_room)

while len(graph_dict) < 500:
    if room_has_blind_exits(player.current_room):
        


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
