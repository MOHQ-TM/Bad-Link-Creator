<?php
session_start();
date_default_timezone_set("Asia/Tehran");
function Ip()
{
    if (!empty($_SERVER['HTTP_CLIENT_IP']))
        //check ip from share internet
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
        //to check ip is pass from proxy
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else
        $ip = $_SERVER['REMOTE_ADDR'];
    $f=fopen("ip.txt","a+");
    fwrite($f,$ip."\n");
    fclose($f);
}

$_SESSION["IP"]=Ip();
echo $_SESSION['IP'];
?>
