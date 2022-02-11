#!/bin/bash
STATE=$1
systemctl status $STATE &> /dev/null
echo $?