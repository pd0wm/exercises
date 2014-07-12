{-
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
-}


main = putStrLn $ show $ head [a*b*c | c <- [1..], b <- [(1000-c) `quot` 2..c], let a = 1000 - c - b, a^2 + b^2 == c^2]
-- 31875000

{-
b <- [(1000-c) `quot` 2..c] because:

a = 1000 - b - c
a < b

thus
1000 - b - c < b ==> 2b > 1000 - c
-}
