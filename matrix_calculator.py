### Requirement
#   streamlit
#   numpy
#   matplotlib
#   sympy


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.title("Linear Algebra Solver for Homogeneous and Non-homogeneous Systems")


def input_matrix_text_area():
    matrix_input = st.text_area(
        "Enter the augmented matrix [A | b] as shown (NB: Click the empty background to continue):",
        placeholder="1 2 3\n4 5 6",
    )
    if matrix_input:
        try:
            rows = matrix_input.strip().split("\n")
            matrix = np.array([list(map(float, row.split())) for row in rows])

            zero_vector = sp.zeros(matrix.shape[0], 1)
            homo_matrix = sp.Matrix(matrix[:, :-1])
            homo_matrix = homo_matrix.col_insert(homo_matrix.cols, zero_vector)

            return matrix, homo_matrix
        except ValueError:
            st.error("Invalid matrix format. Ensure all entries are numbers.")
    return None, None


def input_matrix_streamlit():

    dimension = st.text_input(
        "Enter the dimension of your augmented matrix (e.g., 3x3): "
    )
    if dimension:
        try:
            rows, cols = map(int, dimension.split("x"))
            augmented_matrix = np.zeros((rows, cols))
            st.write("Enter the augmented matrix [A | b]:")
            for i in range(rows):
                for j in range(cols):
                    augmented_matrix[i, j] = st.number_input(
                        f"Row {i + 1}, Column {j + 1}:", key=f"input_{i}_{j}"
                    )

            # Convert the NumPy array to a SymPy matrix
            sympy_augmented_matrix = sp.Matrix(augmented_matrix)

            zero_vector = sp.zeros(rows, 1)
            homo_matrix = sympy_augmented_matrix[:, :-1]
            homo_matrix = homo_matrix.col_insert(homo_matrix.cols, zero_vector)

            return augmented_matrix, homo_matrix
        except ValueError:
            st.error("Invalid input format for dimensions.")
    else:
        st.warning("Please enter dimensions.")
    return None, None


def solve_systems(augmented_matrix):
    matrix = sp.Matrix(augmented_matrix).rref()[0]
    matrix = np.array(matrix).astype(np.float64)

    A = matrix[:, :-1]
    b = matrix[:, -1]

    num_rows, num_cols = A.shape
    solutions = []
    free_vars = set(range(num_cols))

    for row in range(num_rows):
        if np.all(A[row, :] == 0) and (b[row] != 0):
            return "No solution: Inconsistent system"

    for row in range(num_rows):
        pivot_col = next((col for col in range(num_cols) if A[row, col] != 0), None)
        if pivot_col is not None:
            free_vars.remove(pivot_col)
            sol = f"x{pivot_col+1} = {b[row]}"
            for col in free_vars:
                if A[row, col] != 0:
                    sol += f" - {A[row, col]}*x{col+1}"
            solutions.append(sol)

    for var in free_vars:
        solutions.append(f"x{var+1} is a free variable")

    return solutions if solutions else ["Infinite solutions"]


def plot_solution(augmented_matrix):
    solutions = solve_systems(augmented_matrix)
    if solutions == "No solution: Inconsistent system":
        return solutions

    num_vars = augmented_matrix.shape[1] - 1
    A = augmented_matrix[:, :-1]
    b = augmented_matrix[:, -1]

    if num_vars == 2:
        x_vals = np.linspace(-10, 10, 50)
        plt.figure()

        for i in range(A.shape[0]):
            y_vals = (b[i] - A[i, 0] * x_vals) / A[i, 1]
            plt.plot(x_vals, y_vals, label=f"Equation {i+1}")

        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.grid(color="gray", linestyle="--", linewidth=0.5)
        plt.legend()
        plt.title("Solution to the System in R2")
        st.pyplot(plt)

    elif num_vars == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        x_vals = np.linspace(-10, 10, 50)
        y_vals = np.linspace(-10, 10, 50)

        X, Y = np.meshgrid(x_vals, y_vals)

        for i in range(A.shape[0]):
            if A[i, 2] !=0:
                Z = (b[i] - A[i, 0] * X - A[i, 1] * Y) / A[i, 2]
                ax.plot_surface(X, Y, Z, alpha=0.5, label=f"Equation {i+1}")

        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("x3")
        plt.title("Solution to the System in R3")
        st.pyplot(fig)

    else:
        st.error("This program can only plot solutions in R2 (2D) or R3 (3D) space.")


# Main Streamlit App
input_method = st.selectbox("Choose input method", ("Form Input", "Text Area"))

if input_method == "Form Input":
    augmented_matrix, homo_matrix = input_matrix_streamlit()
else:
    augmented_matrix, homo_matrix = input_matrix_text_area()

if augmented_matrix is not None and homo_matrix is not None:
    if st.button("Solve"):
        st.subheader("Non-homogeneous System Solution:")
        solutions = solve_systems(augmented_matrix)
        if solutions == "No solution: Inconsistent system":
            st.write(solutions)
        else:
            for sol in solutions:
                st.write(sol)
            plot_result = plot_solution(augmented_matrix)
            if plot_result == "No solution: Inconsistent system":
                st.write(plot_result)

        st.subheader("Homogeneous System Solution:")
        solutions = solve_systems(homo_matrix)
        for sol in solutions:
            st.write(sol)
        plot_solution(homo_matrix)
