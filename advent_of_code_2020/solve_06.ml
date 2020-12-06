#load "str.cma";;

open Printf;;
module SS = Set.Make(Char) ;;

let (%) f g x = f (g x)

let split (substr : string) (s : string) : string list = Str.split (Str.regexp substr) s

let sum (s : int list) : int = List.fold_right (fun a b -> a + b) s 0
let set_union (s : SS.t list) : SS.t = List.fold_right SS.union s SS.empty
let set_inter (s : SS.t list) : SS.t = List.fold_right SS.inter s (List.hd s)

let list2set (s : char list) : SS.t = List.fold_right SS.add s SS.empty
let str2list (s : string) : char list = List.init (String.length s) (String.get s)

let () =
  let ic = open_in "input_06" in
  let contents : string = really_input_string ic (in_channel_length ic) in

  let groups : string list = split "\n\n" contents in
  let groups : string list list = List.map (split "\n") groups in
  let groups : SS.t list list = List.map (List.map (list2set % str2list )) groups in

  let q1 : SS.t list = List.map set_union groups in
  let q1 : int = sum (List.map SS.cardinal q1) in

  let q2 : SS.t list = List.map set_inter groups in
  let q2 : int = sum (List.map SS.cardinal q2) in

  printf "%d\n%d\n" q1 q2
