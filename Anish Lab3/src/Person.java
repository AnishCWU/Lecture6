
import java.io.Serializable;
import java.lang.String;

public class Person implements Serializable, Comparable<Person> {
    // Declare a private string variable "name" to store the name of the person.
    private String name;

    // Declare a private string variable "address" to store the address of the person.
    private String address;

    // Declare a private string variable "phone" to store the phone number of the person.
    private String phone;

    // Create a default constructor to initialize the variables.
    public Person() {
        name = "";
        address = "";
        phone = "";
    }

    // Create a constructor with parameters to set the values of the variables.
    public Person(String name, String address, String phone) {
        this.name = name;
        this.address = address;
        this.phone = phone;
    }

    // Create a method "getName()" to return the value of name.
    public String getName() {
        return this.name;
    }

    // Create a method "getAddress()" to return the value of address.
    public String getAddress() {
        return this.address;
    }

    // Create a method "getPhone()" to return the value of phone.
    public String getPhone() {
        return this.phone;
    }

    // Create a method "setName()" to set the value of name.
    public void setName(String newName) {
        // Trim the input value to remove any leading or trailing white spaces.
        newName = newName.trim();

        // Check if the input value is empty and throw an error if it is.
        if (newName.equals("")) {
            throw new Error("The name can not be empty");
        }

        // Set the value of name to the input value.
        this.name = newName;
    }

    // Create a method "setAddress()" to set the value of address.
    public void setAddress(String newAddress) {
        // Trim the input value to remove any leading or trailing white spaces.
        newAddress = newAddress.trim();

        // Check if the input value is empty and throw an error if it is.
        if (newAddress.equals("")) {
            throw new Error("The address can not be empty!!!");
        }

        // Set the value of address to the input value.
        this.address = newAddress;
    }

    // Create a method "setPhone()" to set the value of phone.
    public void setPhone(String newPhone) {
        // Trim the input value to remove any leading or trailing white spaces.
        newPhone = newPhone.trim();

        // Check if the input value is empty and throw an error if it is.
        if (newPhone.equals("")) {
            throw new Error("The phone can not be empty!!!");
        }

        // Set the value of phone to the input value.
        this.phone = newPhone;
    }

    // Create a method "toString()" to display the values of the variables in a formatted string.
    public String toString() {
        return name + "\n" + address + "\n" + phone;
    }

    // Create a method "compareTo()" to compare the names of two persons.
    @Override
    public int compareTo(Person o) {
        return this.name.compareTo(o.name);
    }
}

