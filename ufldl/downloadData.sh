#########################################################################
# File Name: downloadData.sh
# Author: xq
# mail: roachsinai@gmail.com
# Created Time: 2016年06月09日 星期四 20时50分27秒
#########################################################################
#!/bin/bash

wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
gunzip train-labels-idx1-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
gunzip train-images-idx3-ubyte.gz
wget http://ufldl.stanford.edu/wiki/resources/stl10_patches_100k.zip
unzip stl10_patches_100k.zip
wget http://ufldl.stanford.edu/wiki/resources/stlSubset.zip
unzip stlSubset.zip
