<?php

$pref=$_POST['pref']; // Префикс: <input type="text" name="pref"/>
$str_mass=$_POST['str_mass']; // Строки: <input type="text" name="str_mass"/>
$arr_answ = array(); // пустой массив, чтобы положить туда всякое

foreach ($str_mass as $value) { // для каждого элемента в массиве str_mass
  if (str_starts_with($value, $pref)) { // если элемент начинается с pref
    array_push($arr_answ, $value); // то положить в массив arr_answ
  }
}

?>
