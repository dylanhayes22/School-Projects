using System;
using System.Collections.Generic;
using System.Text;

namespace Phase_2
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
        public const double MIN_BALANCE = 50;
        public const double CHECKING_MAX = 1000;
        public const double SAVING_MAX = 500;

        public Account()
        {
            acccountType = "Checking";
            balance = 100;
        }
        public Account(string name, string yob, string num, string type, double bal)
        {
            ownerName = name;
            ownerYOB = int.Parse(yob);
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
        public string GetAccountNumber()
        {
            return acccountNumber;
        }

        public string GetAccountType()
        {
            return acccountType;
        }

        public string GetAccountDate()
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

        public void SetYOB(int year)
        {
            ownerYOB = year;
        }
        public void SetCity(string city)
        {
            branchCity = city;
        }
        public void SetAcccountNumber(string accntNum)
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
        public double Withdraw(double amnt)
        {
            double oldBalance = balance;

            if (acccountType == "Saving" && amnt > SAVING_MAX)
                return 0;
            else if (acccountType == "Checking" && amnt > CHECKING_MAX)
                return 0;
            
            if (amnt > 0)
                balance -= amnt;

            if (balance < 50)
            {
                balance = MIN_BALANCE;
                amnt = oldBalance - MIN_BALANCE;
            }


            return amnt;
        }

        public double Transfer(Account accnt, double amnt)
        {
            string account = accnt.acccountType;

            if (account == "Saving")
                if (amnt > SAVING_MAX)
                    amnt = 0;
            if (account == "Checking")
                if (amnt > CHECKING_MAX)
                    amnt = 0;
            if (balance <= MIN_BALANCE)
                amnt = 0;
            if (balance > MIN_BALANCE)
            {
                double newBalance = accnt.balance + amnt;
                accnt.balance = newBalance;

                newBalance = balance - amnt;
                balance = newBalance;
            }

            return amnt;
        }
        public override string ToString()
        {
            return "Owner: " + ownerName + "\n" + "Age: " + GetAge() + "\n" + "Address: " + GetAddress() + "\n" + "Acccunt Type: " + GetAccountType() + "\n" + "Acccunt Number: " + GetAccountNumber() + "\n" + "Balance: " + GetBalance();
        }
    }
}
