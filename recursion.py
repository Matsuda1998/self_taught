def bottles_of_beer(bob):
    """pram:bobは正の整数でなければ
    いけません"""
    if bob < 1 :
        print("""
        No more bottles of beer on tha wall.
        No more bottles of beer.""")
        return
    temp=bob
    bob -= 1
    print("""
        {} bottles of beer on the wall.
        {} bottles of beer.
        Take on down,pass it around,
        {} bottles of beer on the wall.""".format(temp,temp,bob))
    bottles_of_beer(bob)

bottles_of_beer(5)

