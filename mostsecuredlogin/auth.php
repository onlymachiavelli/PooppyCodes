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

function Auth($user, $pass){
    global $conn;
    $action = "SELECT * FROM users";
        $res = mysqli_query($conn, $action);
        while ($row = $res -> fetch_assoc()){
            if($row['email'] == $user && $row['password'] == $pass) {
                return TRUE;
            }
        }
        return FALSE;
}


$ver = FALSE;
if($conn){
    $sql = "SELECT * from users";
    if(Auth($_POST["username"], $_POST["password"]) ) {
        print("COOL URE IN");
    }
    else {
        
        $res = mysqli_query($conn, $sql);
        while($row = $res -> fetch_assoc()){
            if($row["password"] == $_POST["password"] && $row["email"] != $_POST["username"]){
                print("Error login but this password's belongs to " . $row["email"]) ;
                $ver = TRUE;
                break;
            }
        }

        if (!$ver) print("Error Logining in");
    }
   
    
}


else die("fcking db error");

?>