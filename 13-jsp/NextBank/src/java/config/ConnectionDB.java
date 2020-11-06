/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author ofaczero
 */
public class ConnectionDB {
    private static Connection con = null;
    private static final String URL  = "jdbc:mysql://localhost:3306/nextbank";
    private static final String USER = "root";
    private static final String PASS = "";
    
    public static Connection getConnection() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection(URL, USER, PASS);
        } catch(ClassNotFoundException | SQLException e) {
            System.err.println("Error: "+e);
        }
            
        return con;
    } 
}
