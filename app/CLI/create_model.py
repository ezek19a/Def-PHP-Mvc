# php.py

import os
  
#controller = os.mkdir('controller')

if not os.path.exists('../models'):
    os.makedirs('../models')

userinput = input('Please Enter Filename!: ')

ext = "_model.php"

ufilename = userinput+ext

filename = ufilename.title()

uclassinput = input('Please Enter Model Class name!: ')

classinput = uclassinput.title()

dbtable = input('Please Enter Database Table name!: ')

f = open('../models/'+filename,'w')

message = """<?php

class """+classinput+"""_model{

	private $table = '"""+dbtable+"""';
	private $db;


	public function __construct(){

		$this->db = new Database;

	}
    
	public function loginCheck($data){

		$query = "SELECT * FROM users WHERE (username = :logid OR contact = :logid OR email = :logid) AND status = 1 AND password = :password";

		$this->db->query($query);
		$this->db->bind(':logid', $data['logid']);
		$this->db->bind(':password', md5($data['password']));
		$this->db->execute();

		return $this->db->rowCount();		

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

		$query = "INSERT INTO """+dbtable+""" VALUES('', :username, :contact, :email, :pics, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)";
		
		$this->db->query($query);		

		$this->db->bind('username', $data['username']);
		$this->db->bind('contact', $data['contact']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('pics', $pics);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}

	public function createUser($data){

		$query = "INSERT INTO users VALUES('', :username, :email, :contact, :password, status, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)";
		
		$this->db->query($query);		

		$this->db->bind('username', $data['username']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('contact', $data['contact']);
		$this->db->bind('password', md5($data['password']));
        $this->db->bind('status', $data['status']);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}


	public function deleteData($id){

		$query = "DELETE FROM """+dbtable+""" WHERE id = :id";

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

		$query = "UPDATE """+dbtable+""" SET
					username = :username,
					contact = :contact,
					email = :email,
					password = :password
				  WHERE id = :id";
		
		$this->db->query($query);		

		$this->db->bind('username', $data['username']);
		$this->db->bind('contact', $data['contact']);
		$this->db->bind('email', $data['email']);
		$this->db->bind('password', $password);
		$this->db->bind('id', $data['id']);

		$this->db->execute();

		return $this->db->rowCount();

		//return 0;
	}	

	public function searchData(){

		$keyword = $_POST['keyword'];
		$query = "SELECT * FROM """+dbtable+""" WHERE keywords LIKE :keyword ORDER BY id DESC";
		$this->db->query($query);
		$this->db->bind(':keyword', "%$keyword%");
		return $this->db->resultSet();

	}	
    
 	public function checkUserPass($data){

		$query = "SELECT * FROM users WHERE password = :password";

		$this->db->query($query);
		$this->db->bind(':password', md5($data['password']));
		$this->db->execute();

		return $this->db->rowCount();			

	}
   
	public function changeUserPass($data, $password){

	$query = "UPDATE users SET
				password = :password
			  WHERE id = :id";
		
	$this->db->query($query);		
    $this->db->bind('password', md5($data['password']));		
	$this->db->bind('id', $data['id']);

	$this->db->execute();

	return $this->db->rowCount();

	//return 0;
		
	}
    
	public function resetPass($data, $password){

	$query = "UPDATE users SET
				password = :password
			  WHERE email = :email";
		
	$this->db->query($query);		
    $this->db->bind('password', md5($data['password']));		
	$this->db->bind('email', $data['email']);

	$this->db->execute();

	return $this->db->rowCount();

	//return 0;
		
	}    
    
	public function checkToken($data){

		$query = "SELECT * FROM apiverify WHERE token = :token AND status = 1";

		$this->db->query($query);
		$this->db->bind(':token', $data['token']));
		$this->db->execute();

		return $this->db->rowCount();		
	

	}

"""

f.write(message)
f.close()