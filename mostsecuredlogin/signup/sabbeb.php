<?php 
    $hostname = "localhost";
    $username = "root";
    $password = "";





    $connection = new mysqli(
        $hostname, 
        $username,
        $password,
        "bored"
    );




    function findTarget($target){
        global $connection;
        $action = "SELECT * FROM users";
        $res = mysqli_query($connection, $action);
        while ($row = $res -> fetch_assoc()){
            if($row['email'] == $target) {
                return TRUE;
            }
        }
        return FALSE;
    }
    if($connection) {
        $sql = "INSERT INTO users (name, email, password) VALUES ('".$_POST["name"]."', '".$_POST["email"]."' ,'".$_POST["pass"]."')" ;
        if(findTarget($_POST["email"])){
            print("this email is token");
        }
        else{
            if($connection -> query($sql)){
                print("c bon tsabbou");
            }
            else{
                die (mysqli_error($connection));
            }
        }

    }
    else {
        die ("error db");
    }
?>