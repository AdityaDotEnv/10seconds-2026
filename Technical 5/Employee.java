public class Employee {
    private String name;
    private int age;
    private double salary;

    public void getData(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public void printData() {
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Age: " + age);
        System.out.println("Employee Salary: " + salary);
        System.out.println();
    }
}

class Main {
    public static void main(String[] args) {
        Employee e1 = new Employee();
        e1.getData("Alex", 21, 32000);
        e1.printData();

        Employee e2 = new Employee();
        e2.getData("Brian", 25, 15000);
        e2.printData();

    }
}
