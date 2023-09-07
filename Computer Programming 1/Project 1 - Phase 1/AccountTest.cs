//Dylan Hayes

using System;
using System.Collections.Generic;
using System.Text;

namespace Phase_1
{
    class AccountTest
    {
        static void Main(string[] args)
        {
            Account account1 = new Account("Dylan", 1998, "1", "Savings", 1100);

            string userInput;
            int temporary;

            Console.WriteLine($"\n{account1}");

            Console.Write("\nPlease enter amount to deposit: ");
            userInput = Console.ReadLine();
            temporary = int.Parse(userInput);
            account1.Deposit(temporary);

            Console.WriteLine($"\n{account1}");

            Console.Write("\nPlease enter amount to withdraw: ");
            userInput = Console.ReadLine();
            temporary = int.Parse(userInput);
            account1.Withdraw(temporary);

            Console.WriteLine($"\n{account1}");

            Account account2 = new Account("Dylan", 1998, "1", "Checking", 5000);

            string userInput2;
            int temporary2;

            Console.WriteLine($"\n{account2}");

            Console.Write("\nPlease enter amount to deposit: ");
            userInput2 = Console.ReadLine();
            temporary2 = int.Parse(userInput2);
            account2.Deposit(temporary2);

            Console.WriteLine($"\n{account2}");

            Console.Write("\nPlease enter amount to withdraw: ");
            userInput2 = Console.ReadLine();
            temporary2 = int.Parse(userInput2);
            account2.Withdraw(temporary2);

            Console.WriteLine($"\n{account2}");
        }
    }
}
