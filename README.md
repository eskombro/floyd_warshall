## Usage: How to request server

### 1. Authenticate

In order to use Floyd Warshall algorithm implementation, you need to be authenticated. Route `/authenticate` is available and takes two form parameters: username and password.  Default values are 'admin' and 'admin'

#### Example of authentication and saving cookies:


`curl -sD - -X POST -c /tmp/cookies.tmp -F 'username=admin' -F 'password=admin' http://localhost:8000/authenticate  | grep csrf | cut -d ' ' -f3`

```
Output:

csrftoken=sPntJWmRTP8rRfjl0hiOe12HveODf2FNDHByOg8pMrAv0w4GMM1wpJUfUmWgUYPd;
```

### 2. Send graph data

When you get your CSRF Token, you can now make a POST request to ``/floyd-warshall`
You must send a json object with a field called "data", providing the graph information.
Format expected is:

  - First line: Number of nodes
  - Second line: Number of links between nodes
  - Third to last line: Each link specifying node source, node destination and distance.

#### Format example:

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

- Request example

`curl -X POST -H "Content-Type: application/json" \
-H "X-CSRFToken: <YOUR_CSRF_TOKEN>" \
-d '{"data":"4\n7\n1,2,3\n2,3,2\n3,4,1\n3,1,5\n4,1,2\n2,1,8\n1,4,7"}' \
-b /tmp/cookies.tmp \
http://localhost:8000/floyd-warshall`

```
Output:

[0, 3, 5, 6][5, 0, 2, 3][3, 6, 0, 1][2, 5, 7, 0]
```
