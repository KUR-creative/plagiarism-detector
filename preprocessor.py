# it may run process in creating subprocess object...
import subprocess

# this function is so slow.
# need to optimize performance.
# use command(only in python 2) or something..
# or use multiprocessing.
def get_asm_code(srcname):
    ''' 
    Srcname must be name of existing c/c++ source file.
    If not, it'll raise error.
    Srcname example: 'prog_name.cpp' 
    '''
    proc = subprocess.Popen(['g++',
                             '-S','-O2','-std=c++11',
                             '-o-', srcname],
                            stdout=subprocess.PIPE)
    (asm,_) = proc.communicate();
    return asm

import unittest, os
class preprocessorTest(unittest.TestCase):
    def setUp(self):
        self.srcname = 'fact.cpp'
        self.src = ''' 
            #include <iostream>
            using namespace std; 

            long long fact(long long n){
                return 
                    ((n == 1) ?
                     1
                     :
                     fact(n-1) * n);
            }

            long long fib(long long n){
                return
                    ((n <= 1) ?
                     n
                     :
                     fib(n-1) + fib(n-2));
            }

            int main(void){
                cout << fact(4) << endl;
                cout << fib(17) << endl; // 1597
                return 0;
            }'''
        self.cmd = ('g++ -S -O2 -std=c++11' 
                    + self.srcname)
        with open(self.srcname, "w") as f:
            f.write(self.src)

    def tearDown(self):
        os.remove(self.srcname)

    def test_get_asm(self):
        with open(self.srcname, "r") as f:
            data = f.read()
        print(self.srcname)
        asm_code = get_asm_code(self.srcname)
        print(asm_code)

if __name__ == '__main__':
    #string = subprocess.check_output(['ls', '|', 'sort','-r'], shell=True)
    #print(string)
    #ps = subprocess.Popen(('./m1', 'Makefile'), stdout=subprocess.PIPE)
    #string = subprocess.check_output(('./m2'), stdin=ps.stdout)
    #ps.wait()
    #print(string)
    unittest.main()
