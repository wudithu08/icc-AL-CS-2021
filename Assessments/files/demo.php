<?php
$input1=$_POST['Input1'];
$input2=$_POST['Input2'];
if ($input1==$input2){
	echo "<script>alert('Same');history.back(-1);</script>";
}else{
	echo "<script>alert('Different');history.back(-1);</script>";
}
?>