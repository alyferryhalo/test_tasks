<?php
$year=$_POST['year'];

if (($year%4 == 0 and $year%100 != 0) or ($year%400 == 0))
{
   echo "ДА";
}

else
{
   echo "НЕТ";
}
?>
