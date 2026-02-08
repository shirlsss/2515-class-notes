# Lab 4 Reflection Questions

## 1. How do fixtures reduce code duplication in tests?

We can create fixtures to serve as common parameters to pass into any of our tests. for example, we can set a fixture to be a particular string and then, by passing a fixture as a parameter into a test_function, we can use it in multiple places.

## 2. What happens when you use a fixture name as a parameter in a test function?

We get to use this fixture as an argument when testing inside our test function

## 3. Why is tmp_path useful for testing file operations?

This creates temporary files that we can test file operation functions on, like those that use `with open` to file.write, file.read, etc., instead of needing to create our own testing folders. This tmp_path gets deleted after the test is done running.

## 4. How can fixtures use other fixtures?

We can pass in other fixtures as parameters for a fixture, to use fixtures inside a fixture.
