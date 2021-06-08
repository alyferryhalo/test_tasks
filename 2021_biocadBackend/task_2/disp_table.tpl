%# disp_table.tpl
<table border="1">
<tr><th>title</th><th>data</th></tr>
%for d in data:
<td>{{data[d]}}</td></tr>
%end
</table>
