import preprocessor
fs4 = preprocessor.get_asm('./long/f4.cpp')
fs3 = preprocessor.get_asm('./long/f3.cpp')
fs2 = preprocessor.get_asm('./long/f2.cpp')
fgeeks = preprocessor.get_asm('./long/geeks.cpp')
fs1_4 = preprocessor.get_asm('./long/1-4.cpp')
fs1_3 = preprocessor.get_asm('./long/1-3.cpp')
fs1_2 = preprocessor.get_asm('./long/1-2.cpp')
fs1_1 = preprocessor.get_asm('./long/1-1.cpp')
s2 = preprocessor.get_asm('./long/f2.cpp')
s1 = preprocessor.get_asm('./long/f4.cpp')
##################
#string = preprocessor.get_asm('./tests/fact.cpp')
###############
#str2 = preprocessor.get_asm('./tests/origin.cpp')

import comparator
strs = [
        (fs1_1,'fs1_1'),
        (fs1_2,'fs1_2'),
        (fs1_3,'fs1_3'),
        (fs1_4,'fs1_4'),
        (fs2,'fs2'),
        (fs3,'fs3'),
        (fs4,'fs4'),
        (fgeeks,'fgeeks'),
        ]

from sequencer import * 

for a in strs:
    for b in strs:
        seq1 = sequence(
                    proc_dict(
                      map(inst2str,
                          filter(is_not_inst, 
                                 map(lambda s:s.lstrip(), 
                                     a[0].split('\n'))))))
        seq2 = sequence(
                    proc_dict(
                      map(inst2str,
                          filter(is_not_inst, 
                                 map(lambda s:s.lstrip(), 
                                     b[0].split('\n'))))))
        score = comparator.match_score(seq1,seq2)
        base_len = min(len(seq1),len(seq2))
        print(a[1] + ' vs ' + b[1] + ' match score is\t\t\t' + str(score))
        print(a[1] + ' vs ' + b[1] + ' /min_len similarity is\t\t' + str(float(score)/float(base_len)))
        print(a[1] + ' vs ' + b[1] + ' /a+b_len * 2 similarity is\t' + str(2 * float(score)/float(len(seq1)+len(seq2))))
        print('------')