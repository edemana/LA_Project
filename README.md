# Equations In Motion: A Graphical Exploration

## Overview

Welcome to the **Equations In Motion** project, a comprehensive exploration of solving and visualizing systems of linear equations using Python. This repository contains code and resources developed as part of a group project for MATH 212: Linear Algebra at Ashesi University, under the guidance of Dr. Justice K. Appati.

The project aims to develop a Python program capable of solving both homogeneous and non-homogeneous systems of linear equations and visualizing their solution sets. The application provides insights into the nature of these solutions, enabling users to explore the relationship between the systems' equations and their graphical representations.

## Project Summary

Systems of linear equations are fundamental in various fields, including engineering, economics, physics, and computer science. Our project delves into these systems' complexities, offering a Python-based solution to solve and visualize them.

### Key Components:
- **Input Method**: Allows users to manually input the augmented matrix or use a text area for direct input.
- **Solve System Method**: Computes the row-reduced echelon form, checks for inconsistencies, and provides solutions.
- **Plot Solutions Method**: Visualizes the solutions in either 2D or 3D, depending on the number of variables.

### Test Cases:
- **2D Unique Solution**: Example system with a single intersection point.
- **2D Infinite Solutions**: Example system where equations are dependent, leading to coinciding lines.
- **3D Unique Solution**: Example system where three planes intersect at a single point.
- **3D Infinite Solutions**: Example system where planes intersect along a line.
- **No Solution**: Example system with parallel lines that do not intersect.

### Historical Context:
The project also explores the historical development of methods for solving linear equations, from ancient Babylonian techniques to modern computational methods like Gaussian elimination.

### Discussion and Results:
- A unique solution in 2D results in intersecting lines.
- Infinite solutions occur when equations are dependent and represent the same line.
- In 3D, a unique solution is where three planes intersect at a single point.
- Infinite solutions in 3D occur when planes are parallel and intersect along a line.
- No solution is observed when lines or planes are parallel and do not intersect.

For a more detailed explanation of our project, including code examples and a thorough discussion of the results, please refer to our full [[Project Report](https://github.com/edemana/LA_Project/blob/main/Linear%20Algebra%20Report.pdf)].

## Streamlit Application

In addition to the Python code, we've developed a Streamlit application that allows users to interactively explore the solutions to systems of linear equations.

### Features:
- **Input System**: Users can input their linear equations directly into the application.
- **Solution Visualization**: The application solves the system and visualizes the results in either 2D or 3D, depending on the number of variables.
- **User-Friendly Interface**: The app is designed to be intuitive, making it easy for users to explore the solution space without needing to write any code.

### How to Run the Application:

1. Clone this repository:
   git clone [repository](https://github.com/edemana/LA_Project)

   cd Equations-In-Motion
   

3. Install the required dependencies:
   pip install -r requirements.txt
  

4. Run the Streamlit app:
   streamlit run app.py

5. Open your browser to `http://localhost:8501` to interact with the app.

### Example Use Cases:
- **Engineering**: Analyze structural equations and visualize the solution sets.
- **Economics**: Model supply and demand equations graphically.
- **Physics**: Explore solutions in mechanics or electrical circuits.
- **Computer Science**: Visualize linear systems used in graphics or machine learning.

## Documentation

For a comprehensive understanding of the project, including the theoretical background, methods, and results, please refer to the full [[Project Report](https://github.com/edemana/LA_Project/blob/main/Linear%20Algebra%20Report.pdf)].

## References

- [History of Linear Equations in Math - Mathnotspedia](https://mathnotespedia.in/history-of-linear-equations-in-math/)
- [ChatGPT - OpenAI](https://chatgpt.com)
- [Systems of Linear Equations - Mathsisfun.com](https://www.mathsisfun.com/algebra/systems-linear-equations.html)

## Contributors

This project was developed by:

- Caleb Okwesie Arthur @Okwesie
- Edem Korbla Anagbah @edemana
- Frances Seyram Fiahagbe @francesseyram

---

For more details, feel free to reach out or contribute to the project by submitting issues or pull requests. We hope this project provides valuable insights into solving and visualizing systems of linear equations!
