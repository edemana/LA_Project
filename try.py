import streamlit as st
import numpy as np
import matplotlib

matplotlib.use("Agg")  # Setting the backend
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D

st.title("Linear Algebra Solver")
st.write("Enter augmented matrix [A | b] in the format below:")
st.write("m n o")
st.write("p q r")

# Input Area for the Matrix
matrix_input = st.text_area(
    "",
    placeholder="""
    1 2 3
    4 5 6
    """,
)


# --- Helper Functions ---
def solve_system(augmented_matrix):
    matrix = sp.Matrix(augmented_matrix).rref()[0]
    matrix = np.array(matrix).astype(np.float64)

    A = matrix[:, :-1]
    b = matrix[:, -1]

    num_rows, num_cols = A.shape
    solutions = []
    free_vars = set(range(num_cols))

    for row in range(num_rows):
        if np.all(A[row, :] == 0) and (b[row] != 0):
            return ["No solution: Inconsistent system"]

    for row in range(num_rows):
        pivot_col = next((col for col in range(num_cols) if A[row, col] != 0), None)
        if pivot_col is not None:
            free_vars.remove(pivot_col)
            solutions.append(
                f"x{pivot_col+1} = {b[row]} "
                + " ".join(
                    [
                        f"- {A[row,col]}*x{col+1}"
                        for col in free_vars
                        if A[row, col] != 0
                    ]
                )
            )

    for var in free_vars:
        solutions.append(f"x{var+1} is a free variable")

    return solutions if solutions else ["Infinite solutions"]


def plot_solution(augmented_matrix):
    A = augmented_matrix[:, :-1]
    b = augmented_matrix[:, -1]
    num_vars = A.shape[1]

    if num_vars == 2:
        plot_solution_R2(A, b)
    elif num_vars == 3:
        plot_solution_R3(A, b)
    else:
        st.warning("Plotting is only supported for 2D and 3D systems.")


def plot_solution_R2(A, b):
    plt.clf()  # Clear previous figure
    x_vals = np.linspace(-10, 10, 400)
    fig, ax = plt.subplots()
    for i in range(A.shape[0]):
        if A[i, 1] != 0:
            y_vals = (b[i] - A[i, 0] * x_vals) / A[i, 1]
            ax.plot(x_vals, y_vals, label=f"Equation {i+1}")
        else:
            ax.axvline(x=b[i] / A[i, 0], label=f"Equation {i+1}")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.legend()
    st.pyplot(fig)


def plot_solution_R3(A, b):
    plt.clf()
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for i in range(A.shape[0]):
        Z = (b[i] - A[i, 0] * X - A[i, 1] * Y) / A[i, 2]
        ax.plot_surface(X, Y, Z, alpha=0.5)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("x3")
    st.pyplot(fig)


if st.button("Solve Ax = b"):
    if matrix_input:
        try:
            # Parse input and create augmented matrix
            rows = [
                list(map(float, row.split()))
                for row in matrix_input.split("\n")
                if row.strip()
            ]
            augmented_matrix = np.array(rows)

            # Solve the system
            solutions = solve_system(augmented_matrix)

            # Display solutions
            st.subheader("Solution:")
            for sol in solutions:
                st.text(sol)

            # Plot the solution
            plot_solution(augmented_matrix)

        except ValueError:
            st.error("Invalid input format.")
    else:
        st.warning("Please enter the matrix.")
