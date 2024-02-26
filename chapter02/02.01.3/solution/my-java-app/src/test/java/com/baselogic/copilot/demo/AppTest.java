package com.baselogic.copilot.demo;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {

    @Test
    public void testApp() {
        App app = new App();
        String result = app.runApp();
        assertEquals("Hello World!", result);
    }
}