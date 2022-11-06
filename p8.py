import keyboard

f = open('out.txt', 'r')

lines = f.readlines()

contain = list()

for line in lines:
    contain.append(line)

rem_string = contain[0].split('--')


i = 0
while (i < len(rem_string)):
    print(rem_string[i])
    print("[enter - read more, press q to quit]")
    user = input()
    x = user.isdigit()
    if x:
        i += int(user)

    elif user == "q":
        break
    else:
        i += 1

f.close()
