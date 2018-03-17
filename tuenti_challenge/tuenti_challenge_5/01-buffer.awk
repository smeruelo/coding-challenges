#!/usr/bin/awk -f

function ceiling(x) {
   return (x == int(x)) ? x : int(x)+1
}

{
   if (NR > 1)
      print ceiling($1/2)
}
