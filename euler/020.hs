{-
Problem 20: Factorial digit sum

n! means n x (n 1) x ... 3 x 2 x1
For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
-}

import Data.Char

factorial :: Integer -> Integer
factorial n = foldl1 (*) [1..n]

sumDigits :: Integer -> Integer
sumDigits n = sum $ map (toInteger.digitToInt) $ show n

main = putStrLn $ show $ sumDigits $ factorial 100
-- 648