<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Consultar Usuario</title>
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
                <div class="col-md-6 offset-md-3">
                    <h1 class="text-center">
                        <i class="fa fa-search"></i> Consultar Usuario
                    </h1>
                    <hr>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                          <li class="breadcrumb-item"><a href="./">Inicio</a></li>
                          <li class="breadcrumb-item"><a href="UserController?action=list">Listar Usuarios</a></li>
                          <li class="breadcrumb-item active" >Consultar Usuario</li>
                        </ol>
                     </nav>
                     <table class="table table-hover table-striped">
                         <tr>
                             <th>ID: </th>
                             <td>${user.id}</td>
                         </tr>
                         <tr>
                             <th>Documento: </th>
                             <td>${user.document}</td>
                         </tr>
                         <tr>
                             <th>Correo Electrónico: </th>
                             <td>${user.email}</td>
                         </tr>
                         <tr>
                             <th>Dirección: </th>
                             <td>${user.address}</td>
                         </tr>
                         <tr>
                             <th>Teléfono: </th>
                             <td>${user.phone}</td>
                         </tr>
                         <tr>
                             <th>Productos: </th>
                             <td>
                                 ${user.products}
                             </td>
                         </tr>
                     </table>
                </div>
            </div>
        </div> 
        <script src="js/jquery-3.5.1.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
    </body>
</html>
