LEX = 0
ASM = 1

#### set sequence kind. ####
seq_kind = LEX

#### set test directory ####
test_dir = './candle/'
#test_dir = './eleccar/'
#test_dir = './food/'
#test_dir = './long/'

print('preprocessing...')
import os
import preprocessor, comparator, sequencer
srcnames = os.listdir(test_dir)

if seq_kind == ASM:
    asm_name_pairs = map(lambda srcname: 
                            (preprocessor.get_asm_code(test_dir + srcname),
                             srcname), 
                         srcnames[:])
elif seq_kind == LEX:
    seq_name_pairs = map(lambda srcname: 
                            (sequencer.get_sequence_from(test_dir + srcname),
                             srcname), 
                         srcnames[:])

print('computing match scores of all pairs...')
import itertools 
scores = []
if seq_kind == ASM:
    for pair in itertools.combinations(asm_name_pairs,2):
        (a,b) = pair
        seq1 = sequencer.make_sequence_from(a)
        seq2 = sequencer.make_sequence_from(b)

        score = comparator.match_score_local(seq1,seq2)
        scores.append( (score,a,b) )
elif seq_kind == LEX:
    for pair in itertools.combinations(seq_name_pairs,2):
        (a,b) = pair
        (seq1,seq2) = (a[0],b[0])

        score = comparator.match_score_local(seq1,seq2)
        scores.append( (score,a,b) )

scores.sort()
for tup in scores:
    (score,a,b) = tup
    name_a = a[1]
    name_b = b[1]
    
    print( str(score) + ': ' + name_a + ' vs ' + name_b )

print('plotting result.')
import matplotlib.pyplot as plt
#data = [100,200,300,400, 1000,1400,1500,1700]
plt.hist(map(lambda tup: tup[0], scores), bins = 10, width=10.0)
#plt.plot(, map(lambda tup: tup[2], scores), 'ro')
plt.show()

