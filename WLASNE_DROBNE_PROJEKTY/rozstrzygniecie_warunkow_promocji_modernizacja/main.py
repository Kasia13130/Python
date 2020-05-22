min_like = 500
min_share = 100

num_like = 600
num_share = 250

if num_like >= min_like and num_share >= min_share:
    print("The prizes is -10%")
else:
    if num_like < min_like:
        print("Not enough likes, price is the same")
    else:
        print("We need more shares")

# modernizacja - ciag dalszy
min_like = 500
min_share = 100

num_like = 400
num_share = 50

if num_like >= min_like and num_share >= min_share:
    print("The prizes is -10%")
elif num_share < min_share:
    print("Not enough shares, price is the same")
else:
    print("We need more likes")