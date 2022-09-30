#!/bin/bash

echo "masukkan angka"
read input

until [ ! $input -gt 0 ]
do
 echo $input
 input=$((input-2))
done
