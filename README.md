# Know Your Customer (KYC) on Blockchain



## Introduction

The objective of this project is to explore the possibilities of integrating blockchain into Anti-Money Laundering (AML) practices. We have used Solidity to create a smart contract to input and update information on the blockchain for the purpose of streamlining the Know Your Customer (KYC) process.

AML refers to the global laws, regulations, and procedures that are in place to prevent the act of producing income through illegal activities. The issue with the current AML procedures is that they are not able to keep pace with the evolving complexity and volume of financial transactions, which becomes a problem for keeping a check on money-laundering activities.

KYC is a component of AML; it involves certain details that businesses keep as an end criterion for the identification of customers who are interested in doing business with them. Some predominant issues faced by current KYC compliance include corruption, terrorist financing, identity theft, and illegal tax avoidance.

According to a study, the annual AML compliance costs for the United States and Canadian financial institutions totaled $31.5 billion USD.

## How Can Blockchain Help?

Blockchain technology allows for the creation of a distributed ledger that is then shared with all users on the network. Utilizing Blockchain as a distributed ledger system has the potential to unlock the advantages of automated processes such as reducing compliance errors. A blockchain-based registry would not only remove the repetitive efforts of implementing KYC checks but also enable encrypted updates to client accounts to be distributed in near real-time.

A KYC utility system based on blockchain technology will enable the financial and banking sectors to emancipate the process of identity verification. Currently, our data is collected and stored in a centralized system, such as a repository. With the introduction of blockchain solutions to handle the KYC process, data will be available on a decentralized network and can, therefore, be accessed by third parties directly after permission has been given.

This blockchain-based KYC system will also offer better data security by ensuring that data access is only made after confirmation or permission is received from the relevant authority. This will eliminate the chance of unauthorized access and subsequently give individuals greater control over their data.

This ledger will provide a historical record of all documents shared and compliance activities undertaken for each client. Blockchain technology is also helpful in identifying entities attempting to create fraudulent histories. Within the provisions of data protection regulation, the data in the blockchain is immutable and could be analyzed to identify irregularities - directly targeting criminal activity.

![Blockchain method](Images/Blockchain_KYC.jpg)

## Building the KYC System

The KYC System is built using a command-line interface that uploads and pins KYC reports to IPFS via Pinata, permanently storing them on-chain by using the register KYC function in the KYC smart contract. The cost of gas for creating the KYC report will be borne by the client.

1. A smart contract kyccontract.sol is created with the msg.sender as the contract administrator. Using a struct, we created a client object stored in a mapping called clientdatabase. Each client is mapped to an address called userID.

    The following functions make up the contract:

    * registerKYC: Uploads customer information into the kyc contract with userID as the address and report_uri containing the details of the customer account. Simultaneously, the client is added to a list used to track KYC expiry dates. A check for duplicate records is also part of this function.

    * updateKYC: Updates any changes to an existing client record by adding a new report_uri containing the updated information.

    * checkvalidity: Tracks the validity of a customer report. The KYC report for customers is valid for up to 365 days.

    * clientLoop: Iterates over the list of clients and pulls out reports that are about to expire in the next 30 days. A log is generated for the administrator (i.e., the msg.sender) to follow up with customers to update their KYC information.
        
2. This contract is deployed in Remix IDE. 

3. A new KYC_frontend directory is created where a .env file is stored with Pinata API Key, Secret API Key, the address of the deployed smart contract, and the WEB3 provider URI.

4. The deployed kyccontract.sol contract ABI is copied and stored in a kyc.json file.

5. A Python file kyc.py is created. In this file:

   * Import web3.auto, load the environment variables using dotenv, and import the Path library from pathlib to fetch the ABI.

   * A headers object to populate the variables defined in .env.

   * An initContract function that returns the Web3 contract object to interact with the KYC contract on-chain.

   * A convertDataToJSON function to convert customer data to JSON format.
   
   * A pinJSONtoIPFS function with a POST request to the PinJSONtoIPFS endpoint on Pinata. 

6. Another file called kycreport.py is created. In this file:

    * Import the kyc.py functions.

    * A kyccontract object is created using the initContract function from kyc.py.

    * In the createkycReport function, user data is fetched using the input function in Python. 

    * Pass the user data variables to the convertDataToJSON function. Store the result in json_data, then pass json_data to the pinJSONtoIPFS function and save it as report_uri. Return the user_id, email, and report_uri variables.

    * In the kycreport function, generate the transaction that interacts with the KYC smart contract and return the transaction receipt. 

    * A kycupdate function interacts with the update function in the KYC smart contract to update records and return the transaction receipt.

    * A main function puts the pieces together. In the report flow, create the KYC report, store the receipt, and print the results. A similar update flow creates a report with updated information and prints the receipt.
    
## Launching the KYC System

1. Create a Pinata account and get your Pinata API keys.
​2. Create an Ethereum environment using Anaconda prompt.
​3. Go to the repository where kyc.py and kycreport files are stored.
​4. Deploy the kyccontract.sol in Remix IDE.
​5. Inside the KYC_frontend folder, create a .env file and copy the Pinata API Key, Secret API Key, the address of the deployed smart contract, and the WEB3 provider URI.
6. Use the command-line interface to create your records using the following steps:
​
   * Launch your Ethereum environment.
​   * Navigate to the KYC_frontend directory.
​   * Run the following commands:

      * python kycreport.py report (to create a new report)
      * python kycreport.py update (to update a record)

   * Complete the prompts to create your KYC report and register the client.
   * This should return an IPFS hash of the report URI and a transaction receipt.

## Technologies Used

- Solidity
- Remix IDE
- Python
- Ganache
- Metamask
- Pinata API

## Limitations

1. The clientLoop function is stored on the chain and therefore uses gas every time the administrator pulls up a list of expiring reports. This could become costly with a growing database. A mapping may be more gas-efficient for managing this function depending on the number of expected users.

2. The checkvalidity function does not work well in the test environment. Unlike the main net, where there is constant activity and real-time transactions, the test net records time only during transactions. This creates challenges when calculating elapsed time.

3. The end date for each report is stored as a timestamp on the blockchain. A function could be written to convert this into human-readable form.

## Conclusion

Blockchain-based KYC utilities will help reduce costs for any industry reliant on identity verification by enabling secure, organized, and unified data handling.

#

