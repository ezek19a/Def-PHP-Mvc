<?php

class Session {

	
	public static function init() {

		@session_start();

	}
	
	public static function set($key, $value) {

		$_SESSION[$key] = $value;

	}
	
	public static function get($key) {

		if (isset($_SESSION[$key]))
		return $_SESSION[$key];

	}
	
	public static function destroy() {

		//unset($_SESSION);
		session_destroy();

	}

	public static function delete($key)	{

		unset($_SESSION[$key]);

	}


	public static function setFlash($message, $action, $type) {

		$_SESSION['flash'] = [

			'message' => $message,
			'action' => $action,
			'type' => $type

		];

	}


	public static function flash(){

		if(isset($_SESSION['flash'])){

			echo '<div class="alert alert-' . $_SESSION['flash']['type'] . ' alert-dismissible fade show" role="alert">
					  <strong> ' . $_SESSION['flash']['message'] . ' </strong>' . $_SESSION['flash']['action'] . '
					  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
					    <span aria-hidden="true">&times;</span>
					  </button>
					</div>';


			unset($_SESSION['flash']);

		}

	}
	
}