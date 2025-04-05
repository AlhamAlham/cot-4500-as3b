# cot-4500-as3b

## Overview
This project implements several core linear algebra algorithms without using external libraries like `scipy`, following specifications from the COT 4500 Numerical Analysis course.

### Included Topics:
1. **Gaussian Elimination with Backward Substitution**  
2. **LU Factorization (Doolittle's Method)**  
   - Computes **L** and **U** matrices  
   - Computes the **determinant** of the original matrix  
3. **Diagonal Dominance Check**  
4. **Positive Definiteness Check**

`test_assignment_3.py` includes unit tests and examples to verify the correctness of each method.

---

## Repository Structure
```
cot-4500-as3b
│-- src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_3.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_3.py
│-- requirements.txt
│-- README.md
```

---

## Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/AlhamAlham/cot-4500-as3b
cd cot-4500-as3b
```

### **2. Install Dependencies**
Only **NumPy** is required:
```bash
pip install -r requirements.txt
```

> 💡 Note: If you're not using any libraries beyond Python's standard library and NumPy, your `requirements.txt` can simply contain:
> ```
> numpy
> ```

---

## Running the Code

To run the main script (which prints the results for all 4 questions):
```bash
python src/main/assignment_3.py
```

---

## Running the Tests

I moved the tests into the same file as assignment_3
