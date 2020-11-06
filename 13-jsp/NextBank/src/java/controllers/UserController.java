/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controllers;

import DAO.UserDAO;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import models.User;
import config.EnCrypt;

/**
 *
 * @author ofaczero
 */
public class UserController extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    
    UserDAO Udao;
    EnCrypt eCrypt;
    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String action = request.getParameter("action");
        List<User> users = new ArrayList<>();
        User user = new User();
        
        switch(action) {
            case "add":
                request.getRequestDispatcher("views/add.jsp").forward(request, response);
                break;
            case "store":
                int rs = 0;
                int document    = Integer.parseInt(request.getParameter("document"));
                String email    = request.getParameter("email");
                String address  = request.getParameter("address");
                int phone       = Integer.parseInt(request.getParameter("phone"));
                String password = eCrypt.getEncrypt(request.getParameter("password"));
                String products = request.getParameter("account1");
                if(request.getParameterMap().containsKey("account2")) {
                     products = products+","+request.getParameter("account2");
                }
                if(request.getParameterMap().containsKey("account3")) {
                     products = products+","+request.getParameter("account3");
                }
                
                User usr = new User();
                usr.setDocument(document);
                usr.setEmail(email);
                usr.setAddress(address);
                usr.setPhone(phone);
                usr.setPassword(password);
                usr.setProducts(products);
                Udao = new UserDAO();
                rs = Udao.add(usr);
              
                if(rs != 0) {
                    request.setAttribute("type", "success");
                    request.setAttribute("title", "Felicitaciones");
                    request.setAttribute("message", "Usuario Adicionado con Exito!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                } else {
                    request.setAttribute("type", "error");
                    request.setAttribute("title", "Problemas");
                    request.setAttribute("message", "Usuario No se pudo Adicionar!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                }
                break;
            case "list":
                Udao = new UserDAO();
                users = Udao.getUsers();
                request.setAttribute("users", users);
                request.getRequestDispatcher("views/list.jsp").forward(request, response);
                break;
            case "show":
                Udao = new UserDAO();
                user = Udao.getId(Integer.parseInt(request.getParameter("id")));
                request.setAttribute("user", user);
                request.getRequestDispatcher("views/show.jsp").forward(request, response);
                break;
            case "edit":
                Udao = new UserDAO();
                user = Udao.getId(Integer.parseInt(request.getParameter("id")));
                request.setAttribute("user", user);
                request.getRequestDispatcher("views/edit.jsp").forward(request, response);
                break;
            case "update":
                rs = 0;
                int id   = Integer.parseInt(request.getParameter("id"));
                document = Integer.parseInt(request.getParameter("document"));
                email    = request.getParameter("email");
                address  = request.getParameter("address");
                phone    = Integer.parseInt(request.getParameter("phone"));
                products = request.getParameter("account1");
                if(request.getParameterMap().containsKey("account2")) {
                     products = products+","+request.getParameter("account2");
                }
                if(request.getParameterMap().containsKey("account3")) {
                     products = products+","+request.getParameter("account3");
                }
                
                usr = new User();
                usr.setId(id);
                usr.setDocument(document);
                usr.setEmail(email);
                usr.setAddress(address);
                usr.setPhone(phone);
                usr.setProducts(products);
                Udao = new UserDAO();
                rs = Udao.update(usr);
              
                if(rs != 0) {
                    request.setAttribute("type", "success");
                    request.setAttribute("title", "Felicitaciones");
                    request.setAttribute("message", "Usuario Modificado con Exito!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                } else {
                    request.setAttribute("type", "error");
                    request.setAttribute("title", "Problemas");
                    request.setAttribute("message", "Usuario No se pudo Modificar!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                }
                break;
            case "delete":
                Udao = new UserDAO();
                int del = Udao.delete(Integer.parseInt(request.getParameter("id")));
                if(del != 0) {
                    request.setAttribute("type", "success");
                    request.setAttribute("title", "Felicitaciones");
                    request.setAttribute("message", "Usuario Eliminado con Exito!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                } else {
                    request.setAttribute("type", "error");
                    request.setAttribute("title", "Problemas");
                    request.setAttribute("message", "Usuario No se pudo Eliminado!");
                    request.getRequestDispatcher("UserController?action=list").forward(request, response);
                }
                break;
            default:
                throw new AssertionError();
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
