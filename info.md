## Request Header:
```
Origin: https://people.jacobs.university
Authorization: Bearer Sq5NEGsKD5h7h2NOdLDKcQVQRlflHU
Referer: https://people.jacobs.university/?q=Brian
```
## Request Address
```
https://jacobs.university/api/v1/users/?limit=7000&skip=0&tl=(((%22firstName%22%20contains%20%22yiping%22)%20or%20(%22lastName%22%20contains%20%22yiping%22)))%20and%20((%22active%22%20equals%20true))
```

## The result is like:
```
{'eid': 42796, 'active': True, 'email': 'y.deng@jacobs-university.de', 'username': 'ydeng', 'firstName': 'Yiping', 'lastName': 'Deng', 'country': 'China', 'college': 'C3', 'phone': '5665', 'isCampusPhone': True, 'room': 'CA-225', 'building': 'C3', 'isStudent': False, 'isFaculty': False, 'isStaff': False, 'status': 'undergrad', 'degree': None, 'year': 20, 'majorShort': 'CS'}
```
