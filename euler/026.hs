{-
Problem 26: Reciprocal cycles
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
-}

import Data.List

-- Use the recurrence of remainders i a long division to determine the cycle length
divide :: Int -> [Int] -> Int -> [Int]
divide rem rems d
	| rem == 0 = [] -- The long division is finished, so no cycle at all
	| rem' `elem` rems = rem' : takeWhile (/= rem') rems -- Determine if this remainder has been found already, return the remainders of the cycle only
	| otherwise = divide rem' (rem':rems) d -- Calculate next step in long division
	where
		rem' = 10 * (rem `mod` d)

--main = putStrLn $ show $ divide 10 [10] 6
main = putStrLn $ show $ snd $ maximum $ zip (map (length.divide 1 []) [1..1000]) [1..]
-- 983