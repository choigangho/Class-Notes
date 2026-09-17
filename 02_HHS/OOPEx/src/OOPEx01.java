// 객체지향형(유지보수가 편리한) 프로그래밍

class Person {
    private String name;    // 캡슐화
    public int age;

    public void setName(String n ) {
        name = n + "님";
    }
    public String getName( ) {
        return name;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }
    public int getAge() {
        return age;
    }

}

public class OOPEx01 {
    public static void main(String[] args) {

        // 다음 코드는 객체지향형 프로그래밍인가?
        // つまり 유지보수 관리가 편한가?
        Person p1 = new Person();
        // p1.name = "최강호";     // 이건 OOP가 아님 -> 유지보수 불편쓰
        p1.setName("최강호");      // 이건 OOP임
        p1.setAge(25);

        Person p2 = new Person();
        // p2.name = "이상혁";
        p2.setName("이상혁");
        p2.setAge(29);

        Person p3 = new Person();
        // p3.name = "김기인";
        p3.setName("김기인");
        p3.setAge(28);

    }
}
