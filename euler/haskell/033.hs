{-
Problem 33: Digit canceling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
-}
import Data.Ratio

fractions = [a%d | d <- [1..9], a <- [1..(d-1)], 9*a*d `mod` (10*a - d) == 0, 9*a*d < 100*a - 10*d]
main = putStrLn $ show $ denominator $ product fractions
-- 100