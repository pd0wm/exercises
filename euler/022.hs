{-
Problem 22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
-}

import Data.List.Split
import Data.List
import Data.Char
import Text.Regex

readNames :: String -> [String]
readNames s = sort $ map (init.tail) $ splitOn "," s


alphValue :: String -> Int
alphValue s = sum $ map ((+(-64)).ord) s

main = do
	contents <- readFile "022.txt"
	let sortedNames = readNames contents
	putStrLn $ show $ sum $ map (\x -> fst x * snd x) $ zip (map alphValue sortedNames) [1..]

-- 871198282