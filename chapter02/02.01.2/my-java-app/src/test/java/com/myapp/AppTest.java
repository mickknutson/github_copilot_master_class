package com.myapp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class AppTest {

    @Test
    public void testMain() {
        App app = new App();
        String result = app.main();
        assertEquals("Hello World", result);
    }
}