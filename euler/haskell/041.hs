{-
Problem 41: Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
-}
import Data.Numbers.Primes
import Data.List

pandigitalPrimes :: [Int]
pandigitalPrimes = [n | m <- ['2'..'9'], p <- permutations ['1'..m], let n = read p, isPrime n]

main = putStrLn $ show $ maximum $ pandigitalPrimes
-- 7652413