<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FatCats</title>
</head>
<body>
<h2>InputValidation</h2>
    <hr />

<form action = 'demo.php' method='post'>
<center>
Input1:<br>
<!-- input for input1  -->
<label for="Input1" class="label"></label><input name="Input1" type="text"/><br>
Input2:<br>
<!-- input for input2  -->
<label for="Input2" class="label"></label><input name="Input2" type='text'/>
<br>
<br>
</div>
<p>
<!-- button to click for submitting -->
<button type="submit" name='submit'>Check</button>
</center>
</form>
</body>
</html>

<?php
if (isset($_POST['submit'])){
$input1=$_POST['Input1'];
$input2=$_POST['Input2'];
if ($input1==$input2){
	echo "<script>alert('Same');history.back(-1);</script>";
}else{
	echo "<script>alert('Different');history.back(-1);</script>";
}
}
?>