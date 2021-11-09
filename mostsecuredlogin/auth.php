<?php


$hostname ="localhost";
$username = "root";
$password = "";

$conn = new mysqli(
    $hostname,
    $username,
    $password,
    "bored"
);

if($conn){
    print("cv");
   
    
}


else die("fcking db error");

?>