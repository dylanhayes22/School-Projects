//Dylan Hayes

using System;
using System.Collections.Generic;
using System.Text;

namespace Phase_3
{
    class AccountTest
    {
        private static void Main()
        {
            Account[] BankAccounts = new Account[5];
            int userInt = 0;
            int index = 0;
            while (userInt != 7)
            {
                Console.WriteLine(" ================================== ");
                Console.WriteLine("Welcome to ABC bank... ");
                Console.WriteLine("1. Open a new account.");
                Console.WriteLine("2. Withdraw.");
                Console.WriteLine("3. Deposit.");
                Console.WriteLine("4. Transfer.");
                Console.WriteLine("5. Print info of a given account.");
                Console.WriteLine("6. Show how many accounts left.");
                Console.WriteLine("7. Exit.");
                Console.WriteLine(" ================================== ");
                while (true)
                {
                    Console.Write("Please choose a number from above: ");
                    if (int.TryParse(Console.ReadLine(), out userInt) && ((userInt >= 1) && (userInt <= 7)))
                    {
                        switch (userInt)
                        {
                            case 1:
                                if (index >= BankAccounts.Length)
                                {
                                    Console.WriteLine("Sorry..the maximum number of accounts is reached.");
                                }
                                else
                                {
                                    Console.Write("Enter the name: ");
                                    string ownerName = Console.ReadLine();
                                    while (true)
                                    {
                                        int year;
                                        Console.Write("Enter the year of birth (must be 18 to 100 years old by 2022): ");
                                        if (int.TryParse(Console.ReadLine(), out year) && ((year >= 1922) && ((2022 - year) >= 18)))
                                        {
                                            Console.Write("Enter account number: ");
                                            string acccountNumber = Console.ReadLine();
                                            while (true)
                                            {
                                                Console.Write("Enter account type (Checking or Saving): ");
                                                string acccountType = Console.ReadLine();
                                                if ((acccountType == "Checking") || (acccountType == "checking" || (acccountType == "Saving") || (acccountType == "saving")))
                                                {
                                                    while (true)
                                                    {
                                                        double newBalance;
                                                        Console.Write("Enter initial balance (must be 50 or more): ");
                                                        if (double.TryParse(Console.ReadLine(), out newBalance) && (newBalance >= 50.0))
                                                        {
                                                            BankAccounts[index] = new Account(ownerName, year, acccountNumber, acccountType, newBalance);
                                                            index++;
                                                            Console.WriteLine("Opened successfully!");
                                                            break;
                                                        }
                                                    }
                                                    break;
                                                }
                                            }
                                            break;
                                        }
                                    }
                                }
                                break;

                            case 2:
                                if (index <= 0)
                                {
                                    Console.WriteLine("No accounts yet!");
                                }
                                else
                                {
                                    Console.Write("Enter account number to withdraw from: ");
                                    int accountWithdraw = searchAccounts(BankAccounts, Console.ReadLine(), index);
                                    if (accountWithdraw == -1)
                                    {
                                        Console.WriteLine("The account was not found!");
                                    }
                                    else
                                    {
                                        double withdrawAmount;
                                        Console.Write("How much would you like to withdraw? ");
                                        double.TryParse(Console.ReadLine(), out withdrawAmount);
                                        double num = BankAccounts[accountWithdraw].Withdraw(withdrawAmount);
                                        if (num > 0.0)
                                        {
                                            Console.WriteLine($"Successful! {(double)num:C} withdrawn.");
                                        }
                                        else
                                        {
                                            Console.WriteLine("Not Successful!");
                                        }
                                    }
                                }
                                break;

                            case 3:
                                if (index <= 0)
                                {
                                    Console.WriteLine("No accounts yet!");
                                }
                                else
                                {
                                    Console.Write("Enter account number to deposit to: ");
                                    int accountDeposit = searchAccounts(BankAccounts, Console.ReadLine(), index);
                                    if (accountDeposit == -1)
                                    {
                                        Console.WriteLine("The account was not found!");
                                    }
                                    else
                                    {
                                        double depositAmount;
                                        Console.Write("How much would you like to deposit? ");
                                        double.TryParse(Console.ReadLine(), out depositAmount);
                                        if (depositAmount <= 0.0)
                                        {
                                            Console.WriteLine("Nothing was deposited!");
                                        }
                                        else
                                        {
                                            BankAccounts[accountDeposit].Deposit(depositAmount);
                                            Console.WriteLine($"{(double)depositAmount:C} was deposited!");
                                        }
                                    }
                                }
                                break;

                            case 4:
                                if (index <= 0)
                                {
                                    Console.WriteLine("No accounts yet!");
                                }
                                else
                                {
                                    Console.Write("Current accounts: ");
                                    int amountAccounts = 0;
                                    while (true)
                                    {
                                        if (amountAccounts >= index)
                                        {
                                            Console.WriteLine(" ");
                                            Console.Write("Enter the number of the account to transfer from: ");
                                            int num2 = searchAccounts(BankAccounts, Console.ReadLine(), index);
                                            Console.Write("Enter the number of the account to transfer to: ");
                                            int num3 = searchAccounts(BankAccounts, Console.ReadLine(), index);
                                            if ((num2 == -1) || (num3 == -1))
                                            {
                                                Console.WriteLine("One or both of the accounts were not found!");
                                            }
                                            else
                                            {
                                                double transferAmount;
                                                Console.Write("How much would you like to transfer? ");
                                                double.TryParse(Console.ReadLine(), out transferAmount);
                                                double transferAmount2 = BankAccounts[num2].Transfer(BankAccounts[num3], transferAmount);
                                                if (transferAmount2 > 0.0)
                                                {
                                                    Console.WriteLine($"Successful! {(double)transferAmount2:C} was tranferred.");
                                                }
                                                else
                                                {
                                                    Console.WriteLine("Unsuccessful!");
                                                }
                                            }
                                            break;
                                        }
                                        Console.Write(BankAccounts[amountAccounts++].GetAccountNumber() + "\t");
                                    }
                                }
                                break;

                            case 5:
                                if (index <= 0)
                                {
                                    Console.WriteLine("No accounts were created/opened yet!");
                                }
                                else
                                {
                                    Console.Write("Current accounts: ");
                                    int currentAccounts = 0;
                                    while (true)
                                    {
                                        if (currentAccounts >= index)
                                        {
                                            Console.WriteLine();
                                            while (true)
                                            {
                                                Console.Write("Enter account number to print info: ");
                                                string accountInfo = Console.ReadLine();
                                                int num4 = searchAccounts(BankAccounts, accountInfo, index);
                                                if (num4 != -1)
                                                {
                                                    Console.WriteLine(BankAccounts[num4]);
                                                    break;
                                                }
                                            }
                                            break;
                                        }
                                        Console.Write(BankAccounts[currentAccounts++].GetAccountNumber() + "\t");
                                    }
                                }
                                break;

                            case 6:
                                Console.WriteLine($"You can create/open {(int)(BankAccounts.Length - index)} more accounts.");
                                break;

                            default:
                                break;
                        }
                        if (userInt != 7)
                        {
                            Console.WriteLine("Press any key to return to main menu.");
                            Console.ReadLine();
                            Console.Clear();
                        }
                        break;
                    }
                }
            }
        }
        private static int searchAccounts(Account[] BankAccounts, int numberAccount, string accountInfo, )
        {
            for (int i = 0; i < numberAccount; i++)
            {
                if (BankAccounts[i].GetAccountNumber() == accountInfo)
                {
                    return i;
                }
            }
            return -1;
        }


    }
}