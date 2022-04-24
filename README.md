# StudySafe

## Sprint 1 Deliverables

| Description                      | URL                                                |
| -------------------------------- | -------------------------------------------------- |
| StudySafe Core                   | http://group-k-studysafe.herokuapp.com/Core/       |
| StudySafe Trace                  | http://group-k-studysafe.herokuapp.com/Trace/      |
| StudySafe Core API Documentation | http://group-k-studysafe.herokuapp.com/Core/APIDoc |

### StudySafe Core Example Usage

General purposes APIs:

 - list all the **campus venues**: http://group-k-studysafe.herokuapp.com/Core/venues/

 - retrieve the info on a campus venue by `venue_code`: [http://group-k-studysafe.herokuapp.com/Core/venues/<venue_code\>/]()<br>e.g. http://group-k-studysafe.herokuapp.com/Core/venues/CPD-LG.02/
   


 - list all the **HKU members**: http://group-k-studysafe.herokuapp.com/Core/members/
   


 - retrieve the info about a HKU memeber by `hkuID`: [http://group-k-studysafe.herokuapp.com/Core/members/<hkuID\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/Core/members/3030012344/

 - list all the **exit/entry record**: http://group-k-studysafe.herokuapp.com/Core/ExitEntry/

 - add **exit/entry record** of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/Core/ExitEntry/ hkuID=<hkuID> venue_code=<venue_code> datetime='20220401-09:00:00'
   ```
   
   e.g. 
   
   1. add *entry* record
   
   ```shell
   http POST http://group-k-studysafe.herokuapp.com/Core/ExitEntry/ hkuID='3030012345' venue_code='CPD-LG.02' datetime='20220401-09:00:00'
   ```
   
   2. add *exit* record
   
   ```shell
   http POST http://group-k-studysafe.herokuapp.com/Core/ExitEntry/ hkuID='3030012345' venue_code='CPD-LG.02' datetime='20220401-09:00:00'
   ```

API service paths used by *StudySafe Trace*:

 - retrieve the **close contacts** of `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): [http://group-k-studysafe.herokuapp.com/Core/members/close-contacts/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/Core/members/close-contacts/3030012345/20220411/

 - retrieve the **venues** visited by `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): 

   [http://group-k-studysafe.herokuapp.com/Core/venues/infectious-venues/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/Core/venues/infectious-venues/3030012345/20220411/

### StudySafe Trace Example Usage

 - view all the infected HKU members: http://group-k-studysafe.herokuapp.com/Trace/infected

 - view their close contacts: http://group-k-studysafe.herokuapp.com/Trace/contacts
   
 - view all the venues visited by the infectious two days before onset/diagnosis: http://group-k-studysafe.herokuapp.com/Trace/venues
   
 - view `hkuID`'s close contacts: [http://group-k-studysafe.herokuapp.com/Trace/contacts/<hkuID\>]() <br>e.g. http://group-k-studysafe.herokuapp.com/Trace/contacts/3030012348
   
 - view the venues visited by `hkuID` two days before onset/diagnosis: [http://group-k-studysafe.herokuapp.com/Trace/venues/<hkuID\>]() <br>e.g. http://group-k-studysafe.herokuapp.com/Trace/venues/3030012348
   

### API documentation

#### Visit https://group-k-studysafe.herokuapp.com/Core/APIDoc for full documentation

### Admin Access

visit http://group-k-studysafe.herokuapp.com/admin as superuser (Username: `adminse`, Password: `comp3297`)

| Repository and project root | Configuration root | App root                                                     |
| --------------------------- | ------------------ | ------------------------------------------------------------ |
| StudySafe                   | StudySafe/config   | StudySafe/users<br>StudySafe/Core (Sprint 1)<br>StudySafe/Trace (Sprint 2) |

## Run the local test server

1. After `git clone https://github.com/COMP3297-Group-K/StudySafe`, create virtual environment at the repository root, <br>

   ```shell
   pipenv --three
   ```

2. Install requirements from Pipfile.lock,

   ```shell
   pipenv install
   ```

3. Activate the virtual environment

   ``` shell
   pipenv shell
   ```

4. Run the development server

   ```shell
   python manage.py runserver
   ```

   visit http://127.0.0.1:8000/admin as superuser (Username: `adminse`, Password: `comp3297`)

#### 
