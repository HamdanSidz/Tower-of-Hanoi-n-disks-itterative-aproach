

# ITERATIVE APPROACH

def towerOfHanoi(disks):
    source = []
    auxilary = []
    end = []

    for i in range(disks):
        disk_name = input(f"Enter {i+1} disk name: ")
        source.append(disk_name)

    loop_to = 2**disks-1
    #print(loop_to)
    print()

    for i in range(1,loop_to+1):
        print(F"STEP: {i}")

        if i%3 == 1:
            if len(end) == 0:
                a = source.pop()
                end.append(a)
                print(f"Move DISK {a} from ROD A to C \n")

            elif len(source) == 0:
                a = end.pop()
                source.append(a)    
                print(f"Move DISK {a} from ROD C to A \n")

            else:    
                a = ord(source.pop())
                b = ord(end.pop())
                if a<b:
                    source.append(chr(a))
                    source.append(chr(b))
                    print(f"Move DISK {chr(b)} from ROD C to A \n")
                else:
                    end.append(chr(b))
                    end.append(chr(a))
                    print(f"Move DISK {chr(a)} from ROD A to C \n")


        elif i%3 == 2:
            if len(auxilary) == 0:
                a = source.pop()
                auxilary.append(a)
                print(f"Move DISK {a} from ROD A to B \n")

            elif len(source) == 0:
                a = auxilary.pop()
                source.append(a)
                print(f"Move DISK {a} from ROD B to A \n")

            else:    
                a = ord(source.pop())
                b = ord(auxilary.pop())
                if a<b:
                    source.append(chr(a))
                    source.append(chr(b))
                    print(f"Move DISK {chr(b)} from ROD B to A \n")
                else:
                    auxilary.append(chr(b))
                    auxilary.append(chr(a))
                    print(f"Move DISK {chr(a)} from ROD A to B \n")


        elif i%3 == 0:
            if len(auxilary) == 0:
                a = end.pop()
                auxilary.append(a)
                print(f"Move DISK {a} from ROD C to B \n")
            
            elif len(end) == 0:
                a = auxilary.pop()
                end.append(a)
                print(f"Move DISK {a} from ROD B to C \n")
            
            else:
                a = ord(auxilary.pop())
                b = ord(end.pop())
                if a<b:
                    auxilary.append(chr(a))
                    auxilary.append(chr(b))
                    print(f"Move DISK {chr(b)} from ROD C to B \n")
                else:
                    end.append(chr(b))
                    end.append(chr(a))
                    print(f"Move DISK {chr(a)} from ROD B to C \n")
            

        print(source)
        print(auxilary)
        print(end)
        print()

        



disks = int(input("Enter no.of disks you wants to go with in your Tower of Hanoi: "))
towerOfHanoi(disks)
