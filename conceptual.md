### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Python alone needs to run on a server, while JavaScript can be ran on a browser
  - Syntax and installing dependencies
  - Differences in mutability

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.
  ```
  dictionary = {"a": 1, "b": 2}
  ```
  ```
  dictionary.get("c", None)
  ```
  ```
  if "c" in dictionary: 
    return True
  else:
    return None
  ```

- What is a unit test?
  - Unit tests are typically only used to test one function or method. An example would be testing the output of a function.

- What is an integration test?
  - Integration tests are tests that make sure components work together. An example of integrated testing is checking the HTML received after directing to a certain URL path.

- What is the role of web application framework, like Flask?
  - Flask provides other tools and libraries to allow python users to build web applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - I would use a URL query param to if I needed to store any information from the user.
  - I would use route URL's for simple page navigation.

- How do you collect data from a URL placeholder parameter using Flask?
  - Import Flask's `request` object to collect data from the URL.

- How do you collect data from the query string using Flask?
  - Using Flask's `request.args[query_name]` command to get information the the URL. 
- How do you collect data from the body of the request using Flask?
  - `request.data`

- What is a cookie and what kinds of things are they commonly used for?
  - A cookie is a name/string-value pair that's stored on the browser. When the client(browser) makes a request, cookies will be sent to the server and the server will tell the browser to store the cookies.

- What is the session object in Flask?
  - The session object in Flask acts as a dictionary that stores data on the browser as a cookie. This data is encrypted and cannot be manually modified by the user through the browser. Adding Flask-session will allow you to store session data on the server instead.
- What does Flask's `jsonify()` do?
  - `jsonify()` will parse any data passed in, into a JSON string 

- What was the hardest part of this past week for you?
  What was the most interesting?
  - The hardest part of this week was working on the Flask Boggle Assignment and understanding how Javascript and Python "communicate" back and forth.
  - While the Flask Boggle Assignment may have been the most difficult part of this week, it was also the most interesting and rewarding being able to see how everything can come together.
