{-
Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
-}

triplets :: Int -> [(Int, Int, Int)]
triplets p = [(a,b,c) | a <- [1..1000], b <- [1..a], let c = p - a - b, c > 0, a*a + b*b == c*c]

main = putStrLn $ show $ snd $ maximum $ [(length (triplets p), p) | p <- [1..1000]]
-- 840
-- TODO: Use more efficient formula to generate triplets. Research needed.
