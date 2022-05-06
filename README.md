# StudySafe (Group K)

| Description                      | URL                                                 |
| -------------------------------- | --------------------------------------------------- |
| StudySafe Core                   | http://group-k-studysafe.herokuapp.com/core/        |
| StudySafe Core API Documentation | http://group-k-studysafe.herokuapp.com/core/apidoc/ |

| Repository and project root                                  | Configuration root    | App root                                     |
| ------------------------------------------------------------ | --------------------- | -------------------------------------------- |
| [StudySafe-Core](https://github.com/COMP3297-Group-K/StudySafe-Core) | StudySafe-Core/config | StudySafe-Core/users<br/>StudySafe-Core/Core |

### StudySafe Core Example Usage

General purposes APIs:

#### 1. Campus Venues

| Method                                        | URL                                                          |
| --------------------------------------------- | ------------------------------------------------------------ |
| list all the venues                           | http://group-k-studysafe.herokuapp.com/core/venues/          |
| retrieve venue by `venue_code`                | http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/<br/>e.g. http://group-k-studysafe.herokuapp.com/core/venues/KK101/ |
|                                               | **Command Line**                                             |
| update venue info<br> **(CML ONLY)**          | http PUT http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/ venue_code=<venue_code> location=<new_location> type=<new_type> capacity=<new_capacity> <br> e.g. `http PUT http://group-k-studysafe.herokuapp.com/core/venues/KK101/ venue_code=KK101 location=newloc type=newtype capacity=20` |
| partial update venue info<br/> **(CML ONLY)** | http PATCH http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/ location=<new_location> or type=<new_type> or capacity=<new_capacity> <br/> e.g. `http PATCH http://group-k-studysafe.herokuapp.com/core/venues/KK101/ capacity=20` |
| create venue<br/> **(CML ONLY)**              | http POST  http://group-k-studysafe.herokuapp.com/core/venues/ venue_code=<venue_code> location=<new_location> type=<new_type> capacity=<new_capacity> <br/> e.g. `http POST http://group-k-studysafe.herokuapp.com/core/venues/ venue_code=KK102 location=K.K.\ Leung\ Building,\ Main\ Campus type=LT capacity=100` |
| delete venue<br/> **(CML ONLY)**              | http DELETE  http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/  <br/> e.g. `http DELETE http://group-k-studysafe.herokuapp.com/core/venues/KK102/` |
| list all the venues                           | `http GET http://group-k-studysafe.herokuapp.com/core/venues/` |
| retrieve venue by `venue_code`                | http GET http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/<br/>e.g. `http GET http://group-k-studysafe.herokuapp.com/core/venues/KK101/` |

#### 2. HKU Members

| Method                                        | URL                                                          |
| --------------------------------------------- | ------------------------------------------------------------ |
| list all the HKU members                      | http://group-k-studysafe.herokuapp.com/core/members/         |
| retrieve HKU member by `hkuID`                | [http://group-k-studysafe.herokuapp.com/core/members/<hkuID\>/]() <br/>e.g. http://group-k-studysafe.herokuapp.com/core/members/3025704501/ |
|                                               | **Command Line**                                             |
| update venue info<br> **(CML ONLY)**          | http PUT [http://group-k-studysafe.herokuapp.com/core/members/<hkuID\>/]() hkuID=<hku_ID> name=<name> <br> e.g. ` http PUT http://group-k-studysafe.herokuapp.com/core/members/29705/ hkuID=29705 name=Cheung,\ Ka\ Fai ` |
| partial update venue info<br/> **(CML ONLY)** | http PATCH [http://group-k-studysafe.herokuapp.com/core/members/<hkuID\>/]() name=<name> <br/> e.g. `http PATCH http://group-k-studysafe.herokuapp.com/core/members/29705/ name=Cheung,\ Ka\ Fai` |
| create venue<br/> **(CML ONLY)**              | http POST [http://group-k-studysafe.herokuapp.com/core/members/]() hkuID=<hku_ID> name=<name> <br/> e.g. `http POST http://group-k-studysafe.herokuapp.com/core/members/ hkuID=123456 name=Random\ Guy` |
| delete venue<br/> **(CML ONLY)**              | http DELETE  [http://group-k-studysafe.herokuapp.com/core/members/]()<hkuID\>/  <br/> e.g. `http DELETE http://group-k-studysafe.herokuapp.com/core/members/123456/` |
| list all the venues                           | `http GET http://group-k-studysafe.herokuapp.com/core/members/` |
| retrieve venue by `venue_code`                | http GET [http://group-k-studysafe.herokuapp.com/core/members/]() <hkuID\>/ <br/>e.g. `http GET http://group-k-studysafe.herokuapp.com/core/members/29705/` |

#### 3. Exit Entry Record


 - add **exit/entry record** of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/exitentry/ hkuID=<hkuID> venue_code=<venue_code> datetime='20220401-09:00:00'
   ```

   e.g. 

   1. add *entry* record

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/exitentry/ hkuID='3025704501' venue_code='CPD-2.58' datetime='20220502-15:32:00'
   ```

   2. add *exit* record

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/exitentry/ hkuID='3025704501' venue_code='CPD-2.58' datetime='20220502-16:25:00'
   ```

- delete **exit/entry record**:

  ```shell
  http DELETE http://group-k-studysafe.herokuapp.com/core/exitentry/id/
  ```




API service paths used by *StudySafe Trace*:

 - retrieve the **close contacts** of `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): [http://group-k-studysafe.herokuapp.com/core/members/close-contacts/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/core/members/close-contacts/3025704501/20220504/

 - retrieve the **venues** visited by `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): 

   [http://group-k-studysafe.herokuapp.com/core/venues/infectious-venues/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/core/venues/infectious-venues/3025704501/20220504/
   
   

### API documentation

Visit https://group-k-studysafe.herokuapp.com/core/apidoc for full documentation



### Admin Access

visit http://group-k-studysafe.herokuapp.com/admin as superuser (Username: `adminse`, Password: `comp3297`)
