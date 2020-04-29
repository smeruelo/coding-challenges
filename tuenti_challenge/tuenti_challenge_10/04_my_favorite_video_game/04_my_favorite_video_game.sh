#!/usr/bin/bash

IP_PREPROD=`dig steam-origin.contest.tuenti.net +short`
echo "$IP_PREPROD  pre.steam-origin.contest.tuenti.net" >> /etc/hosts
curl pre.steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key
