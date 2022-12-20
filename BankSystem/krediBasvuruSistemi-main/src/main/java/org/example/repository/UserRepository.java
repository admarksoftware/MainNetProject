package org.example.repository;

import java.util.List;
import org.example.domain.*;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends CrudRepository<User, Long> {
	@Query(value = "Select * from user where identity = :identity limit 1",nativeQuery = true)
	User findByIdentity(@Param("identity") Long identity);


	List<User> findAll();


}