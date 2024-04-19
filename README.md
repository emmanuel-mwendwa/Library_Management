## Library Management System

This Library Management System is a robust tool built with the Frappe Framework, designed to manage the operations of a library, including handling articles[books], members, memberships, and transactions. 
This system is ideal for librarians looking to digitize their library's functions and enhance user interaction.

## Features
The Library Management System includes the following features:

 - **Article Management:** Allows librarians to create, update, and manage articles
 - **Member & Membership Management:** Facilitates the creation and management of library members and memberships
 - **Transaction Handling:** Enables the issuance and return of articles, tracking each transaction within the library.
 - **Settings Configuration:** Provides a customizable setup through the Library Setting DocType to cater to different library needs. The loan period and maximum articles issuance

## DocTypes

The system comprises several DocTypes, each serving a specific funcition:
- **Article:** Represents books
- **Library Member:** Stores information about library users.
- **Library Membership:** Manages memberships for active or inactive members to allow issuance of articles
- **Library Transaction:** Handles the issuance and return of articles[books]
- **Library Setting:** Maximum articles can be issued and maximum loan period

## Installation

### Prerequisites
- Frappe Framework [Frappe Framework Installationn](https://github.com/D-codE-Hub/Frappe-ERPNext-Version-15--in-Ubuntu-22.04-LTS/blob/main/README.md)
- MacOs or Linux

  ### Setting up the Library Management System

  1. Clone the repository:
     ```
     https://github.com/emmanuel-mwendwa/Library_Management.git
     cd Library_Management
     ```
     
  2. Install the app onto your Frappe site:
     ```
     bench get-app library_management https://github.com/emmanuel-mwendwa/Library_Management.git
     bench --site library_management install-app library_management_system
     ```

  4. Migrate your site to apply any doctype changes and start using the application:
     ```
     bench --site library_management migrate
     ```


## Usage

### Managing Articles

1. **Creating a New Article:**
    - Go to the Article list, click on "New Article", and enter the details of the article.
    
2. **Updating an Article:**
    - Open the existing Article from the list and make the necessary changes.
    
### Managing Memberships

1. **Adding a New Member:**
    - Navigate to the Library Member list, click on "New Library Member", and fill in the member details.
    
2. **Creating Memberships:**
    - Access the Library Membership list, click on "New Library Membership", and specify the membership details.

### Handling Transactions

1. **Issuing an Article:**
    - In the Library Transaction DocType, create a new record, set the status to 'Issued' and select the member and the article.

2. **Returning an Article:**
    -Update the status of the transaction record to 'Returned'.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more information.
