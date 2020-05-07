#!/usr/bin/python3

import os
import sys

if __name__ == '__main__':
	with open('connect.sh', 'w') as f:
		f.write('ssh -R 52698:localhost:52698 {}'.format(sys.argv[1]))
		os.system('chmod 777 connect.sh')
