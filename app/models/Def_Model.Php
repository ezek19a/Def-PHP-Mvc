<?php

class Def_model{

	private $table = 'def';
	private $db;

	public function __construct(){

		$this->db = new Database;

	}

	public function getAllData(){

		$this->db->query('SELECT * FROM ' . $this->table . ' ORDER BY id DESC');
		return $this->db->resultSet();

	}


	public function getDataById($id){

		$this->db->query('SELECT * FROM ' . $this->table . ' WHERE id=:id');

		$this->db->bind('id', $id);
		return $this->db->single();

	}


	public function addNewData($data, $pics){

		$query = "INSERT INTO def VALUES('', :username, :contact, :email, :pics, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)";
		
		$this->db->query($query);		

		$this->db->bind('username', $data['username']);
		$this->db->bind('contact', $data['contact']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('pics', $pics);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}

	public function addData($data){

		$query = "INSERT INTO def VALUES('', :nama, :nrp, :email, :jurusan)";
		
		$this->db->query($query);		

		$this->db->bind('nama', $data['nama']);
		$this->db->bind('nrp', $data['nrp']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('jurusan', $data['jurusan']);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}


	public function deleteData($id){

		$query = "DELETE FROM def WHERE id = :id";

		$this->db->query($query);
		$this->db->bind('id', $id);

		$this->db->execute();

		return $this->db->rowCount();

	}

	public function getEditData($id){

		$this->db->query('SELECT * FROM ' . $this->table . ' WHERE id=:id');

		$this->db->bind('id', $id);
		return $this->db->single();		

	}


	public function editData($data, $pics){

		$query = "UPDATE def SET
					username = :username,
					contact = :contact,
					email = :email,
					pics = :pics
				  WHERE id = :id";
		
		$this->db->query($query);		

		$this->db->bind('username', $data['username']);
		$this->db->bind('contact', $data['contact']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('pics', $pics);
		$this->db->bind('id', $data['id']);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}	

	public function searchData(){

		$keyword = $_POST['keyword'];
		$query = "SELECT * FROM def WHERE keywords LIKE :keyword ORDER BY id DESC";
		$this->db->query($query);
		$this->db->bind(':keyword', "%$keyword%");
		return $this->db->resultSet();

	}	

