import preprocessor

def is_instruction(string):
    return (len(string) != 0 and string[0] != '.')

def asmline2inst(asmline):
    ''' 
    1 line of asm code 
    -> instruction
       (or callee function name: in case of 'call')
    '''
    splited_arr = asmline.split('\t')
    if splited_arr[0] == 'call':
        return splited_arr[1]
    return splited_arr[0]

def proc_dict(inst_list):
    proc_dict = {}
    now_proc = None
    for s in inst_list:
        if s[-1] == ':':
            proc_name = s[:-1] # remove trailing ':'
            now_proc = proc_name
            proc_dict[proc_name] = [] 
        else:
            #inst_seq = proc_dict[now_proc]
            #inst_seq.append(s)
            proc_dict[now_proc].append(s)
    return proc_dict


def sequence(procdict):
    ''' 
    Procdict's type is { str:[str,str,str...] }
    Use proc_dict function to get procdict.
    Return value is list of instruction.
    '''
    if procdict.get('main') == None:
        return []
    def _sequence(procdict, ret_seq, history_stack, now_proc):
        ''' side effect!: param seq changed. '''
        history_stack.append(now_proc)
        now_proc_seq = procdict[now_proc]
        for instruction in now_proc_seq:
            if (procdict.get(instruction) and 
                instruction not in history_stack):
                _sequence(procdict, ret_seq, history_stack, instruction)
            else:
                ret_seq.append(instruction)
        history_stack.pop()
        return ret_seq
    return _sequence(procdict,[],[],"main")

import subprocess
def make_sequence_from(asm_code_str):
    return sequence(
             proc_dict(
               map(asmline2inst,
                   filter(is_instruction, 
                          map(lambda s:s.lstrip(), 
                              asm_code_str[0].split('\n'))))))

def get_sequence_from(filename):
    print('get sequence from ' + filename + '...')
    ps = subprocess.Popen(('./lex_pro', filename), stdout=subprocess.PIPE)
    string = subprocess.check_output(('./rerepro'), stdin=ps.stdout)
    ps.wait()
    return string


import unittest
class sequenceTest(unittest.TestCase):
    def test_get_sequence_from(self):
        print(get_sequence_from('./long/1-1.cpp'))
        print(get_sequence_from('./long/1-2.cpp'))
        print(get_sequence_from('./long/1-3.cpp'))

    def test_no_proc_call(self):
        proc_dict = {'main':['1','2','3','4'],
                     'p'   :['10','20','30']}
        expected = ['1','2','3','4']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_no_recur(self):
        proc_dict = {'main':['1','2','3','4','p'],
                     'p'   :['10','20','30']}
        expected = ['1','2','3','4','10','20','30']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_call_more(self):
        proc_dict = {'main':['1','2','p1','4','p2'],
                     'p1'  :['10','20','30'],
                     'p2'  :['a','b','c']}
        expected = ['1','2','10','20','30','4',
                    'a','b','c']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_call_more_depth(self):
        proc_dict = {'main':['a','b','c','d'],
                     'a'   :['1','2','3'],
                     'b'   :['4','5'],
                     'c'   :['6']}
        expected = ['1','2','3','4','5','6','d']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_remove_recur(self):
        proc_dict = {'main':['1','main']}
        expected = ['1','main']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    #@unittest.skip("not now")
    def test_remove_mutual_recur(self):
        proc_dict = {'main':['a'],
                     'a'   :['1','b'],
                     'b'   :['2','a']}
        expected = ['1','2','a'] # sort of... dfs.
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_remove_mutual_recur2(self):
        proc_dict = {'main':['a','b','a'],
                     'a'   :['1','2','a','a','3'],
                     'b'   :['7','8','a','b']}
        expected = ['1','2','a','a','3',
                    '7','8','1','2','a','a','3','b',
                    '1','2','a','a','3'] 
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_if_compile_failed(self):
        proc_dict = {}
        expected = [] 
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
    '''
    print '---------'
    result = sequence(proc_dict)
    print result
    print '\n'.join(result)
    '''

#import re
#is_proc_decl = re.compile('.*:')

#pattern = re.compile('.*:')
#result = pattern.findall(string)
#print(result)
