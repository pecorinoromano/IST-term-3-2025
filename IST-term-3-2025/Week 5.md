# Week 5 
## Database Setup
#### 1. what data do you want stored during the use of your app?
The data that should be stored is the reminders and the details of the reminders (such as notes, images, dates), as well as the user information (email, login, user, password, name), so that the database can pull the user information from the backend into the frontend quickly.
#### 2. what data you want displayed on your front end?
I want the reminders to display on the front end (so it's notes, images and dates), as well as the username, and maybe the user-image.
#### 3. what data is related to each other - needing keys set-up for each table
All the login data is connected - the username, email and password. The reminders are also connected - all the notes, images and dates are related to the task itself.

#### 4. what data types should be used for elements in your database (text, numeric, image etc)
The data types that need to be used for my database are images, text, dates.

#### 5. what queries might you need to write (between and across tables) allowing for good information storage and retrieval
Some queries that I would need to write are queries about the users (and their details, such as userID, password and email), as well as the reminders and the details that need to go into the reminders.

## Database Structure
For the reminders database: In the first column I have the ID number (where you can pull the ID from different reminders), then I have the title [of the reminder], the description, and the due date. All the data is written data, and numerical data for dates. <br> <img width="979" height="469" alt="image" src="https://github.com/user-attachments/assets/1011da43-067c-4b2b-bf71-919eda96454b" />

## Queries
<img width="722" height="508" alt="image" src="https://github.com/user-attachments/assets/a52173fa-d450-4ef4-aeea-f4dce3c5a4b9" /> <br> this query is used to note down the list of items that are needed to be reminded. <br> <img width="1128" height="607" alt="image" src="https://github.com/user-attachments/assets/46772769-1deb-49de-a2f9-3f4cf733f11c" /> <br> this query can be used for pulling the information for people who have logged into the website <br> <img width="913" height="445" alt="image" src="https://github.com/user-attachments/assets/3e2720fa-2bd1-49cb-9a1a-c37d4d6dd450" /> <br> this query can be used to pull different types of reminders, their ID and the date set for the reminders. <br> <img width="1153" height="525" alt="image" src="https://github.com/user-attachments/assets/d0919cfe-b82a-4457-9209-23a717c771b8" /> <br> this query is used to pull peoples information from when they sign up in the sign in page.




