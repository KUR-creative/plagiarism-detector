MATCH_REWARD = 1

def dp_variables(a, b):
    if type(a) != type(b):
        raise TypeError("arg1 and arg2 type must be same!")
    len_a = len(a)
    len_b = len(b)
    return (len_a, len_b,
            [[0 for x in range(len_b+1)] for y in range(len_a+1)])
    # $bbbb
    #$00000
    #a00000
    #a00000

def match_score(a,b):
    (len_a, len_b, memo) = dp_variables(a,b)

    for y in range(len_a+1):
        for x in range(len_b+1):
            if x == 0 or y == 0:
                memo[y][x] = 0
            else:
                score = 0
                if a[y-1] == b[x-1]:
                    score = MATCH_REWARD

                case1 = memo[y-1][x-1] + score
                case2 = memo[y  ][x-1]
                case3 = memo[y-1][x  ]

                best_score = max(case1,case2,case3)
                memo[y][x] = best_score

    return memo[len_a][len_b]

import unittest
class match_scoreTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(match_score('',''),  0)
        self.assertEqual(match_score('','a'), 0)
        self.assertEqual(match_score('b',''), 0)

        self.assertEqual(match_score([],[]),    0)
        self.assertEqual(match_score([],[1]),   0)
        self.assertEqual(match_score(['2'],[]), 0)

        self.assertRaises(TypeError, lambda:match_score([],''))

    def test_1vs1_cases(self):
        self.assertEqual(match_score('a','a'), MATCH_REWARD)
        self.assertEqual(match_score('a','b'), 0)

        self.assertEqual(match_score([1],[1]), MATCH_REWARD)
        self.assertEqual(match_score([1],[2]), 0)
    
    def test_common_cases(self): 
        self.assertEqual(match_score('abc','bca'),  2*MATCH_REWARD)
        self.assertEqual(match_score('xby','xab6y'),3*MATCH_REWARD)

        self.assertEqual(match_score([-1,-2,0,7,8,2],
                                     [0,7,8,-1,-2]),3*MATCH_REWARD)



class helper_functionsTest(unittest.TestCase):
    def test_dpvariables(self):
        (len_a, len_b, table) = dp_variables([1],[2])
        self.assertEqual(len(table),2)    # number of rows
        self.assertEqual(len(table[0]),2) # number of columns
        self.assertEqual(len_a, 1)
        self.assertEqual(len_b, 1)

        (len_a, len_b, table) = dp_variables('','a')
        self.assertEqual(len(table),1)    # number of rows    
        self.assertEqual(len(table[0]),2) # number of columns 
        self.assertEqual(len_a, 0)
        self.assertEqual(len_b, 1)


if __name__ == '__main__':
    unittest.main()
