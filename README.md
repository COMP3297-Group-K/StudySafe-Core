# StudySafe

| Repository and project root | Configuration root | App root |
| --------------------------- | ------------------ | ---------|
| StudySafe                   | StudySafe/config   | StudySafe/Core<br>StudySafe/Trace (not added yet) |

1. After `git clone <URL>`, create virtual environment at the repository root (shell commands on **MacOS**, replace `python3` with `py` on **Windows**),

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
