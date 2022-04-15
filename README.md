# StudySafe

<<<<<<< HEAD
| Repository and project root | Configuration root | App root                          |
| --------------------------- | ------------------ | --------------------------------- |
| StudySafe                   | StudySafe/config   | StudySafe/Core<br>StudySafe/Trace |
=======
| Repository and project root | Configuration root | App root                                             |
| --------------------------- | ------------------ | ---------------------------------------------------- |
| StudySafe                   | StudySafe/config   | StudySafe/users<br>StudySafe/Core<br>StudySafe/Trace |
>>>>>>> a11f86634b70b60c29a5d4a0b316715e237d8068

## Run the server

1. After `git clone <URL>`, create virtual environment at the repository root, <br>(shell commands on **MacOS**, replace `python3` with `py` on **Windows**)

   ```shell
   python3 -m pipenv --three
   ```

2. Install requirements from Pipfile.lock,

   ```shell
   python3 -m pipenv install
   ```

3. Activate the virtual environment

   ``` shell
   python3 -m pipenv shell
   ```

4. Run the development server

   ```shell
   python3 manage.py runserver
   ```

   visit http://127.0.0.1:8000/admin as superuser (Username: `adminse`, Password: `comp3297`)

## StudySafe Core (API)

General purpose APIs:

 - list all the campus venues
<<<<<<< HEAD
   - visit http://127.0.0.1:8000/Core/venues

 - retrieve campus venue `pk`
   - [http://127.0.0.1:8000/Core/venues/<pk\>](), e.g. http://127.0.0.1:8000/Core/venues/1
=======
   - visit http://127.0.0.1:8000/Core/venues/

 - retrieve campus venue `pk`
   - [http://127.0.0.1:8000/Core/venues/<pk\>/](), e.g. http://127.0.0.1:8000/Core/venues/CPD-LG.02/
>>>>>>> a11f86634b70b60c29a5d4a0b316715e237d8068

 - list all the HKU members
   - visit http://127.0.0.1:8000/Core/members/

 - retrieve HKU memebr `pk`
<<<<<<< HEAD
   - [http://127.0.0.1:8000/Core/members/<pk\>](), e.g. http://127.0.0.1:8000/Core/members/1
=======
   - [http://127.0.0.1:8000/Core/members/<pk\>/](), e.g. http://127.0.0.1:8000/Core/members/3030012344/
>>>>>>> a11f86634b70b60c29a5d4a0b316715e237d8068


APIs associated with StudySafe Trace:

 - retrieve the close contacts of `hkuID` whose onset/diagnose data is `date` (YYYYMMDD)
<<<<<<< HEAD
   - visit [http://127.0.0.1:8000/Core/ContactMember/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/ContactMember/3030012345/20220411/
 - retrieve the venues visited by `hkuID` whose onset/diagnose data is `date` (YYYYMMDD)
   - [http://127.0.0.1:8000/Core/ContactVenue/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/ContactVenue/3030012345/20220411/
 - add exit/entry record of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)
   - [http://127.0.0.1:8000/Core/ExitEntry/<hkuID\>/<venue\>/<datetime\>/](), e.g. http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220106-09:15:32/
=======
   - visit [http://127.0.0.1:8000/Core/members/close-contacts/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/members/close-contacts/3030012345/20220411/
   
 - retrieve the venues visited by `hkuID` whose onset/diagnose data is `date` (YYYYMMDD)
   - [http://127.0.0.1:8000/Core/venues/infectious-venues/<hkuID\>/<date\>/](), e.g. http://127.0.0.1:8000/Core/venues/infectious-venues/3030012345/20220411/
   
 - add exit/entry record of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)
   - [http://127.0.0.1:8000/Core/ExitEntry/<hkuID\>/<venue\>/<datetime\>/](), e.g. 
   
     (1)http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220401-09:00:00/
   
     (2)http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220401-19:00:00/
>>>>>>> a11f86634b70b60c29a5d4a0b316715e237d8068

## StudySafe Trace
 - view the whole list of all infected members
   - visit http://localhost:8000/Trace/infected
 - view the whole list of all close contacts
   - visit http://localhost:8000/Trace/contacts
 - view the whole list of all venues visited by the infectious two days before onset/diagnosis
   - visit http://localhost:8000/Trace/venues
 - view a list of `hkuID`'s close contacts
   - visit [http://localhost:8000/Trace/contacts/<hkuID\>](), e.g. http://localhost:8000/Trace/contacts/3030012348
 - view a list of venues visited by `hkuID` two days before onset/diagnosis
   - visit [http://localhost:8000/Trace/venues/<hkuID\>](), e.g. http://localhost:8000/Trace/venues/3030012348
