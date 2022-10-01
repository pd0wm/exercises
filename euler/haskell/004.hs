{-
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. 
Find the largest palindrome made from the product of two 3-digit numbers.
-}

isPalindrome :: Int -> Bool
isPalindrome n = s == reverse s
	where
		s = show n

products :: [Int]
products = [x * y | x <- [100..999], y <- [100..999]]

main = putStrLn $ show $ maximum $ filter isPalindrome products
-- 906609