(* https://projecteuler.net/problem=3 *)

let is_prime n =
  let rec aux i =
    if i = 1 then true
    else if n mod i = 0 then false
    else aux (i - 1)
  in aux (int_of_float (sqrt (float_of_int n)))

let highest_factor n =
  let rec aux i =
    if i = 1 then n
    else if n mod i = 0 && is_prime i then i
    else aux (i - 1)
  in aux (int_of_float (sqrt (float_of_int n)))

let () =
  highest_factor 600851475143 |> print_int;
  print_newline ()
