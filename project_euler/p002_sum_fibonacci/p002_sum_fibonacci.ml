(* https://projecteuler.net/problem=2 *)

let fibonacci n =
  let rec aux fib last1 last2 =
    let current = last1 + last2 in
    if current > n then fib
    else aux (current::fib) current last1
  in aux [1; 1] 1 1

let sum_even list =
  let is_even n =
    n mod 2 = 0
  in List.fold_left (+) 0 (List.filter is_even list)

let () =
  sum_even (fibonacci 4000000) |> print_int;
  print_newline ();
