/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAO;

import config.ConnectionDB;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import models.User;

/**
 *
 * @author ofaczero
 */
public class UserDAO implements UserDAOInterface {

    @Override
    public List<User> getUsers() {
        List<User> users = new ArrayList<>();
        String sql = "SELECT * FROM users";
        try {
            PreparedStatement ps = ConnectionDB.getConnection().prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()) {
                User usr = new User();
                usr.setId(rs.getInt(1));
                usr.setDocument(rs.getInt(2));
                usr.setEmail(rs.getString(3));
                usr.setAddress(rs.getString(4));                
                usr.setPhone(rs.getInt(5));
                users.add(usr);
            }
        } catch(SQLException e) {
            System.err.println("Error: "+e);
        }
        return users;
    }

    @Override
    public User getId(int id) {
        String sql = "SELECT * FROM users WHERE id = ?";
        User usr = new User();
        try {
            PreparedStatement ps = ConnectionDB.getConnection().prepareStatement(sql);
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            while(rs.next()) {
                usr.setId(rs.getInt(1));
                usr.setDocument(rs.getInt(2));
                usr.setEmail(rs.getString(3));
                usr.setAddress(rs.getString(4));                
                usr.setPhone(rs.getInt(5));
                usr.setProducts(rs.getString(7));
            }
        } catch(SQLException e) {
            System.err.println("Error: "+e);
        }
        return usr;
    }

    @Override
    public int add(User usr) {
        String sql = "INSERT INTO users(document, email, address, phone, password, products) VALUES(?, ?, ?, ?, ?, ?)";
        int result = 0;
        try {
            PreparedStatement ps = ConnectionDB.getConnection().prepareStatement(sql);
            ps.setInt(1,    usr.getDocument());
            ps.setString(2, usr.getEmail());
            ps.setString(3, usr.getAddress());
            ps.setInt(4,    usr.getPhone());
            ps.setString(5, usr.getPassword());
            ps.setString(6, usr.getProducts());
            result = ps.executeUpdate();
        } catch(SQLException e) {
            System.err.println("Error: "+e);
        }
        return result;
    }

    @Override
    public int update(User usr) {
        String sql = "UPDATE users SET document = ?, email = ?, address = ?, phone = ?, products = ? WHERE id = ?";
        int result = 0;
        try {
            PreparedStatement ps = ConnectionDB.getConnection().prepareStatement(sql);
            ps.setInt(1,    usr.getDocument());
            ps.setString(2, usr.getEmail());
            ps.setString(3, usr.getAddress());
            ps.setInt(4,    usr.getPhone());
            ps.setString(5, usr.getProducts());
            ps.setInt(6, usr.getId());
            result = ps.executeUpdate();
        } catch(SQLException e) {
            System.err.println("Error: "+e);
        }
        return result;
    }

    @Override
    public int delete(int id) {
        String sql = "DELETE FROM users WHERE id = ?";
        int result = 0;
        try {
            PreparedStatement ps = ConnectionDB.getConnection().prepareStatement(sql);
            ps.setInt(1, id);
            result = ps.executeUpdate();
        } catch(SQLException e) {
            System.err.println("Error: "+e);
        }
        return result;
    }
    
}
