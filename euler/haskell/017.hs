{-
Problem 17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
-}

import Data.Char

ones :: [String]
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens :: [String]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

writtenNumber :: Int -> String
writtenNumber n
	| n == 0			= ""
	| n == 1000			= "one thousand"
	| n `mod` 100 == 0	= (ones !! h) ++ " " ++ "hundred"
	| n < 20			= ones !! n
	| n < 100 			= (tens !! t) ++ " " ++ (writtenNumber (n - t * 10))
	| n < 1000			= (ones !! h) ++ " " ++ "hundred and" ++ " " ++ (writtenNumber (n - h * 100))	
	| otherwise = "snap het niet"
	where
		t = (n `quot` 10)
		h = (n `quot` 100)

removeSpaces :: String -> String
removeSpaces s = [c | c <- s, isSpace c == False]

main = putStrLn $ show $ sum $ map (length.removeSpaces.writtenNumber) [1..1000]
-- 21124