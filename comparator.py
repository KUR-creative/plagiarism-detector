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

def match_score_gene(a,b):
    ''' a,b must be same sequence type. '''
    (len_a, len_b, memo) = dp_variables(a,b)

    for y in range(len_a+1):
        for x in range(len_b+1):
            if x == 0 or y == 0:
                memo[y][x] = 0
            else:
                score = 0
                if a[y-1] == b[x-1]:
                    score = MATCH_REWARD

                from_ul = memo[y-1][x-1] + score
                from_l = memo[y  ][x-1]
                from_u = memo[y-1][x  ]

                best_score = max(from_ul,from_l,from_u)
                memo[y][x] = best_score

    #for row in memo:
        #print(row)
    return memo[len_a][len_b]

import itertools
def match_score_local(a,b):
    ''' a,b must be same sequence type. '''
    (len_a, len_b, memo) = dp_variables(a,b)

    for y in range(len_a+1):
        for x in range(len_b+1):
            if x == 0 or y == 0:
                memo[y][x] = 0
            else:
                if a[y-1] == b[x-1]:
                    score = 3
                else:
                    score = -3

                from_ul= memo[y-1][x-1] + score
                from_l = memo[y  ][x-1] - 2 #gap penalty 
                from_u = memo[y-1][x  ] - 2 #gap penalty

                best_score = max(from_ul,from_l,from_u,0)
                memo[y][x] = best_score
    #for row in memo:
        #print(row)
    return max(list(itertools.chain(*memo)))


import unittest
class match_score_geneTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(match_score_gene('',''),  0)
        self.assertEqual(match_score_gene('','a'), 0)
        self.assertEqual(match_score_gene('b',''), 0)

        self.assertEqual(match_score_gene([],[]),    0)
        self.assertEqual(match_score_gene([],[1]),   0)
        self.assertEqual(match_score_gene(['2'],[]), 0)

        self.assertRaises(TypeError, lambda:match_score_gene([],''))

    def test_1vs1_cases(self):
        self.assertEqual(match_score_gene('a','a'), MATCH_REWARD)
        self.assertEqual(match_score_gene('a','b'), 0)

        self.assertEqual(match_score_gene([1],[1]), MATCH_REWARD)
        self.assertEqual(match_score_gene([1],[2]), 0)
    
    def test_common_cases(self): 
        self.assertEqual(match_score_gene('abc','bca'),  2*MATCH_REWARD)
        self.assertEqual(match_score_gene('xby','xab6y'),3*MATCH_REWARD)

        self.assertEqual(match_score_gene([-1,-2,0,7,8,2],
                                          [0,7,8,-1,-2]),3*MATCH_REWARD)

class match_score_localTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(match_score_local('',''),  0)
        self.assertEqual(match_score_local('','a'), 0)
        self.assertEqual(match_score_local('b',''), 0)

        self.assertEqual(match_score_local([],[]),    0)
        self.assertEqual(match_score_local([],[1]),   0)
        self.assertEqual(match_score_local(['2'],[]), 0)

        self.assertRaises(TypeError, lambda:match_score_local([],''))

    def test_1vs1_cases(self):
        self.assertEqual(match_score_local('a','a'), 3)
        self.assertEqual(match_score_local('a','b'), 0)

        self.assertEqual(match_score_local([1],[1]), 3)
        self.assertEqual(match_score_local([1],[2]), 0)

    def test_common_cases(self): 
        self.assertEqual(match_score_local('tg','g'),3)

    def test_use_gap_penalty(self):
        pass # can't test..
        #self.assertEqual(match_score_local('tgt','g'),3)
        #self.assertEqual(match_score_local('tg','ggt'),1)

    def test_scoring_scheme(self):
        # matched case: add score.
        self.assertEqual(match_score_local('tgt',
                                           'ggt'),6)
        # mismatched case: sub score: can't test..
        self.assertEqual(match_score_local('tgtta',
                                           'ggttg'),9)


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
