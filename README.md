# StudySafe

| Repository and project root | Configuration root | App root |
| --------------------------- | ------------------ | ---------|
| StudySafe                   | StudySafe/config   | StudySafe/Core<br>StudySafe/Trace (not added yet) |

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

## Visit StudySafe Core

 - http://127.0.0.1:8000/Core/contacts/3030012345/20220411/
 - http://127.0.0.1:8000/Core/venues/3030012345/20220411/
 - http://127.0.0.1:8000/Core/exitentry/3030012345/CPD-LG.02/20220106-09:15:32/

## Visit StudySafe Trace
 - visit http://localhost:8000/Trace/infected to view the whole list of all infected members
 - visit http://localhost:8000/Trace/contacts to view the whole list of all close contacts
 - visit http://localhost:8000/Trace/venues to view the whole list of all venues visited by the infectious two days before onset/diagnosis
 - visit http://localhost:8000/Trace/contacts/<hkuID\> to view a list of `hkuID`'s close contacts
 - visit http://localhost:8000/Trace/venues/<hkuID\> to view a list of venues visited by `hkuID` two days before onset/diagnosis
