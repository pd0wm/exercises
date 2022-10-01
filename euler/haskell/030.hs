{-
Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
-}

import Data.Char

sumDigitsPower :: Int -> Int -> Int
sumDigitsPower n k = sum $ map ((^k).digitToInt) $ show n

limit :: Int -> Int
limit k = 10^(length (takeWhile (\x -> 10^(x-1) < x*9^k) [1..]))

main = putStrLn $ show $ sum $ [x | x <- [10..(limit 5)], x == sumDigitsPower x 5]
-- 443839