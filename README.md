### name: Kwadwo Osarfo-Akoto

# PCPARTPICKER
## Description:
This program allows users to select computer parts for building a PC showing using a databases to store different parts and their prices. The program allows users to select parts based on their preferences and budget, and overall specifications. 

## Entities:
- **User**: User will be the main way of interacting with the program in terms of adding parts to their list and and managing overall price. 
- **GPU**: Graphics Processing Unit, responsible for rendering images and video. Integral for gaming and graphic-intensive applications.
- **CPU**: Central Processing Unit, the brain of the computer that performs calculations and processes data.
- **Motherboard**: The main circuit board that connects all components of the computer, allowing communication between them.
- **RAM**: Random Access Memory, temporary storage that allows the CPU to access data quickly for running applications.
- **Storage**: Hard drives or SSDs that store the operating system, applications, and user data.
- **Power Supply**: Converts electrical power from an outlet into usable power for the computer's components.
- **Case**: The enclosure that houses all the computer components, providing protection and cooling.
- **Build**: A collection of selected parts that make up a complete PC configuration. Users can create multiple builds, each consisting of various parts.

## Tech Stack:
- **Programming Language**: Python, HTML5, SQL
- **Database**: SQLite (for storing parts and user selections)
- **GUI**: flask (for web-based interface)
- **Libraries**: 
    - sqlite3 (for database interactions)
    - SQLAlchemy
    - Flask
    - login-manager (for user authentication)
## Interactions:
**User Registration/Login**: Users can register and login to the application. this will add a new user to the database and allow them to save their builds. When a users is done, they can log out and return to the login screen.

**Build CRUD**: Users can create a new build by selecting parts from the database. Users can add multiple builds to their account and even edit parts of their builds. Along with that users can delete builds they no longer want to keep. Builds give the total cost of the entire build based on msrp to give users a rough idea of the total cost of their build.

### Use of AI:
Due to the large amount of parts and specifications, Claude and ChatGPT was used ot generate the data sets to be implemented in the database. Specifically Claude and ChatGPT was used to research and generate the data for the GPU, CPU, Motherboard, RAM, Storage, Power Supply, and Case tables. This data was then used to populate the database with realistic part information, Which otherwise would have taken extensive time to produce by hand.

## ER-Diagram:
The ER diagram below shows the relationships between the entities in the PCPicker application. The User entity is connected to the Build entity, which in turn is connected to the Parts entities. This structure allows users to have multiple builds, and each build can consist of multiple parts.
![ER Diagram](PC_PlantUML.png)

## BCNF Normalization:
the initial schema had it so where user had contained all the foreign keys to all the parts. This created a couple of problems in which the user table became redundant, along with that this format only made it possible for users to have only one build. The normalization process was done to remove the redundancy and allow users to have multiple builds. The new schema has a user table, a parts table, and a Build table in which users can have multiple builds and each build can have multiple parts.
![ER Diagram](Normalization.png)

## Relational Schema:
- user(user_id, username, email, password)
- gpu(gpu_id, name, manufacturer, gpu_brand, vram, vram_type, price, pcie, release_date)
- cpu(cpu_id, name, manufacturer, cores, threads, base_clock_speed, boost_clock_speed, socket_type, tdp, price, release_date)
- motherboard(motherboard_id, name, manufacturer, form_factor, socket_type, chipset, ram_compatibility, ram_slots, price, release_date)
- ram(ram_id, name, manufacturer, capacity, type, speed, price, release_date)
- storage(storage_id, name, manufacturer, type, capacity, speed, price, release_date)
- power_supply(psu_id, name, manufacturer, wattage, efficiency_rating, modular, price, release_date)
- case(case_id, name, manufacturer, form_factor, color, price, release_date)
- build(build_id, user_id, gpu_id, cpu_id, motherboard_id, ram_id, storage_id, psu_id, case_id, total_price, created_date)
## Installation:
install the required packages using pip:
```
pip install flask 
pip install flask_sqlalchemy
pip install flask_login
```
To run the program, got main.py and run the file. the flask server should start running on port 5000, click on the link to open the web application in your browser.

## Navigation:
when you first open the application, you will be greeted with the login screen. If you do not have an account, you can create one by clicking on the "Register" button. Once you are logged in, you will be able to see your builds and add new parts to your builds. You can also edit and delete your builds as needed. At any time users can click the home button to return to the home page. From there you can also view the list of available manufacturers.

<video src ='https://streamable.com/ag6mhq' controls width="100%" height="100%"></video>
