<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Lista de Usuarios</title>
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
                <div class="col-md-10 offset-md-1">
                    <h1 class="text-center">
                        <i class="fa fa-users"></i> Lista de Usuarios
                    </h1>
                    <hr>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                          <li class="breadcrumb-item"><a href="./">Inicio</a></li>
                          <li class="breadcrumb-item active" >Lista de Usuarios</li>
                        </ol>
                     </nav>
                    <table class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th> Documento </th>
                                <th> Correo Electrónico </th>
                                <th class="d-none d-sm-table-cell"> Dirección </th>
                                <th class="d-none d-sm-table-cell"> Teléfono </th>
                                <th> Acciones </th>
                            </tr>
                        </thead>
                        <tbody>
                            <c:forEach var="users" items="${users}">
                            <tr>
                                <td> ${users.document} </td>
                                <td> ${users.email} </td>
                                <td class="d-none d-sm-table-cell"> ${users.address} </td>
                                <td class="d-none d-sm-table-cell"> ${users.phone} </td>
                                <td> 
                                    <a href="UserController?action=show&id=${users.id}" class="btn btn-sm btn-outline-secondary"> <i class="fa fa-search"></i> </a>
                                    <a href="UserController?action=edit&id=${users.id}" class="btn btn-sm btn-outline-secondary"> <i class="fa fa-pen"></i> </a>
                                    <a href="javascript:;" class="btn btn-sm btn-outline-danger btn-delete" data-id="${users.id}"> <i class="fa fa-trash"></i> </a>
                                </td>
                            </tr>
                            </c:forEach>
                        </tbody>
                    </table>
                </div>
            </div>
        </div> 
        <script src="js/jquery-3.5.1.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
        <script src="js/sweetalert2@10.js"></script>
        <script>
                  $(document).ready(function() {
                    <% if(request.getAttribute("message") != null) { %>
                    Swal.fire({
                      position: 'top-end',
                      icon: '${type}',
                      title:'${title}',
                      text: "${message}",
                      showConfirmButton: false,
                      timer: 2500
                    })
                    <% } %>
                    $('.btn-delete').click(function(event) {
                        $id = $(this).attr("data-id");
                        Swal.fire({
                            title: 'Esta usted seguro ?',
                            text: 'Desea eliminar este registro',
                            icon: 'error',
                            showCancelButton: true,
                            cancelButtonColor: '#d0211c',
                            cancelButtonText: 'Cancelar',
                            confirmButtonColor: '#6c757d',
                            confirmButtonText: 'Aceptar',  
                        }).then((result) => {
                            if(result.value) {
                                window.location.replace("UserController?action=delete&id="+$id);
                            }
                        });
                    });
                  });
        </script>
    </body>
</html>
