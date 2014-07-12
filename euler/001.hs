{-
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. 

Find the sum of all the multiples of 3 or 5 below 1000.
-}

import Data.List (union)

divs :: Int -> Int -> [Int]
divs a max = [x | x <- [1..max], x `mod` a == 0]

divsTwo :: Int -> Int -> Int -> [Int]
divsTwo a b max = (divs a max) `union` (divs b max)

main = putStrLn $ show $ sum $ divsTwo 3 5 999
-- 233168

-- Or direct:
-- sum [x | x <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]