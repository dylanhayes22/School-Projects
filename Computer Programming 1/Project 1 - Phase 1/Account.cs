using System;
using System.Collections.Generic;
using System.Text;

namespace Phase_1
{
    class Account
    {
        private string ownerName;
        private string ownerAddress;
        private int ownerYOB;
        private string branchCity;
        private double balance;
        private string acccountNumber;
        private string acccountType;
        private string accountDate;

        public Account()
        {
            ownerName = "UNKNOWN";
            ownerYOB = 0;
            acccountNumber = "UNKNOWN";
            acccountType = "UNKNOWN";
            balance = 0.0;
        }
        public Account(string name, int yob, string num, string type, double bal)
        {
            ownerName = name;
            ownerYOB = yob;
            acccountNumber = num;
            acccountType = type;
            balance = bal;
        }
        //Getters
        public string GetName()
        {
            return ownerName;
        }

        public string GetAddress()
        {
            return ownerAddress;
        }
        public int GetAge()
        {
            return 2022 - ownerYOB;
        }
        public string GetCity()
        {
            return branchCity;
        }
        public double GetBalance()
        {
            return balance;
        }
        public string getAccountNumber()
        {
            return acccountNumber;
        }

        public string getAccountType()
        {
            return acccountType;
        }

        public string getAccountDate()
        {
            return accountDate;
        }

        //Setters
        public void SetName(string name)
        {
            ownerName = name;
        }

        public void SetAddress(string address)
        {
            ownerAddress = address;
        }

        public void setYOB(int year)
        {
            ownerYOB = year;
        }
        public void SetCity(string city)
        {
            branchCity = city;
        }
        public void SetAccountNumber(string accntNum)
        {
            acccountNumber = accntNum;
        }
        public void SetAccountType(string accntType)
        {
            acccountType = accntType;
        }
        public void SetAccountDate(string accntDate)
        {
            accountDate = accntDate;
        }
        public void Deposit(double amnt)
        {
            balance += amnt;
        }
        public void Withdraw(double amnt)
        {
            balance -= amnt;
        }

        public override string ToString()
        {
            return ownerName + " " + "born in " + GetAge() + "." + "\nAccount Type: " + acccountType + "\nCurrent Balance: " + balance;
        }
    }
}
