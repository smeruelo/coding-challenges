(* https://projecteuler.net/problem=1 *)

let is_multiple i j =
  i != 0 && i mod j = 0

let sum n =
  let rec aux i acc =
    if i < n then
      if is_multiple i 3 || is_multiple i 5 then
        aux (i + 1) (acc + i)
      else
        aux (i + 1) acc
    else
      acc
  in aux 3 0

let () =
  print_int (sum 1000);
  print_newline ()
