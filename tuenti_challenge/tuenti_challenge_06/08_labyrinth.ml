#!/usr/bin/ocaml unix.cma

let ip = "52.49.91.111";;
let port = 1986;;
let view_size = 7;;
let view_offset = view_size / 2;;
let maze_size = 140;;
let maze = Array.make_matrix maze_size maze_size '*';;
let view = Array.make_matrix view_size view_size '+';;

(* debug *)
let print_array array =
  let print_vector vector =
    Array.iter print_char vector;
    print_newline () in
  Array.iter print_vector array;
  print_newline ()

let read_view ch_in =
  let rec in_to_list_of_lines i =
    if i = view_size
    then []
    else (input_line ch_in) :: in_to_list_of_lines (i + 1) in
  let lines = in_to_list_of_lines 0 in
  let line_to_array i line =
    let f j char = view.(view_size - i - 1).(j) <- char in
    String.iteri f line in
  List.iteri line_to_array lines (* ; print_array view *)

let update_maze x y =
  let f row vector =
    let ff col cell =
      if maze.(y - view_offset + row).(x - view_offset + col) != '.'
      then maze.(y - view_offset + row).(x - view_offset + col) <- cell in
    Array.iteri ff vector in
  Array.iteri f view;
  maze.(y).(x) <- '.'

let rec get_maze ch_in ch_out x y mov =
  read_view ch_in;
  update_maze x y;
  (* print_array maze; print_newline (); print_newline (); *)
  let backward = function
      'u' -> 'd'
    | 'd' -> 'u'
    | 'l' -> 'r'
    | 'r' -> 'l'
    | _ -> 'x' in
  let moves = List.filter (fun (m, x, y) -> m != backward mov)
			  [('d', x, y + 1); ('r', x + 1, y); ('u', x, y - 1); ('l', x - 1, y)] in
  let valid_moves = List.filter (fun (m, x, y) -> maze.(y).(x) = ' ') moves in
  (* List.iter (fun (m, x, y) -> output_char stdout m; print_int x; print_string ", "; print_int y; print_string "\n") valid_moves; *)
  List.iter (fun (m, x, y) -> output_char ch_out m;
			      output_char ch_out '\n';
			      flush ch_out;
			      get_maze ch_in ch_out x y m;
			      output_char ch_out (backward m);
			      output_char ch_out '\n';
			      flush ch_out;
			      read_view ch_in)
	    valid_moves

let () =
  let (ch_in, ch_out) = Unix.open_connection (Unix.ADDR_INET (Unix.inet_addr_of_string ip, port)) in
  get_maze ch_in ch_out (maze_size / 2) (maze_size / 2) 'x';
  print_array maze
