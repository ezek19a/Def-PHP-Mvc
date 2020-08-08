<?php

//$path = $_SERVER['SERVER_NAME'];

//echo "Path: " . $path;

$actual_link = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http") . "://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";

$full = explode('/', $actual_link);
$pop = array_pop($full);
$fullnlastfolder = implode('/', $full);
$secondfull = explode('/', $fullnlastfolder);
$secondpop = array_pop($secondfull);
$secondlast = implode('/', $secondfull);
$realpath = $fullnlastfolder;
$secondpath = $secondlast;

$app = "app"; // app
$public = "/public/";

define('APP', $app);
define('BASEURL', $secondpath . $public);
define('ACTVURL', 'create/email_activation/');
define('TIMEZONE', date_default_timezone_set("Asia/Kuala_Lumpur"));

// DB
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', ''); //defmvc

//echo "BASEURL: " . BASEURL;