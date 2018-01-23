#test_dir = './candle/'
#test_dir = './eleccar/'
test_dir = './food/'

print('preprocessing...')
import os
import preprocessor, comparator, sequencer
srcnames = os.listdir(test_dir)
asm_name_pairs = map(lambda srcname: 
                        (preprocessor.get_asm_code(test_dir + srcname),
                         srcname), 
                     srcnames[:])
#print(len(asm_name_pairs))
#print(map(lambda x:x[1], asm_name_pairs))

print('computing match scores of all pairs...')
import itertools 
scores = []
for pair in itertools.combinations(asm_name_pairs,2):
    (a,b) = pair
    seq1 = sequencer.make_sequence_from(a)
    seq2 = sequencer.make_sequence_from(b)

    score = comparator.match_score_local(seq1,seq2)
    scores.append( (score,a,b) )
    #base_len = min(len(seq1),len(seq2))
    #print(a[1] + ' vs ' + b[1] + ' match score is\t\t\t' + str(score))
    #print(a[1] + ' vs ' + b[1] + ' /min_len similarity is\t\t' + str(float(score)/float(base_len)))
    #print(a[1] + ' vs ' + b[1] + ' /a+b_len * 2 similarity is\t' + str(2 * float(score)/float(len(seq1)+len(seq2))))
    #print('------')

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

