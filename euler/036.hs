{-
Problem 36: Double­base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
-}

isPalindrome :: [Char] -> Bool
isPalindrome s = s == reverse s

dec2bin :: Int -> [Char]
dec2bin n
	| n == 0 = []
	| even n = '0' : dec2bin (n `div` 2)
	| otherwise = '1' : dec2bin (n `div` 2)

main = putStrLn $ show $ sum$ [n | n <- [1..999999],
									let d = show n,
									let b = dec2bin n,
									isPalindrome d,
									isPalindrome b]
-- 872187
