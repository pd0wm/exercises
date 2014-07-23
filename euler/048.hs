{-
Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
-}


main = putStrLn $ show $ n
	where
		s = show $ sum [i^i | i <- [1..1000]]
		l = length s
		n = drop (l - 10) s
-- 9110846700

