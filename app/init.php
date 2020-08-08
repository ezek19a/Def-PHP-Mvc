<?php

/*
require_once "core/App.php";
require_once "core/Controller.php";
require_once "core/Database.php";
require_once "core/Session.php";
require_once "core/Cookie.php";
require_once "core/Openssl.php";
*/

require_once "config.php";

// Also spl_autoload_register (Take a look at it if you like)

//function __autoload($class)

spl_autoload_register(function($class) {

	require_once "core/" . $class .".php";

});