<?php

require_once "../app/init.php";

if( !session_id() ) Session::init();

$app = new App;