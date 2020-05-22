def BuyMe(prefix="Please buy me", what="something nice", *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)


BuyMe("Please buy me", "a new car")
BuyMe("Please buy me", "a new car", "a cat", "a dog", "a dragon")
BuyMe("Please buy me", "a new car", "a cat", "a dog", "a dragon", shop="market", color="any")


products = ["milk", "bread", "flakes"]

parameters = {"price": "low", "time": "now"}

BuyMe("Buy me", "newspaper", products, parameters)
BuyMe("Buy me", "newspaper", *products, **parameters)   