{-
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
-}

import Data.Numbers.Primes

-- Implement factorization by hand
factors :: Int -> [Int] -> [Int]
factors n (p:ps)
	| p * p > n = [n] -- No factors will be found anymore, n is the last prime factor
	| n `mod` p == 0 = p : factors (n `div` p) (p:ps) -- p is a factor, divide and continue
	| otherwise = factors n ps -- p is no prime factor, continue with the rest of the primes
--main = putStrLn $ show $ maximum $ factors 600851475143 primes

-- Use built in factorization
main = putStrLn $ show $ maximum $ primeFactors 600851475143
-- 6857