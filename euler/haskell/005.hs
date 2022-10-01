{-
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
-}

divs :: Int -> [Int] -> [Int]
divs n (d:ds)
	| n `mod` d == 0 = d : divs n ds
	| otherwise = []
divs n [] = []

numDivs :: Int -> [Int] -> Int
numDivs n d = length $ divs n d

main = putStrLn $ show $ head $ [x | x <- [20,40..], numDivs x [1..20] == 20]
-- 232792560

-- Or in a more mathematical way
-- foldl1 lcm [1..20]