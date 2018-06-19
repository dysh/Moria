#!/bin/bash

echo testing MLYA
for i in {1..50};
do 
{
echo $i 'мля!'
./mlya
phyml -i sample.phy -m JC69 --quiet 
phyml -i samplAA.phy -m JC69 --quiet
./dst.py $i
}
echo Done!
done
