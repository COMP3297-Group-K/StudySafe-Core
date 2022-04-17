# StudySafe

==Modified on April 17, 2022 for sprint 1 delivery.==

visit http://group-k-studysafe.herokuapp.com/admin as superuser (Username: `adminse`, Password: `comp3297`)

| Repository and project root | Configuration root | App root                                                     |
| --------------------------- | ------------------ | ------------------------------------------------------------ |
| StudySafe                   | StudySafe/config   | StudySafe/users<br>StudySafe/Core (Sprint 1)<br>StudySafe/Trace (Sprint 2) |

## Run the local test server

1. After `git clone <URL>`, create virtual environment at the repository root, <br>

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
   

## API documentation

<!--- ==Visit http://127.0.0.1:8000/Core/APIDoc for full documentation== --->

==Visit https://group-k-studysafe.herokuapp.com/Core/APIDoc for full documentation==

#### StudySafe Core (API)

General purpose APIs:

 - list all the campus venues

  <!--- http://127.0.0.1:8000/Core/venues/ --->

  http://group-k-studysafe.herokuapp.com/Core/venues/

 - retrieve campus venue `pk`
    
  <!--- [http://127.0.0.1:8000/Core/venues/<pk\>/](), e.g. http://127.0.0.1:8000/Core/venues/CPD-LG.02/ --->
  
  [http://group-k-studysafe.herokuapp.com/Core/venues/<pk\>/](), e.g. http://group-k-studysafe.herokuapp.com/Core/venues/CPD-LG.02/


 - list all the HKU members
   
   <!--- http://127.0.0.1:8000/Core/members/ --->
   
   http://group-k-studysafe.herokuapp.com/Core/members/


 - retrieve HKU memebr `pk`

   <!--- [http://127.0.0.1:8000/Core/members/<pk\>/](), e.g. http://127.0.0.1:8000/Core/members/3030012344/ --->

   [http://group-k-studysafe.herokuapp.com/Core/members/<pk\>/](), e.g. http://group-k-studysafe.herokuapp.com/Core/members/3030012344/


APIs associated with StudySafe Trace:

 - retrieve the close contacts of `hkuID` whose onset/diagnose data is `date` (YYYYMMDD)
   
   <!--- [http://127.0.0.1:8000/Core/members/close-contacts/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/members/close-contacts/3030012345/20220411/ --->
   
   [http://group-k-studysafe.herokuapp.com/Core/members/close-contacts/<hkuID\>/<date\>/](), e.g. http://group-k-studysafe.herokuapp.com/Core/members/close-contacts/3030012345/20220411/
   
 - retrieve the venues visited by `hkuID` whose onset/diagnose data is `date` (YYYYMMDD)
   
   <!--- [http://127.0.0.1:8000/Core/venues/infectious-venues/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/venues/infectious-venues/3030012345/20220411/ --->
   
   [http://group-k-studysafe.herokuapp.com/Core/venues/infectious-venues/<hkuID\>/<date\>/](), e.g. http://group-k-studysafe.herokuapp.com/Core/venues/infectious-venues/3030012345/20220411/
   
 - add exit/entry record of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)
   
   <!--- [http://127.0.0.1:8000/Core/ExitEntry/<hkuID\>/<venue\>/<datetime\>/](), e.g. --->
   
   <!--- (1. add entry record)http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220401-09:00:00/ --->
   
   <!--- (2. add exit record)http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220401-19:00:00/ --->
   
   [http://group-k-studysafe.herokuapp.com/Core/ExitEntry/<hkuID\>/<venue\>/<datetime\>/](), e.g. 
   
   (1. add *entry* record)http://group-k-studysafe.herokuapp.com/Core/ExitEntry/3030012345/CPD-LG.02/20220401-09:00:00/
   
   (2. add *exit* record)http://group-k-studysafe.herokuapp.com/Core/ExitEntry/3030012345/CPD-LG.02/20220401-19:00:00/

#### StudySafe Trace
 - view all the infected HKU members

   <!--- http://localhost:8000/Trace/infected --->

   http://group-k-studysafe.herokuapp.com/Trace/infected

 - view their close contacts
   
   <!--- http://localhost:8000/Trace/contacts -->
   
   http://group-k-studysafe.herokuapp.com/Trace/contacts
   
 - view all the venues visited by the infectious two days before onset/diagnosis
   
   <!--- http://localhost:8000/Trace/venues --->
   
   http://group-k-studysafe.herokuapp.com/Trace/venues
   
 - view `hkuID`'s close contacts
   
   <!--- [http://localhost:8000/Trace/contacts/<hkuID\>](), e.g. http://localhost:8000/Trace/contacts/3030012348 --->
   
   [http://group-k-studysafe.herokuapp.com/Trace/contacts/<hkuID\>](), e.g. http://group-k-studysafe.herokuapp.com/Trace/contacts/3030012348
   
 - view the venues visited by `hkuID` two days before onset/diagnosis
   
   <!--- [http://localhost:8000/Trace/venues/<hkuID\>](), e.g. http://localhost:8000/Trace/venues/3030012348 --->
   
   [http://group-k-studysafe.herokuapp.com/Trace/venues/<hkuID\>](), e.g. http://group-k-studysafe.herokuapp.com/Trace/venues/3030012348
