{-
Problem 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.

We will call 192 384 576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 9 18 27 36 45, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
-}

import Data.List

merge :: [Int] -> [Char]
merge ns = concat $ map (show) ns

numbers :: Int -> Int -> [Char]
numbers x m = merge [x * n | n <- [1..m]]

products :: [Int]
products = [read p | p <- (reverse $ sort $ permutations ['1'..'9']),
					 n <- [2..5], m <- [2..4],
					 let x = read (take n p),
					 let s = numbers x m,
					 s == p]

main = putStrLn $ show $ head $ products
-- 932718654