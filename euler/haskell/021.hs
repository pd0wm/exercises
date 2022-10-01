{-
Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) == b and d(b) == a, where a /= b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
-}

divs :: Int -> [Int]
divs n = [x | x <- [1..(n `quot` 2 + 1)], n `mod` x == 0]

sumDivs :: Int -> Int
sumDivs n = sum $ divs n

isAmicable :: Int -> Bool
isAmicable n = n == a && a /= b
	where
		b = sumDivs n
		a = sumDivs b

main = putStrLn $ show $ sum $ filter isAmicable [1..9999]
-- 31626

-- TODO: add more efficient method to calculate sum divisors