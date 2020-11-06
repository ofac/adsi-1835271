<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>CRUD Usuarios</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" crossorigin="anonymous">
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="css/fontawesome.min.css">
        <link rel="stylesheet" href="css/owl.carousel.min.css">
        <link rel="stylesheet" href="css/owl.theme.default.min.css">
        <link rel="stylesheet" href="css/custom.css">
    </head>
    <body>
        <div class="container">
            <div class="row my-5">
                <div class="col-md-4 offset-md-4 text-center">
                    <h1>CRUD Java Web</h1>
                    <hr>  
                    <a href="UserController?action=add" class="btn btn-block btn-outline-secondary"> 
                        <i class="fa fa-plus"></i> Adicionar Usuario 
                    </a>
                    <a href="UserController?action=list" class="btn btn-block btn-outline-secondary"> 
                        <i class="fa fa-users"></i> Listar Usuarios 
                    </a>
                </div>
            </div>
        </div> 
        <script src="js/jquery-3.5.1.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
    </body>
</html>
