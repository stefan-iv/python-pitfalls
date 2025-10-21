# Python Pitfalls

A collection of common Python programming pitfalls and how to avoid them.

## 1. Using `is` for Value Comparison
**File:** `pitfall1_is.py`
Using `is` to compare values instead of `==` - works for small integers due to caching but fails for larger numbers.

## 2. Mutable Default Arguments
**File:** `pitfall2_mutable_default.py`
Using mutable objects (like lists) as default function arguments creates shared state across function calls.

## 3. List Multiplication with Mutable Objects
**File:** `pitfall3_list_multiplication.py`
Multiplying lists containing mutable objects creates references to the same object, not independent copies.

## 4. Truthiness Gotchas
**File:** `pitfall4_truthiness.py`
Unexpected falsy values like `0`, empty containers, and `None` can cause bugs in conditional logic.

## 5. Shallow Copy vs Deep Copy
**File:** `pitfall5_closures.py`
Using `copy()` creates shallow copies that still share references to nested mutable objects - use `deepcopy()` for true independence.

## 6. Variable Shadowing Issues
**File:** `pitfall6_shadowing.py`
Accidentally shadowing built-in functions or outer scope variables with local variables, causing unexpected behavior.

## 7. Mutating While Iterating
**File:** `pitfall7_mutate_while_iterating.py`
Modifying a list while iterating over it can skip elements or cause unexpected behavior.
