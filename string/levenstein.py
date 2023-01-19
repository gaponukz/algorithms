import unittest

def levenstein(string1, string2):
    n = range(0, len(string1) + 1)

    for y in range(1, len(string2) + 1):
        l, n = n, [y]
        
        for x in range(1, len(string1) + 1):
            n.append(min(l[x] + 1, n[-1] + 1, l[x - 1] + ((string2[y - 1] != string1[x - 1]) and 1 or 0)))
    
    return n[-1]


class TestLevenstein(unittest.TestCase):
    def test_all_what_can(self):
        self.assertEqual(levenstein("data", "data"), 0)
        self.assertEqual(levenstein("data", "dara"), 1)
        self.assertEqual(levenstein("data", "dataa"), 1)
        self.assertEqual(levenstein("data", "ata"), 1)
        self.assertEqual(levenstein("data", ""), 4)

if __name__ == '__main__':
    unittest.main()
