# Code Challenge: Access Control Decorator

## Background:
Decorators in Python are often used to enhance or modify the behavior of functions or methods, especially for repetitive tasks like logging, caching, or access control. In this challenge, you will create a decorator that checks if a user has the required permissions to execute a function.

## Challenge Description:
You are tasked with writing a decorator named requires_permission. This decorator should check if a provided user object has the specified permission before allowing the function to execute. If the user does not have the required permission, the function should not execute, and instead, an exception should be raised.

## Requirements:
Define a User class with attributes name and permissions (a list of strings).
Implement the requires_permission decorator, which takes the required permission as an argument and checks this against the user’s permissions.
If the user has the permission, the function should execute normally.
If the user does not have the permission, raise a PermissionError with a message.

## Instructions:
Implement the User class.
Write the requires_permission decorator as described.
Test the decorator with a function that simulates an action requiring permissions, such as edit_document.
Handle cases where the user lacks the required permission by catching PermissionError.

## Goals of the Challenge:
Learn how to create and use decorators to encapsulate common functionality such as access control checks.
Understand how decorators can simplify the management of cross-cutting concerns in a codebase.
Practice raising and handling exceptions in Python.