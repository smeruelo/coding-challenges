#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

def find_captains_room(room_list):
    rooms = set()
    repeated_rooms = set()
    for r in room_list:
        if r in rooms:
            repeated_rooms.add(r)
        else:
            rooms.add(r)
    return list(rooms.difference(repeated_rooms))[0]

if __name__ == '__main__':
    _ = raw_input()
    print find_captains_room(raw_input().split())

