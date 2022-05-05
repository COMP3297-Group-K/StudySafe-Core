# StudySafe (Group K)


| Description                      | URL                                                 |
| -------------------------------- | --------------------------------------------------- |
| StudySafe Core                   | http://group-k-studysafe.herokuapp.com/core/        |
| StudySafe Core API Documentation | http://group-k-studysafe.herokuapp.com/core/apidoc  |
| StudySafe Trace                  | http://group-k-studysafe-trace.herokuapp.com/trace/ |



### StudySafe Core Example Usage

General purposes APIs:

 - list all the **campus venues**: http://group-k-studysafe.herokuapp.com/core/venues/

 - retrieve the info on a campus venue by `venue_code`: [http://group-k-studysafe.herokuapp.com/core/venues/<venue_code\>/]()<br>e.g. http://group-k-studysafe.herokuapp.com/core/venues/CPD-LG.02/


 - list all the **HKU members**: http://group-k-studysafe.herokuapp.com/core/members/


 - retrieve the info about a HKU memeber by `hkuID`: [http://group-k-studysafe.herokuapp.com/core/members/<hkuID\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/core/members/3030012344/

 - list all the **exit/entry record**: http://group-k-studysafe.herokuapp.com/core/exitentry/

 - add **exit/entry record** of `hkuID` to `venue` at `datetime` (YYYMMDD-HH:MM:SS)

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/ExitEntry/ hkuID=<hkuID> venue_code=<venue_code> datetime='20220401-09:00:00'
   ```

   e.g. 

   1. add *entry* record

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/ExitEntry/ hkuID='3030012345' venue_code='CPD-LG.02' datetime='20220401-09:00:00'
   ```

   2. add *exit* record

   ```shell
   http POST http://group-k-studysafe.herokuapp.com/core/ExitEntry/ hkuID='3030012345' venue_code='CPD-LG.02' datetime='20220401-09:00:00'
   ```

API service paths used by *StudySafe Trace*:

 - retrieve the **close contacts** of `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): [http://group-k-studysafe.herokuapp.com/core/members/close-contacts/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/core/members/close-contacts/3030012345/20220411/

 - retrieve the **venues** visited by `hkuID` whose onset/diagnose date is `date` (YYYYMMDD): 

   [http://group-k-studysafe.herokuapp.com/core/venues/infectious-venues/<hkuID\>/<date\>/]() <br>e.g. http://group-k-studysafe.herokuapp.com/core/venues/infectious-venues/3030012345/20220411/



### StudySafe Trace Example Usage

 - view all the infected HKU members: http://group-k-studysafe-trace.herokuapp.com/trace

 - view their close contacts: http://group-k-studysafe-trace.herokuapp.com/trace/contacts

 - view all the venues visited by the infectious two days before onset/diagnosis: http://group-k-studysafe-trace.herokuapp.com/trace/venues

 - view `hkuID`'s close contacts: [http://group-k-studysafe-trace.herokuapp.com/trace/contacts/<hkuID\>]() <br>e.g. http://group-k-studysafe-trace.herokuapp.com/trace/contacts/3030012348

 - view the venues visited by `hkuID` two days before onset/diagnosis: [http://group-k-studysafe-trace.herokuapp.com/trace/venues/<hkuID\>]() <br>e.g. http://group-k-studysafe-trace.herokuapp.com/trace/venues/3030012348



### API documentation

##### Visit https://group-k-studysafe.herokuapp.com/core/APIDoc for full documentation



### Admin Access

visit http://group-k-studysafe.herokuapp.com/admin as superuser (Username: `adminse`, Password: `comp3297`)

| Repository and project root                                  | Configuration root     | App root                                    |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------- |
| [StudySafe-Core](https://github.com/COMP3297-Group-K/StudySafe-Core) | StudySafe-Core/config  | StudySafe-Core/users<br>StudySafe-Core/Core |
| [StudySafe-Trace](https://github.com/COMP3297-Group-K/StudySafe-Trace) | StudySafe-Trace/config | StudySafe-Trace/Trace                       |

