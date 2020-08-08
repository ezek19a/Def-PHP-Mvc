<?php

Class Openssl{
	
	public static function encrypt($string, $key){
		
		$method = "AES-256-CBC";
		
		$serverkey = 'This is my secret iv';

		// hash
		$seckey = hash('sha256', $key);
		
		// iv - encrypt method AES-256-CBC expects 16 bytes - else you will get a warning
		$iv = substr(hash('sha256', $serverkey), 0, 16);		
		
		$output = openssl_encrypt($string, $method, $seckey, 0, $iv);
		$encrypt = base64_encode($output);
	
		return $encrypt;		
	}
	
	
	public static function decrypt($string, $key){
		
		$method = "AES-256-CBC";
		
		$serverkey = 'This is my secret iv';

		// hash
		$seckey = hash('sha256', $key);
		
		// iv - encrypt method AES-256-CBC expects 16 bytes - else you will get a warning
		$iv = substr(hash('sha256', $serverkey), 0, 16);

		$decrypt = openssl_decrypt(base64_decode($string), $method, $seckey, 0, $iv);
	
		return $decrypt;
		
	}	
	
}