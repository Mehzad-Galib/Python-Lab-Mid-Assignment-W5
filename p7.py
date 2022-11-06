import keyboard

f = open('out.txt', 'r')

lines = f.readlines()

contain = list()

for line in lines:
    contain.append(line)

rem_string = contain[0].split('--')

for j in range(len(rem_string)):
    print(rem_string[j])
    print("[enter - read more, press q to quit]")
    user = int(input())
    j += user
    # page = int(input('Enter pages to go forward: '))
    if keyboard.read_key() == "ENTER":
        print("enter pressed so going forward")
        pass
    elif keyboard.read_key() == "q":
        break

    else:
        pass


f.close()
