package com.aplalb;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@SpringBootApplication
@Controller
public class HackBuApplication {
	@ResponseBody
	@RequestMapping("/a")
	String entry(){
		return "My Spring Boot App rere";
	}
	@ResponseBody
	@RequestMapping("/h")
	String test(){
		return "Added a string";
	}
	@RequestMapping("/")
	String index() {
	    return"index.html";
	}
	public static void main(String[] args) {
		SpringApplication.run(HackBuApplication.class, args);
	}
}
