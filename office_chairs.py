number_of_rooms = int(input())
free_chairs = 0
left_chairs = 0
for current_room in range(1,number_of_rooms+1):
    chairs_in_the_room, people = input().split()
    free_chairs = len(chairs_in_the_room) - int(people)
    left_chairs += free_chairs
    if free_chairs < 0:
        print(f"{abs(free_chairs)} more chairs needed in room {current_room}")


if left_chairs >= 0:
    print(f"Game On, {left_chairs} free chairs left")
