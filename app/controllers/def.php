<?php

    class Def extends Controller{
        
        public function index(){

            $data['title'] = 'Def';
        
            $this->view('templates/header', $data);
            $this->view('def/index', $data);
            $this->view('templates/footer');    

        }
        
        public function detail($id){

            $data['title'] = 'Def';
            $data['mhs'] = $this->model('Def_model')->getDataById($id);
            $this->view('templates/header', $data);
            $this->view('def/detail', $data);
            $this->view('templates/footer');

        }   

        public function added(){

            if($this->model('Def_model')->addData($_POST, $_FILES['pics']['name'], $_FILES['pics']['tmp_name']) > 0 ){
            
                Flasher::setFlash(' Added ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/def');
                exit;

            }else{

                Flasher::setFlash(' Added ', 'Failed!', 'danger');
                header('Location: ' . BASEURL . '/def');
                exit;

            }

        }    

        public function delete($id){

            if($this->model('Def_model')->deleteData($id) > 0){
                Flasher::setFlash(' deleted ', 'Succesfully', 'success');
                header('Location: ' . BASEURL . '/def');
                exit;

            }else{

                Flasher::setFlash(' delete ', 'Failed', 'danger');
                header('Location: ' . BASEURL . '/def');
                exit;

            }

        }    

        public function getedit(){

            //echo $_POST['id'];

            echo json_encode($this->model('Def_model')->getEditData($_POST['id']));

        }

        public function edit(){

            if($this->model('Def_model')->editData($_POST) > 0 ){
                Flasher::setFlash(' berjaya ', 'di edit', 'success');
                header('Location: ' . BASEURL . '/def');
                exit;

            }else{

                Flasher::setFlash(' gagal ', 'di edit', 'danger');
                header('Location: ' . BASEURL . '/def');
                exit;

            }       

        }


        public function search(){

            $data['title'] = 'Def';
            $data['mhs'] = $this->model('Def_model')->searchData();
            $this->view('templates/header', $data);
            $this->view('def/index', $data);
            $this->view('templates/footer');        

        }                    
        
        public function phpinfo(){  

            phpinfo();
        }
    }

