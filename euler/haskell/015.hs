{-
Problem 15: Lattice paths

Starting in the top left corner of a 2 corner.
There are exactly 6 routes to the bottom right

How many such routes are there through a 20x20 grid.
-}

factorial :: Integer -> Integer
factorial n = foldl1 (*) [1..n]

nCr :: Integer -> Integer -> Integer
nCr n k = factorial n `div` (factorial k * factorial (n-k))

main = putStrLn $ show $ nCr 40 20
-- 137846528820