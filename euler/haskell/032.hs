{-
Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
-}

import Data.List

slice :: Int -> Int -> [Char] -> [Char]
slice from to xs = take (to - from + 1) (drop from xs)

products :: [Int]
products = [z | p <- permutations ['1'..'9'], 
				a <- [0..2],
				let b = 5,
				let x = read (slice 0 a p),
				let y = read (slice (a+1) (b-1) p),
				let z = read (slice b 8 p),
				x * y == z]

main = putStrLn $ show $ sum $ nub $ products
-- 45228
-- This naive approach works but takes around 5s