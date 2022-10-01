{-
Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
-}
import Data.Char

factorials :: [Integer]
factorials = [product [1..n] | n <- [0..]]

sumFactorials :: Integer -> Integer
sumFactorials n = sum $ map ((factorials!!).digitToInt) s
	where
		s = show n

main = putStrLn $ show $ limit -- sum [n | n <- [3..limit], n == sumFactorials n]
	where
		limit = 10^(length (takeWhile (\x -> 10^(x-1) < x* (factorials !! 9)) [1..]))
-- 40730
-- this can be sped up by memoization of duplicate sums. ( sumFactorial 42 == sumFactorial 24)