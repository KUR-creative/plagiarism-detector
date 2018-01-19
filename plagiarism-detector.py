import preprocessor
fs4 = preprocessor.get_asm_code('./long/f4.cpp')
fs3 = preprocessor.get_asm_code('./long/f3.cpp')
fs2 = preprocessor.get_asm_code('./long/f2.cpp')
fgeeks = preprocessor.get_asm_code('./long/geeks.cpp')
fs1_4 = preprocessor.get_asm_code('./long/1-4.cpp')
fs1_3 = preprocessor.get_asm_code('./long/1-3.cpp')
fs1_2 = preprocessor.get_asm_code('./long/1-2.cpp')
fs1_1 = preprocessor.get_asm_code('./long/1-1.cpp')
s2 = preprocessor.get_asm_code('./long/f2.cpp')
s1 = preprocessor.get_asm_code('./long/f4.cpp')

import comparator, sequencer
strs = [
        (fs1_1,'fs1_1'),
        (fs1_2,'fs1_2'),
        (fs1_3,'fs1_3'),
        (fs1_4,'fs1_4'),
        #(fs2,'fs2'),
        #(fs3,'fs3'),
        #(fs4,'fs4'),
        (fgeeks,'fgeeks'),
        ]

import itertools
scores = []
for pair in itertools.combinations(strs,2):
    (a,b) = pair
    seq1 = sequencer.make_sequence_from(a)
    seq2 = sequencer.make_sequence_from(b)

    score = comparator.match_score(seq1,seq2)
    scores.append( (a,b,score) )
    base_len = min(len(seq1),len(seq2))
    print(a[1] + ' vs ' + b[1] + ' match score is\t\t\t' + str(score))
    print(a[1] + ' vs ' + b[1] + ' /min_len similarity is\t\t' + str(float(score)/float(base_len)))
    print(a[1] + ' vs ' + b[1] + ' /a+b_len * 2 similarity is\t' + str(2 * float(score)/float(len(seq1)+len(seq2))))
    print('------')

for tup in scores:
    (a,b,score) = tup
    name_a = a[1]
    name_b = b[1]
    
    print( str(score) + ': ' + name_a + ' vs ' + name_b )

