#!/usr/bin/env bash
mkdir -p /home/user/etc/stainerCharles/
cp -r /home/user/catkin_ws/src/final/ /home/user/etc/stainerCharles/
export PATH="$PATH:$/home/user/etc/stainerCharles/final/"
echo "Install complete."