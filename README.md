# Employee Scheduling System

This project is a **Flask-based web application** designed to optimize employee schedules using a **genetic algorithm**. The system allows users to input employee names, total required hours, and constraints such as maximum and minimum working hours per employee. The application calculates an optimal schedule that distributes working hours fairly among employees while meeting the specified requirements.

---

## Features

### 1. **Genetic Algorithm Optimization**
- Uses a genetic algorithm to solve scheduling problems.
- Optimizes schedules based on total hours, fairness, and constraints.
- Iteratively improves solutions through selection, crossover, and mutation.

### 2. **Customizable Parameters**
- Input employee names as a list.
- Define:
  - Total required hours to cover.
  - Maximum and minimum working hours per employee.
- Allows flexibility to adapt to various scheduling needs.

### 3. **Interactive Web Interface**
- Built using **HTML**, **Bootstrap**, and **JavaScript**.
- User-friendly form for data input.
- Real-time display of the generated schedule.

### 4. **Backend Logic with Flask**
- Handles input validation and schedule generation.
- Provides a RESTful API endpoint (`/schedule`) for generating schedules in JSON format.

---

## How It Works

1. **Input Data**:
   - Users input a comma-separated list of employee names.
   - Specify the total hours required, maximum hours, and minimum hours per employee.

2. **Genetic Algorithm**:
   - Generates an initial population of schedules.
   - Evaluates schedules using a fitness function considering:
     - Total hours covered.
     - Fairness in hour distribution.
   - Evolves schedules over multiple generations to find the best solution.

3. **Schedule Output**:
   - The optimal schedule is displayed in the interface.
   - Schedules are presented in JSON format for further use or analysis.

---

## Technologies Used

- **Backend**:
  - Flask (Python)
  - RESTful API for schedule generation

- **Frontend**:
  - HTML
  - Bootstrap 5 for styling
  - jQuery for handling AJAX requests

- **Algorithm**:
  - Genetic Algorithm for optimization
  - Randomized generation, selection, crossover, and mutation logic

