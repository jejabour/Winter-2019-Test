# import numpy as np
# import pandas as pd
# import random
# import matplotlib.pyplot as plt
# from random import randint

# rows = 80
# cols = 10

# df = pd.DataFrame(np.random.randn(rows, cols))
# df.to_csv("test.csv", index=False)


# plt.plot("test.csv")
# plt.show()


import urllib.request
import os
from os import path

if not os.path.exists('/Users/RDITLJEJ/Downloads/testfiles/'):
    os.mkdir('/Users/RDITLJEJ/Downloads/testfiles/')

# dependencies = open("/Users/RDITLJEJ/Downloads/dependencies.txt", "r")

with open ("/Users/RDITLJEJ/Desktop/es-workflows-master/dependencies.txt", "r") as dependencies:
    # data=dependencies.read()
    # print (data)


    for line in dependencies:
        tmp = dependencies.readline()
        if tmp[:1] == "#":
            print ("...")
        else:
            if tmp[:1] == "c":
                # print("Conda" + " " + tmp)
                tmpfirst = tmp[13:]
                tmpfirst = tmpfirst[:tmpfirst.find('=')]
                tmp2 = tmp[tmp.find('='):]
                url = 'https://conda.anaconda.org/conda-forge/linux-64/' + tmpfirst + '-' + tmp2[1:] + '-py36_0.tar.bz2'
                print (url)
                # urllib.request.urlretrieve(url, '/Users/RDITLJEJ/Downloads/testfiles/' + tmp[13:])
    

# https://conda.anaconda.org/conda-forge/linux-64/fiona-1.7.12-py36_0.tar.bz2

# url = 'https://conda.anaconda.org/conda-forge/linux-64/fiona-1.7.12-py36_0.tar.bz2'
# urllib.request.urlretrieve(url, '/Users/RDITLJEJ/Downloads/testfiles/fiona-1.7.12-py36_0.tar.bz2')

    # lines = []
    # for line in dependencies:
    #     lines.append(line)
    
#     print()

#     print ("This is lines", lines)

#     print()

# print("This is lines afterwards", lines)

# print()


# f = open("/Users/RDITLJEJ/Desktop/es-workflows-master/dependencies.txt", "r")
# lines2 = []
# for line in f:
#     lines2.append(line).replace("\n", "")
# f.close

# print("This is lines 2", lines2)
# print('Beginning file download')

# url = 'https://conda.anaconda.org/conda-forge/linux-64/fiona-1.7.12-py36_0.tar.bz2'
# urllib.request.urlretrieve(url, '/Users/RDITLJEJ/Downloads/testfiles/fiona-1.7.12-py36_0.tar.bz2')

