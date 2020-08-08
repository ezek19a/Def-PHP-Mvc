<?php

    class Api extends Controller{
        
        public function index(){

            $data['title'] = 'Api';
        
            $this->view('templates/header', $data);
            $this->view('api/index', $data);
            $this->view('templates/footer');    

        }

        public function ajaxApi(){
            
            //$data = $_POST['data'];   
                
                $logid = $_POST['logid'];
                
                $password = $_POST['password'];
                
                //$logid = $_SERVER['PHP_AUTH_USER'];
                //$password = $_SERVER['PHP_AUTH_PW'];
            
            
            
            if($this->model('Def_model')->getAccData($logid, $password)){
                
                header("Access-Control-Allow-Origin: *");
                header("Content-Type: application/json; charset=UTF-8");

                echo json_encode($this->model('Account_model')->getAccData($logid, $password));
                
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
            
            
            
            if($this->model('Account_model')->getAccData($logid, $password)){
                
                header("Access-Control-Allow-Origin: *");
                header("Content-Type: application/json; charset=UTF-8");

                echo json_encode($this->model('Account_model')->getAccData($logid, $password));
                
            }else{
                
                $msg = "Failed!";
                
                echo json_encode($msg);
            }

        }        
        
        public function detail($id){

            $data['title'] = 'Api';
            $data['mhs'] = $this->model('Api_model')->getDataById($id);
            $this->view('templates/header', $data);
            $this->view('api/detail', $data);
            $this->view('templates/footer');

        }   

        public function added(){

            if($this->model('Api_model')->addData($_POST, $_FILES['pics']['name'], $_FILES['pics']['tmp_name']) > 0 ){
            
                Flasher::setFlash(' Added ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/api');
                exit;

            }else{

                Flasher::setFlash(' Added ', 'Failed!', 'danger');
                header('Location: ' . BASEURL . '/api');
                exit;

            }

        }    

        public function delete($id){

            if($this->model('Api_model')->deleteData($id) > 0){
                Flasher::setFlash(' deleted ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/api');
                exit;

            }else{

                Flasher::setFlash(' delete ', 'Failed', 'danger');
                header('Location: ' . BASEURL . '/api');
                exit;

            }

        }    

        public function getedit(){

            //echo $_POST['id'];

            echo json_encode($this->model('Api_model')->getEditData($_POST['id']));

        }

        public function edit(){

            if($this->model('Api_model')->editData($_POST) > 0 ){
                Flasher::setFlash(' berjaya ', 'di edit', 'success');
                header('Location: ' . BASEURL . '/api');
                exit;

            }else{

                Flasher::setFlash(' gagal ', 'di edit', 'danger');
                header('Location: ' . BASEURL . '/api');
                exit;

            }       

        }


        public function search(){

            $data['title'] = 'Api';
            $data['mhs'] = $this->model('Api_model')->searchData();
            $this->view('templates/header', $data);
            $this->view('api/index', $data);
            $this->view('templates/footer');        

        }                    
        
        public function phpinfo(){  

            $data['title'] = 'Defaults';

            $this->view('defaults/phpinfo', $data);
        }
    }

