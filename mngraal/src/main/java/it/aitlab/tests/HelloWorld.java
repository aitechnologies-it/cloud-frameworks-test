package it.aitlab.tests;

import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/")
public class HelloWorld {

    @Get
    public String getHello() {
        return "Hello World!!!";
    }
}
