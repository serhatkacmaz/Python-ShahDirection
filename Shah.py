list_number = [i for i in range(1, 9)]  #chess numbers
list_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # chess characters


def Shah_Step(h, n):
    """Returns the movements of the Shah, whose position is known."""
    def Go_Right(h, n):
        return (list_character[h+1], list_number[n])  # right move
    def Go_Left(h, n):
        return (list_character[h-1], list_number[n])  # left move
    def Go_Up(h, n):
        return (list_character[h], list_number[n+1])  # up move
    def Go_Down(h, n):
        return (list_character[h], list_number[n-1])  # down move
    def Cross_Right_Up(h, n):
        return (list_character[h+1], list_number[n+1])  # cross right up move
    def Cross_Right_Down(h, n):
        return (list_character[h+1], list_number[n-1])  # cross right down move
    def Cross_Left_Up(h, n):
        return (list_character[h-1], list_number[n+1])  # cross left up move
    def Cross_Left_Down(h, n):
        return (list_character[h-1], list_number[n-1])  # cross left down move
        
    n = list_number.index(n)
    h = list_character.index(h)
    if h == 0 and n == 0:  # the bottom left corner
        return (Go_Right(h, n), Go_Up(h, n), Cross_Right_Up(h, n))
    elif h == 7 and n == 0:  # the bottom right corner
        return(Go_Left(h, n), Go_Up(h, n), Cross_Left_Up(h, n))
    elif n == 7 and h == 0:  # the above left corner 
        return (Go_Right(h, n), Go_Down(h, n), Cross_Right_Down(h, n))
    elif n == 7 and h == 7:  # the above right corner
        return (Go_Left(h, n), Go_Down(h, n), Cross_Left_Down(h, n))
    elif n == 0:  # the bottom edge
        return(Go_Left(h, n), Go_Right(h, n), Go_Up(h, n), Cross_Left_Up(h, n), Cross_Right_Up(h, n))
    elif n == 7:  # the above edge
        return(Go_Left(h, n), Go_Right(h, n), Go_Down(h, n), Cross_Left_Down(h, n), Cross_Right_Down(h, n))
    elif h == 0:  # the left edge
        return (Go_Up(h, n), Go_Down(h, n), Go_Right(h, n), Cross_Right_Up(h, n), Cross_Right_Down(h, n))
    elif h == 7:  # the right edge
        return (Go_Up(h, n), Go_Down(h, n), Go_Left(h, n), Cross_Left_Up(h, n), Cross_Left_Down(h, n))
    else:  # the middle of chess
        return(Go_Left(h, n), Go_Right(h, n), Go_Up(h, n), Go_Down(h, n), Cross_Left_Up(h, n), Cross_Left_Down(h, n), Cross_Right_Up(h, n), Cross_Right_Down(h, n))


print(Shah_Step('a', 8))
print(Shah_Step('h', 1))
print(Shah_Step('h', 5))
print(Shah_Step('d', 1))
print(Shah_Step('e', 6))
print(Shah_Step('g', 3))