  package com.example.myhava;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication

public class MyhavaApplication {

	public static void main(String[] args) {

		SpringApplication.run(MyhavaApplication.class, args);
		System.out.println("basarili");
	}

}
