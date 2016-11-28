import os
import sys
from translate_json_to_yml import remove_non_ascii


_file_loc = './yml_files/'

_test_file = 'test.yml'
_all_file = 'all_take_2.yml'

def get_n_recipes(n, start = 0, test_file = _test_file):
    start = int(start)
    n = int(n) + start
    counter = 0
    with open(os.path.join(_file_loc, _all_file)) as allfi:
    	with open(os.path.join(_file_loc, test_file), 'w') as testfi:
            for line in allfi:
		#line = line.replace('<span class="fn">','').replace('</span>','')
		#line = line.replace('<span class ="fn">','').replace('<span class = "fn">','').replace('<span class= "fn">','')
	    	if line[:6] == '- name':
	            counter += 1
		    if counter > n:
		        break
	        if counter > start:
		    print [line]
		#    line = remove_non_ascii(line)
		#    line = line[:-1].replace('\n','')
		    testfi.write(line)
		#    testfi.write('\n')

if __name__ == '__main__':
    get_n_recipes(sys.argv[1], sys.argv[2], sys.argv[3])
    
