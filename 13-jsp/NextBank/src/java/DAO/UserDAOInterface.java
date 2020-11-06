/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAO;

import java.util.List;
import models.User;

/**
 *
 * @author ofaczero
 */
public interface UserDAOInterface {
    public List<User>getUsers();
    public User getId(int id);
    public int add(User usr);
    public int update(User usr);
    public int delete(int id);
}
