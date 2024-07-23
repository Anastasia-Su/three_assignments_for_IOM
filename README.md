# Three Assignments

## Excel Assignment
* Please see `transformed_tables.xlsx`: sheets 1, 2 and 3.

## Algorithm Assignment
* Please see `linked_list.py`. There, you will find a solution for creating and reversing a linked list.

## Python Assignment
* Please see `livelihood_by_oblast.ipynb`. It contains Python code that creates a transformed table and a bar chart based on `dataset.csv`. You can find them in `output_files` folder.  
* The libraries used for this code are: `numpy`, `pandas` and `matplotlib`.  
* Transformation steps:
    - Replaced null values in `Livelihood_Score` column with 0.
    - Removed unwanted special characters from `Oblast` column values.
    - Removed duplicated oblasts.
    - Ordered by `Livelihood_Score` (descending).
    - Created new column `Severity`. Set severity values:  
        `High`: livelihood score > 74,  
        `Medium`: 49 < livelihood score < 75,  
        `Low`: livelihood score < 50.
    - Visualized the scores by oblast using bar chart.
