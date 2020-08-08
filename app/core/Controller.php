<?php


class Controller{

	public function model($model){

		require_once '../' . APP . '/models/' . $model . '.php';
		return new $model;
	}

	public function view($view, $data = []){

		
		require_once '../' . APP . '/views/' . $view . '.php';
		

	}

}