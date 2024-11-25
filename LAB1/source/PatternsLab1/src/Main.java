// Many-to-many зв'язок реалізовано через списки операторів у класі Customer та списки клієнтів у класі Operator.
// Клієнти можуть мати кілька операторів через метод addOperator().
// Оператор може обслуговувати кілька клієнтів через метод addCustomer().

import java.util.ArrayList;

import java.util.List;

class Bill {
    private double limitingAmount;
    private double currentDebt;

    public Bill(double limitingAmount) {
        this.limitingAmount = limitingAmount;
        this.currentDebt = 0;
    }

    public boolean check(double amount) {
        return currentDebt + amount <= limitingAmount;
    }

    public void add(double amount) {
        if (check(amount)) {
            currentDebt += amount;
        }
    }

    public void pay(double amount) {
        currentDebt -= amount;
    }

    public void changeTheLimit(double amount) {
        this.limitingAmount = amount;
    }

    public double getLimitingAmount() {
        return limitingAmount;
    }

    public double getCurrentDebt() {
        return currentDebt;
    }
}

class Operator {
    private int ID;
    private double talkingCharge;
    private double messageCost;
    private double networkCharge;
    private int discountRate;
    private List<Customer> customers;  // Список клієнтів, які обслуговуються оператором

    public Operator(int ID, double talkingCharge, double messageCost, double networkCharge, int discountRate) {
        this.ID = ID;
        this.talkingCharge = talkingCharge;
        this.messageCost = messageCost;
        this.networkCharge = networkCharge;
        this.discountRate = discountRate;
        this.customers = new ArrayList<>();  // Ініціалізація списку клієнтів
    }

    public void addCustomer(Customer customer) {
        customers.add(customer);  // Додаємо клієнта до списку
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public double calculateTalkingCost(int minute, Customer customer) {
        double cost = minute * talkingCharge;
        if (customer.getAge() < 18 || customer.getAge() > 65) {
            cost -= cost * discountRate / 100.0;
        }
        return cost;
    }

    public double calculateMessageCost(int quantity, Customer customer, Customer other) {
        double cost = quantity * messageCost;
        if (customer.getOperators().contains(other.getOperators().get(0))) {
            cost -= cost * discountRate / 100.0;
        }
        return cost;
    }

    public double calculateNetworkCost(double amount) {
        return amount * networkCharge;
    }

    public double getTalkingCharge() {
        return talkingCharge;
    }

    public double getMessageCost() {
        return messageCost;
    }

    public double getNetworkCharge() {
        return networkCharge;
    }

    public int getDiscountRate() {
        return discountRate;
    }
}

class Customer {
    private int ID;
    private String name;
    private int age;
    private List<Operator> operators;  // Список операторів
    private Bill bill;

    public Customer(int ID, String name, int age, Bill bill) {
        this.ID = ID;
        this.name = name;
        this.age = age;
        this.bill = bill;
        this.operators = new ArrayList<>();  // Ініціалізація списку операторів
    }

    public void addOperator(Operator operator) {
        operators.add(operator);
        operator.addCustomer(this);  // Додаємо клієнта до оператора
    }

    public void talk(int minute, Customer other) {
        // Вибираємо перший оператор для обчислення вартості
        Operator operator = operators.get(0);
        double cost = operator.calculateTalkingCost(minute, this);
        if (bill.check(cost)) {
            bill.add(cost);
        }
    }

    public void message(int quantity, Customer other) {

        Operator operator = operators.get(0);
        double cost = operator.calculateMessageCost(quantity, this, other);
        if (bill.check(cost)) {
            bill.add(cost);
        }
    }

    public void connection(double amount) {

        Operator operator = operators.get(0);
        double cost = operator.calculateNetworkCost(amount);
        if (bill.check(cost)) {
            bill.add(cost);
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public List<Operator> getOperators() {
        return operators;
    }

    public void setOperators(List<Operator> operators) {
        this.operators = operators;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
}

public class Main {
    public static void main(String[] args) {

        Operator operator1 = new Operator(0, 0.1, 0.05, 0.02, 10);
        Operator operator2 = new Operator(1, 0.2, 0.07, 0.03, 15);

        // Create bills
        Bill bill1 = new Bill(100);
        Bill bill2 = new Bill(200);


        Customer customer1 = new Customer(0, "Bogdan", 14, bill1);
        Customer customer2 = new Customer(1, "Stanislav", 18, bill2);


        customer1.addOperator(operator1);
        customer2.addOperator(operator2);


        customer1.talk(10, customer2);
        customer2.talk(20, customer1);
        customer1.message(5, customer2);
        customer1.connection(50);


        System.out.println("Customer 1's current debt: " + customer1.getBill().getCurrentDebt());
        System.out.println("Customer 2's current debt: " + customer2.getBill().getCurrentDebt());
    }
}
