import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.Iterator;

public class AppDriver {
    private JTextField textField1;
    private JTextField textField2;
    private JTextField textField3;
    private JPanel mainPanel;
    private JPanel entryPanel;
    private JLabel label1;
    private JLabel label2;
    private JLabel label3;
    private JButton addContactButton;
    private JButton removeContactButton;
    private JButton modifyContactButton;
    private JButton contactInformationButton;
    private JButton resetEntriesButton;
    private JButton resetDisplayPanelButton;
    private JButton printEntirePhoneBookButton;
    private JPanel File;
    private JButton savePhoneBookToFileButton;
    private JButton openOldPhoneBookButton;
    private JTextArea textArea1;

    BinarySearchTree<Person> phoneBook = new BinarySearchTree<>(); // create new BST

    public AppDriver() {
        //  addContactButton is added to contact listener
        addContactButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // textField1, textField2, and textField3 are used to recieve text from input
                String firstName = textField1.getText();
                String lastName = textField2.getText();
                String phone = textField3.getText();
                // With the input information create a new person object
                Person person = new Person(firstName, lastName, phone);
                // use bst phonebook to add bst
                phoneBook.add(person);
                // Append the Person's information to the textArea1
                textArea1.setText(textArea1.getText() + "\n" + person);
            }
        });
        // Add an action listener to the "Remove Contact" button
        removeContactButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Retrieve the name input from the text field
                String name = textField3.getText();
                // Create a new person object with the input name
                Person person = new Person(name, "", "");
                // Remove the person from the phone book binary search tree
                phoneBook.remove(person);
                // Clear the text area where the phone book contents are displayed
                textArea1.setText("");
                // Create an iterator to loop through the phone book contents
                Iterator<Person> itr = phoneBook.iterator();
                // Iterate through the phone book and display each person's information in the text area
                while (itr.hasNext()) {
                    textArea1.setText(textArea1.getText() + "\n" + itr.next());
                }
            }
        });

// Add an action listener to the "Reset Entries" button
        resetEntriesButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Clear the text fields for name, address and phone number
                textField1.setText("");
                textField2.setText("");
                textField3.setText("");
            }
        });

// Add an action listener to the "Reset Display Panel" button
        resetDisplayPanelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Clear the text area where the phone book contents are displayed
                textArea1.setText("");
            }
        });

// Add an action listener to the "Modify Contact" button
        modifyContactButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Retrieve the name input from the text field
                String name = textField3.getText();
                // Create an iterator to loop through the phone book contents
                Iterator<Person> itr = phoneBook.iterator();
                // Iterate through the phone book contents
                while (itr.hasNext()) {
                    // Retrieve the next person object
                    Person p = itr.next();
                    // Check if the person's name matches the input name
                    if (p.getName().equals(name)) {
                        // Retrieve the updated address and phone number from the respective text fields
                        String str1 = textField1.getText();
                        String str2 = textField2.getText();
                        // Update the person's address and phone number
                        p.setAddress(str1);
                        p.setPhone(str2);
                        // Display the updated information in the text area
                        textArea1.setText(textArea1.getText() + "\n" + p);
                    }
                }
            }
        });

// Add an action listener to the "Display Contact Information" button
        contactInformationButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Retrieve the name input from the text field
                String name = textField3.getText();
                // Create an iterator to loop through the phone book contents
                Iterator<Person> itr = phoneBook.iterator();
                // Iterate through the phone book contents
                while (itr.hasNext()) {
                    // Retrieve the next person object
                    Person p = itr.next();
                    // Check if the person's name matches the input name
                    if (p.getName().equals(name)) {
                        // Display the person's information in the text area
                        textArea1.setText(String.valueOf(p));
                    }
                }
            }
        });

// Add an action listener to the "Print Entire Phone Book" button
        printEntirePhoneBookButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Create an iterator to loop through the phone book contents
                Iterator<Person> itr = phoneBook.iterator();
                // Iterate through the phone book contents
                while (itr.hasNext()) {
                    textArea1.setText(textArea1.getText() + "\n" + itr.next()); // Print out all information in the BST
                }
            }
        });
        // Create a button listener for the "Open Old Phone Book" button that reads a phone book object from a file
        openOldPhoneBookButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Open an input stream from the file
                    FileInputStream inStream = new FileInputStream("PhoneBookINFO.dat");
                    // Create an object input stream to read the phone book object from the file
                    ObjectInputStream objInput = new ObjectInputStream(inStream);
                    // Read the phone book object from the file and cast it to the appropriate type
                    phoneBook = (BinarySearchTree<Person>) objInput.readObject();
                    // Close the object input stream
                    objInput.close();
                    // Close the input stream
                    inStream.close();
                } catch (IOException j) {
                    // Print the exception message if an I/O error occurs
                    System.out.println(j.getMessage());
                } catch (ClassNotFoundException j) {
                    // Print the exception message if the class of the serialized object cannot be found
                    System.out.println(j.getMessage());
                }
            }
        });

    }

    // Create and display the GUI on the main thread
    public static void main(String[] args) {
        JFrame frame = new JFrame("CWU 302 Phonebook Anish Ghimire");
        frame.setContentPane(new AppDriver().mainPanel);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
