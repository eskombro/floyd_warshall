## Installation

Install `docker` and `docker-compose` on your server and run

`docker-compose up`

## Usage

### 1. Authenticate

In order to use Floyd-Warshall algorithm implementation, you need to be authenticated.  

Route `/authenticate` is available and takes two form field parameters: username and password.  Default values for test are 'admin:admin'

#### - Example of authentication (saving cookies):


`curl -sD - -X POST -c /tmp/cookies.tmp -F 'username=admin' -F 'password=admin' http://localhost/authenticate | grep csrftoken | cut -d '=' -f2 | cut -d ';' -f1`

(Remember to replace localhost with your URL or IP if needed)

```
Output example:

kebp5QttjuFix4JeHznFAfg8RIOb2nRDiehiQUXanns44HCBGvqqF7VJwxn0dJ9N
```

### 2. Send graph data

When you get your CSRF Token, you can now make a POST request to `/floyd-warshall`  

You will need to send your token as a X-CSRFToken in header request (example below)

The request body requires a json object with a field called "data", providing the graph information.
Format expected is:

  - First line: Number of nodes
  - Second line: Number of links between nodes
  - Third to last line: Each link specifying node source, node destination and distance.

#### - Format example:

```
4
7
1,2,3
2,3,2
3,4,1
3,1,5
4,1,2
2,1,8
1,4,7
```

#### - Request example:


`curl -X POST -H "Content-Type: application/json" -H "X-CSRFToken: <YOUR_CSRF_TOKEN>" -d '{"data":"4\n7\n1,2,3\n2,3,2\n3,4,1\n3,1,5\n4,1,2\n2,1,8\n1,4,7"}' -b /tmp/cookies.tmp http://localhost/floyd-warshall`

Remember to replace <YOUR_CSRF_TOKEN> with the token from the last step (and localhost with your URL or IP if needed)

```
Output example:

[0, 3, 5, 6][5, 0, 2, 3][3, 6, 0, 1][2, 5, 7, 0]
```

### 3. Logout

Route `/logout` will terminate your session and you will no longer be authorized to make requests to `/floyd-warshall`

`curl -X POST -H "Content-Type: application/json" -H "X-CSRFToken: <YOUR_CSRF_TOKEN>" -b /tmp/cookies.tmp http://localhost/logout`

Remember to replace <YOUR_CSRF_TOKEN> with the token from step 1 (and localhost with your URL or IP if needed)
