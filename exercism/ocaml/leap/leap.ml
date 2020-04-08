(* https://exercism.io/my/solutions/ba211fe0f25a4d48b07489aef1668474 *)

let leap_year year =
  let multiple n =
    year mod n == 0 in
  multiple 4 && (not (multiple 100) || (multiple 400))
