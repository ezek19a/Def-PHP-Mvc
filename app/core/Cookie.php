<?php

	class Cookie {


		public static function set($name, $value, $time) {

			setcookie($name, $value, $time);

		}


		public static function get($name) {

		if (isset($_COOKIE[$name]))
		return $_COOKIE[$name];

		}


		public static function destroy($name, $value = null, $time = null) {

			setcookie($name, "", time() - 3600);

		}		

	}