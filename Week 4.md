# week 4 
## Algorithm Flowchart:
<img width="1430" height="554" alt="image" src="https://github.com/user-attachments/assets/e287cad0-b8a1-432b-8002-5bd91b7386e5" />

## Algorithm
| Data | Details |
| --------------------------------------------------------------|--------------------------------------------------------------|
| **Input** | Title [of the task], Date, Details, Images |
| **Workflow (algorithm)** | 1. Start - User adds title to the page <br>2. IF the title has already been used, THEN: <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.1 Make new title <br>&nbsp;&nbsp;&nbsp;&nbsp;ELSE full pop-up appears <br>3. *INPUT:* <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1: Date and Time <br>&nbsp;&nbsp;&nbsp;&nbsp;`SAVE DETAILS`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2: Details <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.1: Is it under 300 words? IF YES <br> &nbsp;&nbsp;&nbsp;&nbsp;`SAVE DETAILS` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.2: IF NO<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove words until <300, repeat 3.2.1 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3: Image <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.1: >5 IMAGES? IF NO <br> &nbsp;&nbsp;&nbsp;&nbsp;`SAVE DETAILS` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.2: IF YES <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove images until until <5, repeat 3.3.1 <br> 4. End (saved onto task bar)
| **Output** | IF successful: Task is successfully created, with a reminder date set, Images and Details. |

## Test case 1
| **Functionality** | **Testing** |
|------------------------|-----------------------| 
| **Test case ID** | #001 |
| **Test case name** | Setting Reminder |
| **Preconditions**  | User has to have a title, time and date. |
| **Test Steps** | 1.Add a Task title <br> 2. Add a time and date <br> 3. add details (but no more than 300) <br> 4. Add images (but no more than 5) <br> 5. save details |
| **Expected Results** | A task/reminder is set for your chosen time and date. |
| **Priority** | High priority - it is the main function of the website/app after all. |

## Test case 2
| **Functionality** | **Testing** |
|------------------------------|------------------------|
| **Test case ID** | #002 |
| **Test case name** | Adding Further Details |
| **Preconditions**  | User has to have a title, time and date. |
| **Test Steps** | 1.Add a Task title <br> 2. Add a time and date <br> 3. add details (but no more than 300) < <br> 5. save details |
| **Expected Results** | PASS: Details have been set for your reminder <br> FAIL: You have to remove words until under the word limit |
| **Priority** | High priority - It contributes to the main function of the website|

Things:
- parts of flowchart dont make sense (connect details to pictures)<br> - outputs (squares to parallelograms) <br> - risks: figure out how to add images
