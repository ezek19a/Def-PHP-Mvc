# create_controllers.py

import os
  
#controller = os.mkdir('controller')

if not os.path.exists('../controllers'):
    os.makedirs('../controllers')
    os.makedirs('../views')
    
userinput = input('Please Enter Filename!: ')

os.makedirs('../views/'+userinput)

ext = ".php"

filename = userinput+ext

uclassinput = input('Please Enter Class name!: ')

classinput = uclassinput.title()

f = open('../controllers/'+filename,'w')
g = open('../views/'+userinput+'/index.php','w')

if not os.path.exists('../views/templates'):
    os.makedirs('../views/templates')

h = open('../views/templates/header.php','w')
i = open('../views/templates/footer.php','w')    

message = """<?php

    class """ + classinput + """ extends Controller{
        
        public function index(){

            $data['title'] = '"""+classinput+"""';
        
            $this->view('templates/header', $data);
            $this->view('"""+userinput+"""/index', $data);
            $this->view('templates/footer');    

        }
        
 	public function User(){
		
		$data['title'] = "User";

		$this->view('templates/header', $data);
		$this->view('users/index', $data);
		$this->view('templates/footer');	
	
	}	

	public function dashboard(){
		
		$logged = Session::get('loggedIn');
		
		if ($logged == false) {
			
			Session::destroy();
			header('location: ' . BASEURL .  'dashboard/login');
			exit;
			
		}
		
		$uid = Session::get('uid');
		
		$data['users'] = $this->model('Users_model')->getAllData($uid);

		$data['title'] = "User";

		$this->view('templates/header', $data);
		$this->view('dashboard/index', $data);
		$this->view('templates/footer');	
	
	}
	
	public function resetPass(){
		
	$password = $_POST['npassword'];
	$email = $_POST['emailpass'];
	
	$apassword = Openssl::encrypt($password,$email);

		if($this->model('Users_model')->checkAccPassword($_POST) > 0 ){	

				$change = $this->model('Users_model')->changeAccPassword($_POST, $apassword);

			if($change > 0 ){
				
			$to = $email;
			$subject = "MVC Crud Password Changed";
			$message = "
			<html>
			<head>
			<title>MVC Crud Password Changed</title>
			</head>
			<body>
			<p>Hai '$username'</p>
			<p><h2>Acc Info</h2></p>
			<p>Login ID:  '$username'</p>
			<p>Your New Password:  '$password'</p>
			<p>
			Thank you,<br >
			MVC Crud <br >
			Hotline : 012-3456789
			</p>
			</body>
			</html>
			";
			// Always set content-type when sending HTML email
			$headers = "MIME-Version: 1.0" . "\r\n";
			$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
			// More headers
			$headers .= 'From: <admin@progse.com>' . "\r\n";
			$headers .= 'Cc: myboss@example.com' . "\r\n";
			mail($to,$subject,$message,$headers);				
				
			Session::destroy();
			Session::setFlash(' Password Change ', 'Succesfully', 'success');			
			header('Location: ' . BASEURL . 'Users/login');
			exit;

			}else{

				Session::setFlash(' Failed ', 'to Change Password', 'danger');
				header('Location: ' . BASEURL . 'Users');
				exit;

			}

		}else{

			Session::setFlash(' Current ', 'Password Invalid', 'danger');
			header('Location: ' . BASEURL . 'Users');
			exit;			

		}
		
	}
	

	public function login(){

		$data['title'] = "Login";

		$this->view('templates/header', $data);
		$this->view('dashboard/login', $data);
		$this->view('templates/footer');

	}


	public function loginCheck(){

		$data['title'] = "Login Check";

		$logid = $_POST['logid'];

		$password = $_POST['password'];
		
		if($this->model('Users_model')->loginCheck($_POST) > 0){
			
			$data['users'] = $this->model('Users_model')->getUserData($logid, $password);
			
			$uid = $data['users']['id'];
			
			Session::set('uid', $uid);
			Session::set('loggedIn', true);

			Session::setFlash(' Succesfully ', 'Logged in', 'success');
			header('Location: ' . BASEURL . 'dashboard');
			exit;

		}else{
			
			Session::setFlash(' Password maybe Wrong or your Users is not activate ', 'please check your email', 'danger');
			
			?>
				<script>
					alert("Failed");
				</script>
			
			<?php
			header('Location: ' . BASEURL . 'dashboard/login');
			exit;
		}

	}


	public function create(){

		$pics = BASEURL . "uploads/" . $_FILES["file"]["name"];

			$username = $_POST['username'];
			$password = $_POST['password'];
			$email = $_POST['email'];		
			$contact = $_POST['contact'];
			
			$apassword = Openssl::encrypt($password,$email);

		if($this->model('Users_model')->createAcc($_POST, $pics, $apassword) > 0){
			
			
			$url = 'https://api.twilio.com/2010-04-01/Users/+yourtoke+/Messages.json';		
 
			$from = "+14792529356";

			$to = "+6".$contact;
			
			$root = (!empty($_SERVER['HTTPS']) ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . '/';
			$activate = $root.ACTVURL.$username."/".$password;			

			$body = $activate;

			$id = "AC4244a6a3efbb7ac8da72613fca003bf6";

			$token = "f10db1f05c42bc6f8074175c88f487da";

			$data = array (

					'From' => $from,
					'To' => $to,
					'Body' => $body
					
					);
					
			$post = http_build_query($data);
			$x = curl_init($url);
			curl_setopt($x, CURLOPT_POST, true);
			curl_setopt($x, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($x, CURLOPT_USERPWD, "$id:$token");
			curl_setopt($x, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
			curl_setopt($x, CURLOPT_POSTFIELDS, $post);

			var_dump($post);
			$y = curl_exec($x);
			var_dump($y);
			curl_close($x);


			$root = (!empty($_SERVER['HTTPS']) ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . '/';
			$activate = $root.ACTVURL.$username."/".$password;
			$to = $email;
			$subject = "MVC Crud Registration";
			$message = "
			<html>
			<head>
			<title>MVC Crud Registration</title>
			</head>
			<body>
			<p>Hai '$username'</p>
			<p><h2>Acc Info</h2></p>
			<p>Activation URL :  '$activate'</p>
			<p>Login ID:  '$username'</p>
			<p>Password:  '$password'</p>
			<p>
			Thank you,<br >
			MVC Crud <br >
			Hotline : 012-3456789
			</p>
			</body>
			</html>
			";
			// Always set content-type when sending HTML email
			$headers = "MIME-Version: 1.0" . "\r\n";
			$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
			// More headers
			$headers .= 'From: <admin@progse.com>' . "\r\n";
			$headers .= 'Cc: myboss@example.com' . "\r\n";
			mail($to,$subject,$message,$headers);			
		
			Session::setFlash(' Succesfully ', 'Added', 'success');
			header('Location: ' . BASEURL . 'Users/login');
			exit;

		}else{

			Session::setFlash(' Failed ', 'to Add', 'danger');
			header('Location: ' . BASEURL . 'Users/login');
			exit;

		}		

	}

	
	public function email_activation($logid, $password){	
			
			$data['Users'] = $this->model('Users_model')->getAccData($logid, $password);
			
			$uid = $data['Users']['id'];
			
				if($this->model('Users_model')->editStatus($uid) > 0 ){
					
					?>
					
					<script type="text/javascript">
					
						alert("Akaun anda telah di Aktifkan!");

						window.close();
					
					</script>
					
					<?php

				}else{
					
					?>
					
					<script type="text/javascript">
					
						alert("Akaun anda gagal di Aktifkan!");

						window.close();
					
					</script>
					
					<?php

				}					
		
	}


	public function logout(){
		
		Session::destroy();
		header('location: ' . BASEURL .  'Users/login');
		exit;

	}


	public function editAcc(){

		//echo $_POST['id'];

		echo json_encode($this->model('Users_model')->editAccData($_POST['id']));

	}	


	public function editUsers(){
		
		//echo $_POST['id'];	

		$username = $_POST['username'];
		$contact = $_POST['contact'];
		$email = $_POST['email'];		
		
		if($this->model('Users_model')->editUsersData($_POST) > 0 ){
			
			$to = $email;
			$subject = "MVC Crud Users Modified";
			$message = "
			<html>
			<head>
			<title>MVC Crud Users Modified</title>
			</head>
			<body>
			<p>Hai '$username'</p>
			<p><h2>Acc Info</h2></p>
			<p>Login ID:  '$username'</p>
			<p>Contact Number:  '$contact'</p>
			<p>Email:  '$email'</p>
			<p>
			Thank you,<br >
			MVC Crud <br >
			Hotline : 012-3456789
			</p>
			</body>
			</html>
			";
			// Always set content-type when sending HTML email
			$headers = "MIME-Version: 1.0" . "\r\n";
			$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
			// More headers
			$headers .= 'From: <admin@progse.com>' . "\r\n";
			$headers .= 'Cc: myboss@example.com' . "\r\n";
			mail($to,$subject,$message,$headers);	
			
			Session::setFlash(' Users Edited ', 'Succesfully', 'success');
			header('Location: ' . BASEURL . 'Users');
			exit;

		}else{
			
			Session::setFlash(' Failed ', 'to Edit Users', 'danger');
			header('Location: ' . BASEURL . 'Users');
			exit;

		}

	}



	public function editPic(){

		$pics = BASEURL . "uploads/" . $_FILES["file"]["name"];

		if($this->model('Users_model')->changeAccPic($_POST, $pics) > 0 ){

			Session::setFlash(' Picture Change ', 'Succesfully', 'success');
			header('Location: ' . BASEURL . 'Users');
			exit;

		}else{

			Session::setFlash(' Failed ', 'to Change Picture', 'danger');
			header('Location: ' . BASEURL . 'Users');
			exit;

		}	

	}


	public function changePassword(){

	$username = $_POST['userpass'];
	$password = $_POST['npassword'];
	$email = $_POST['emailpass'];
	
	$apassword = Openssl::encrypt($password,$email);

		if($this->model('Users_model')->checkAccPassword($_POST) > 0 ){	

				$change = $this->model('Users_model')->changeAccPassword($_POST, $apassword);

			if($change > 0 ){
				
			$to = $email;
			$subject = "MVC Crud Password Changed";
			$message = "
			<html>
			<head>
			<title>MVC Crud Password Changed</title>
			</head>
			<body>
			<p>Hai '$username'</p>
			<p><h2>Acc Info</h2></p>
			<p>Login ID:  '$username'</p>
			<p>Your New Password:  '$password'</p>
			<p>
			Thank you,<br >
			MVC Crud <br >
			Hotline : 012-3456789
			</p>
			</body>
			</html>
			";
			// Always set content-type when sending HTML email
			$headers = "MIME-Version: 1.0" . "\r\n";
			$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
			// More headers
			$headers .= 'From: <admin@progse.com>' . "\r\n";
			$headers .= 'Cc: myboss@example.com' . "\r\n";
			mail($to,$subject,$message,$headers);				
				
			Session::destroy();
			Session::setFlash(' Password Change ', 'Succesfully', 'success');			
			header('Location: ' . BASEURL . 'Users/login');
			exit;

			}else{

				Session::setFlash(' Failed ', 'to Change Password', 'danger');
				header('Location: ' . BASEURL . 'Users');
				exit;

			}

		}else{

			Session::setFlash(' Current ', 'Password Invalid', 'danger');
			header('Location: ' . BASEURL . 'Users');
			exit;			

		}		

	}
	
	
	public function passcheck(){
		
		$email = $_POST['email'];
				
		if($this->model('Users_model')->getPass($_POST['email']) > 0 ){	

		$data['Users'] = $this->model('Users_model')->getPass($_POST['email']);
		
		$apassword = $data['Users']['apassword'];
		
		$password = Openssl::decrypt($apassword, $email);		

			if($password != null ){
				
			$to = $email;
			$subject = "MVC Crud Forgot Password";
			$message = "
			<html>
			<head>
			<title>MVC Crud PForgot Password</title>
			</head>
			<body>
			<p>Hai '$username'</p>
			<p><h2>Acc Info</h2></p>
			<p>Login ID:  '$username'</p>
			<p>Your Password is:  '$password'</p>
			<p>
			Thank you,<br >
			MVC Crud <br >
			Hotline : 012-3456789
			</p>
			</body>
			</html>
			";
			// Always set content-type when sending HTML email
			$headers = "MIME-Version: 1.0" . "\r\n";
			$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
			// More headers
			$headers .= 'From: <admin@progse.com>' . "\r\n";
			$headers .= 'Cc: myboss@example.com' . "\r\n";
			mail($to,$subject,$message,$headers);				
				
			Session::setFlash(' Forgot Password Send ', 'Succesfully', 'success');			
			header('Location: ' . BASEURL . 'Users/forgotpass');
			exit;

			}else{

				Session::setFlash(' Failed ', 'to send Password', 'danger');
				header('Location: ' . BASEURL . 'Users/forgotpass');
				exit;

			}

		}else{

			Session::setFlash(' Email ', 'Not Exist', 'danger');
			header('Location: ' . BASEURL . 'Users/forgotpass');
			exit;			

		}	
		
	}
	
	public function ajaxApi(){
		
		//$data = $_POST['data'];	
			
			$logid = $_POST['logid'];
			
			$password = $_POST['password'];
			
			//$logid = $_SERVER['PHP_AUTH_USER'];
			//$password = $_SERVER['PHP_AUTH_PW'];
		
		
		
		if($this->model('Users_model')->getAccData($logid, $password)){
			
			header("Access-Control-Allow-Origin: *");
			header("Content-Type: application/json; charset=UTF-8");

			echo json_encode($this->model('Users_model')->getAccData($logid, $password));
			
		}else{
			
			$msg = "Failed!";
			
			echo json_encode($msg);
		}

	}

	public function curlApi(){
		
		//$data = $_POST['data'];	
			
			//$logid = $_POST['logid'];			
			//$password = $_POST['password'];
			
			$logid = $_SERVER['PHP_AUTH_USER'];
			$password = $_SERVER['PHP_AUTH_PW'];
		
		
		
		if($this->model('Users_model')->getAccData($logid, $password)){
			
			header("Access-Control-Allow-Origin: *");
			header("Content-Type: application/json; charset=UTF-8");

			echo json_encode($this->model('Users_model')->getAccData($logid, $password));
			
		}else{
			
			$msg = "Failed!";
			
			echo json_encode($msg);
		}

	}               
        
        public function detail($id){

            $data['title'] = '"""+classinput+"""';
            $data['mhs'] = $this->model('"""+classinput+"""_model')->getDataById($id);
            $this->view('templates/header', $data);
            $this->view('"""+userinput+"""/detail', $data);
            $this->view('templates/footer');

        }   

        public function added(){

            if($this->model('"""+classinput+"""_model')->addData($_POST, $_FILES['pics']['name'], $_FILES['pics']['tmp_name']) > 0 ){
            
                Flasher::setFlash(' Added ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }else{

                Flasher::setFlash(' Added ', 'Failed!', 'danger');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }

        }    

        public function delete($id){

            if($this->model('"""+classinput+"""_model')->deleteData($id) > 0){
                Flasher::setFlash(' deleted ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }else{

                Flasher::setFlash(' delete ', 'Failed', 'danger');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }

        }    

        public function getedit(){

            //echo $_POST['id'];

            echo json_encode($this->model('"""+classinput+"""_model')->getEditData($_POST['id']));

        }

        public function edit(){

            if($this->model('"""+classinput+"""_model')->editData($_POST) > 0 ){
                Flasher::setFlash(' berjaya ', 'di edit', 'success');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }else{

                Flasher::setFlash(' gagal ', 'di edit', 'danger');
                header('Location: ' . BASEURL . '/"""+userinput+"""');
                exit;

            }       

        }


        public function search(){

            $data['title'] = '"""+classinput+"""';
            $data['mhs'] = $this->model('"""+classinput+"""_model')->searchData();
            $this->view('templates/header', $data);
            $this->view('"""+userinput+"""/index', $data);
            $this->view('templates/footer');        

        }                    
        
        public function phpinfo(){  

            $data['title'] = 'Defaults';

            $this->view('defaults/phpinfo', $data);
        }

        
    }

"""

f.write(message)
f.close()


content = """<h1>Hello World!</h1>"""

g.write(content)
g.close()

header = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>"""
  
h.write(header)
h.close()

footer = """    <!-- Optional JavaScript -->
    <!-- Popper.js first, then Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
  </body>
</html>"""
  
i.write(footer)
i.close()