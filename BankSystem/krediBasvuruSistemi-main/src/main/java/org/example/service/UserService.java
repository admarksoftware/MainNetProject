package org.example.service;

import java.util.List;
import org.example.domain.User;
import org.example.dto.UserDto;
import org.example.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

@Service
public class UserService {

	@Autowired
	UserRepository userRepository;

	public List<User> findAll() {
		return userRepository.findAll();
	}


	@Transactional(isolation = Isolation.READ_COMMITTED)
	public User creditCalculate2(UserDto user){
		User response = userRepository.findByIdentity(user.getIdentity());
		if(response.getCreditScore() < 500){
			response.setCreditStatus(false);
			response.setName(user.getName());
			response.setPhone(user.getPhone());
			response.setInCome(user.getInCome());
			response.setCreditAmount(0L);
			return response;
		}
		else if(response.getCreditScore()>= 500 && response.getCreditScore()<= 1000 && response.getInCome() < 5000){
			response.setCreditStatus(true);
			response.setName(user.getName());
			response.setPhone(user.getPhone());
			response.setInCome(user.getInCome());
			response.setCreditAmount(10000L);
			return response;
		}else if(response.getCreditScore()>= 500 && response.getCreditScore()<= 1000 && response.getInCome() >= 5000){
			response.setCreditStatus(true);
			response.setName(user.getName());
			response.setPhone(user.getPhone());
			response.setInCome(user.getInCome());
			response.setCreditAmount(response.getInCome() * 4);
			return response;

		}
		else if(response.getCreditScore() >= 1000){
			response.setCreditStatus(true);
			response.setName(user.getName());
			response.setPhone(user.getPhone());
			response.setInCome(user.getInCome());
			response.setCreditAmount(response.getInCome() * 4);
			return response;
		}
		else{
			response.setCreditStatus(false);
			response.setName(user.getName());
			response.setPhone(user.getPhone());
			response.setInCome(user.getInCome());
			response.setCreditAmount(0L);
			return response;
		}
	}

}
