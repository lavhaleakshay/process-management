#!/bin/bash

if [ -f lock ];
then
       sleep 10 && exit 1
fi;
