package org.example;


import static org.assertj.core.api.Assertions.assertThat;

import org.example.domain.User;
import org.example.repository.UserRepository;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@ActiveProfiles("test")
@DataJpaTest
@AutoConfigureTestDatabase(replace= AutoConfigureTestDatabase.Replace.NONE)
public class UserRepositoryMySQLTest {
 
    @Autowired
    private TestEntityManager entityManager;
 
    @Autowired
    private UserRepository USER_REPOSITORY;
 
    // write test cases here

    @Test
    public void addNewIssue() {
        User resultSet = USER_REPOSITORY.findByIdentity(20924544887L);
        System.out.println("Credit Score = " + resultSet.getCreditScore());
    }
}