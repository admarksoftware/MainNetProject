package org.example.controller;
import org.example.domain.User;
import org.example.dto.UserDto;
import org.example.repository.UserRepository;
import org.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class UserController {

	@Autowired
	private UserService userService;

	@PostMapping(path = "/calculate")
	public User creditCalculate(@RequestBody UserDto user) {
		return userService.creditCalculate2(user);
	}



	
 
}