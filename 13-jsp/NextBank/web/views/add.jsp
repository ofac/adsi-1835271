<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Adicionar Usuario</title>
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
                        <i class="fa fa-plus"></i> Adicionar Usuario
                    </h1>
                    <hr>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                          <li class="breadcrumb-item"><a href="./">Inicio</a></li>
                          <li class="breadcrumb-item active" >Adicionar Usuario</li>
                        </ol>
                     </nav>
                    <form method="POST" action="UserController?action=store">
                        <div class="card">
                            <div class="card-header"> * Llenar todos los campos </div>
                            <div class="card-body">

                                <div class="form-group">
                                    <input type="number" class="form-control" name="document" placeholder="Documento de Identidad" required>
                                </div>
                                
                                <div class="form-group">
                                    <input type="email" class="form-control" name="email" placeholder="Correo Electrónico" required>
                                </div>
                                
                                <div class="form-group">
                                    <input type="text" class="form-control" name="address" placeholder="Dirección Residencia" required>
                                </div>
                                
                                <div class="form-group">
                                    <input type="number" class="form-control" name="phone" placeholder="Teléfono" required>
                                </div>
                                
                                <div class="form-group">
                                    <input type="password" class="form-control" name="password" placeholder="Contraseña" required>
                                </div>
                                
                                <div class="form-group text-left">
                                    <h5 class="h5">Productos</h5>
                                    <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="1" name="account1" required>
                                    <label class="form-check-label" for="account1">
                                      Cuenta de Ahorros
                                    </label>
                                  </div>
                                  <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="2" name="account2">
                                    <label class="form-check-label" for="account2">
                                      Cuenta Corriente
                                    </label>
                                  </div>
                                  <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="3" name="account3">
                                    <label class="form-check-label" for="account3">
                                      CDT
                                    </label>
                                  </div>
                                </div>

                            </div>
                            <div class="card-footer">
                                <button class="btn btn-outline-success"> <i class="fa fa-save"></i> Adicionar </button>
                                <a class="btn btn-outline-secondary" href="./"> <i class="fa fa-arrow-left"></i> Cancelar </a>
                            </div>
                          </div>
                      </form>
                </div>
            </div>
        </div> 
        <script src="js/jquery-3.5.1.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
    </body>
</html>
