Sql inspector tool
==================
A simple middleware tool for analyzing Django ORM SQL execution.

# Usage
Add the follow line of code to your middleware in your project settings.py file.

```
sql-inspector-tool.middleware.sql_middleware
```

# How it works
The tool uses Django built in features to inspectthe SQL generated from queries executed by the application.
3rd party tools are used to format and highlight the SQL presented in the terminal window.