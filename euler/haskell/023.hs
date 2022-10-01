{-
Problem 23: Non­abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.

For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n,
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers.

However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
-}

import Data.List
import qualified Data.IntSet as IntSet

divs :: Int -> [Int]
divs n = [x | x <- [1..(n `quot` 2 + 1)], n `mod` x == 0]

sumDivs :: Int -> Int
sumDivs n = sum $ divs n

isAbundant :: Int -> Bool
isAbundant n = sumDivs n > n

abundantNumbers :: [Int]
abundantNumbers =  filter isAbundant [12..28123]

isNotSum :: Int -> Bool
isNotSum n = length [x | x <- abundantNumbers, IntSet.member (n - x) abundantSet] == 0
	where
		abundantSet = IntSet.fromList abundantNumbers
	

main = putStrLn $ show $ sum $ filter isNotSum [1..28123]
-- 4179871

-- TODO: add more efficient method to calculate sum divisors
