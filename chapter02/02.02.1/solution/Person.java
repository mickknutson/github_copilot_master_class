// Description: A Person class.

// create a person class that is final
// use the final keyword to prevent inheritance
// the class should be based on the encapsulation pattern
// the class should have the following fields
// id, name, age
final class Person {
    private int id;
    private String name;
    private int age;
    
    // constructor
    public Person(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    
    // getters and setters
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        this.age = age;
    }
}
