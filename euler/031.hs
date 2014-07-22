{-
Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation: 
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1x £1 + 1x 50p + 2x 20p + 1x 5p + 1x 2p + 3x 1p

How many different ways can £2 be made using any number of coins?
-}

import Data.Tree

coins = [200, 100, 50, 20, 10, 5, 2, 1]

main = putStrLn $ show $ coins