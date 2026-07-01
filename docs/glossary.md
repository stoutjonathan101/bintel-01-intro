# Glossary

Use this page to record terms and ideas that help you understand
professional analytics projects.

This project introduces business intelligence and smart sales data:
loading raw data, inspecting it, and thinking in terms of business goals.

Pro-tip: Expand the VS Code **Outline** view (below the navigator on the right)
to see this file organization at-a-glance.

## Project Organization

### source code

Source code are instructions that tell the computer what to do.
In a Python project, source code lives in files ending with `.py`.

### module

A module is one Python file that contains related code.
A module may include constants, functions, imports, and a `main()` function.
A project may have many modules working together.

### package

A package is a folder of related Python modules.
A package usually includes an `__init__.py` file.
The init file allows code in that folder to be
imported and reused across a project.

### virtual environment

A virtual environment is an isolated folder (`.venv/`) that holds
the specific Python packages a project needs.
Using one means projects do not interfere with each other.

## Reuse and Workflow

### reusable function

A reusable function is a named block of code that performs
one clear task and can be called more than once.
Good functions make projects easier to read, test, debug, and modify.

### dependency

A dependency is an external package or tool that a project
needs in order to run.
Dependencies are listed in `pyproject.toml`
and the environment can be easily recreated using `uv`.

### workflow

A workflow is an ordered process for completing work.
In a project, a workflow might include running code,
checking results, making changes, testing again,
and saving progress with Git.

### version control

Version control is a system for tracking changes to files over time.
Git is the most widely used version control system.
It allows you to save snapshots of your work and recover earlier versions.

### repository

A repository (repo) is a folder tracked by Git.
It contains your project files and the full history of changes.
GitHub hosts repositories online so they can be shared and backed up.

## Data and Outputs

### raw data

Raw data is the original input data used by the project.
It should usually be kept unchanged so the analysis
can be repeated from the original source.

### CSV file

A CSV (comma-separated values) file stores tabular data as plain text.
Each row is a record and each value is separated by a comma.
CSV files can be opened in Excel, VS Code, or read into Python with pandas.

### log file

A log file records what happened when a program ran.
The `project.log` file in this project captures INFO and DEBUG messages
so you can review what the program did without re-running it.

## Business Intelligence Concepts

### business intelligence

Business intelligence (BI) is the process of collecting, organizing,
and analyzing business data to support better decisions.
BI turns raw data into actionable insights.

### data-driven decision making

Data-driven decision making (DDDM) means using data and analysis
to guide business choices rather than relying on intuition alone.
The goal is to reduce guesswork and increase confidence in decisions.

### KPI

A KPI (Key Performance Indicator) is a measurable value that shows
how well a business is achieving a specific goal.
Examples include total revenue, customer count, and average sale amount.

### actionable insight

An actionable insight is a finding from data analysis that suggests
a specific thing the business should do.
A good BI analysis always ends with a recommendation, not just a chart.

### dimension

A dimension is a descriptive attribute used to slice and group data.
Examples include region, product category, and date.
Dimensions answer questions like who, what, where, and when.

### metric

A metric is a numeric value that measures business performance.
Examples include total sales, average order value, and transaction count.
Metrics answer questions like how much and how many.
