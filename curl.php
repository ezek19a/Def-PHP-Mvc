<?php

		

	$url = "https://github.com/ezek19a/def/blob/master/def/public/def/curlApi";		

 

	$logid = "ezek19";



	$pass = "ezek1234";



	$data = array(			

	

	);

	

			$post = http_build_query($data);

			

			$x = curl_init($url);

			curl_setopt($x, CURLOPT_POST, true);

			curl_setopt($x, CURLOPT_RETURNTRANSFER, true);

			curl_setopt($x, CURLOPT_USERPWD, "$logid:$pass");

			curl_setopt($x, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);

			curl_setopt($x, CURLOPT_POSTFIELDS, $post);



			//var_dump($post);

			$y = curl_exec($x);

			//var_dump($y);

			curl_close($x);

			

			$a = json_decode($y);

			

			$array = json_decode(trim($y), TRUE);

			//print_r($array);

			

			foreach($a as $key => $value){				

				echo $key ." : ". $value;

				echo "<br />";				

			}			

			

			echo $y;

			echo "<br />";	

			echo "<img src='". $array['pics'] . "' width='10%'>";
