{-
Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
-}

import Data.Numbers.Primes
import Data.List

rotate :: Int -> [a] -> [a]
rotate _ [] = []
rotate n xs = zipWith const (drop n (cycle xs)) xs

rotations :: Int -> [Int]
rotations x = [read (rotate n s) | n <- [0..(length s)-1]]
	where
		s = show x

allPrime :: Int -> Bool
allPrime n = all isPrime (rotations n)

isSorted :: Int -> Bool
isSorted n = s == sort s
	where
		s = show n

main = putStrLn $ show $ length $ filter allPrime [1..999999]
-- 5