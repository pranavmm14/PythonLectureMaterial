# Demonstration of Python `math` Module Functions

The usage of various functions available in Python's `math` module.

## Constants

The `math` module provides several mathematical constants:

- **π (pi)**: The ratio of the circumference of a circle to its diameter.
- **e**: The base of natural logarithms.
- **τ (tau)**: The ratio of the circumference of a circle to its radius (2π).
- **inf**: Represents positive infinity.
- **nan**: Represents a floating-point "Not a Number" value.

```python
import math

print("Math Constants:")
print(f"math.pi: {math.pi}")
print(f"math.e: {math.e}")
print(f"math.tau: {math.tau}")
print(f"math.inf: {math.inf}")
print(f"math.nan: {math.nan}")
print()
```

## Trigonometric Functions

These functions are used to perform trigonometric calculations:

- **sin(x)**: Returns the sine of `x` radians.
- **cos(x)**: Returns the cosine of `x` radians.
- **tan(x)**: Returns the tangent of `x` radians.
- **asin(x)**: Returns the arc sine of `x`.
- **acos(x)**: Returns the arc cosine of `x`.
- **atan(x)**: Returns the arc tangent of `x`.

```python
angle = math.pi / 4  # 45 degrees

print("Trigonometric Functions:")
print(f"math.sin({angle}): {math.sin(angle)}")
print(f"math.cos({angle}): {math.cos(angle)}")
print(f"math.tan({angle}): {math.tan(angle)}")
print(f"math.asin(1): {math.asin(1)}")
print(f"math.acos(1): {math.acos(1)}")
print(f"math.atan(1): {math.atan(1)}")
print()
```

## Hyperbolic Functions

These functions are used to perform hyperbolic calculations:

- **sinh(x)**: Returns the hyperbolic sine of `x`.
- **cosh(x)**: Returns the hyperbolic cosine of `x`.
- **tanh(x)**: Returns the hyperbolic tangent of `x`.

```python
x = 1

print("Hyperbolic Functions:")
print(f"math.sinh({x}): {math.sinh(x)}")
print(f"math.cosh({x}): {math.cosh(x)}")
print(f"math.tanh({x}): {math.tanh(x)}")
print()
```

## Exponential and Logarithmic Functions

These functions are used for exponential and logarithmic calculations:

- **exp(x)**: Returns `e` raised to the power of `x`.
- **log(x)**: Returns the natural logarithm of `x`.
- **log10(x)**: Returns the base-10 logarithm of `x`.
- **log2(x)**: Returns the base-2 logarithm of `x`.

```python
print("Exponential and Logarithmic Functions:")
print(f"math.exp(1): {math.exp(1)}")
print(f"math.log(1): {math.log(1)}")
print(f"math.log(math.e): {math.log(math.e)}")
print(f"math.log10(100): {math.log10(100)}")
print(f"math.log2(1024): {math.log2(1024)}")
print()
```

## Power Functions

These functions are used for power calculations:

- **pow(x, y)**: Returns `x` raised to the power of `y`.
- **sqrt(x)**: Returns the square root of `x`.
- **isqrt(x)**: Returns the integer square root of `x`.

```python
print("Power Functions:")
print(f"math.pow(2, 3): {math.pow(2, 3)}")
print(f"math.sqrt(16): {math.sqrt(16)}")
print(f"math.isqrt(16): {math.isqrt(16)}")
print()
```

## Rounding Functions

These functions are used for rounding numbers:

- **ceil(x)**: Returns the smallest integer greater than or equal to `x`.
- **floor(x)**: Returns the largest integer less than or equal to `x`.
- **trunc(x)**: Returns the truncated integer value of `x`.

```python
print("Rounding Functions:")
print(f"math.ceil(4.2): {math.ceil(4.2)}")
print(f"math.floor(4.8): {math.floor(4.8)}")
print(f"math.trunc(4.8): {math.trunc(4.8)}")
print()
```

## Other Functions

These functions perform various other mathematical operations:

- **fabs(x)**: Returns the absolute value of `x`.
- **factorial(x)**: Returns the factorial of `x`.
- **gcd(x, y)**: Returns the greatest common divisor of `x` and `y`.
- **isclose(a, b)**: Returns `True` if the values `a` and `b` are close to each other.
- **isfinite(x)**: Returns `True` if `x` is neither an infinity nor a NaN.
- **isnan(x)**: Returns `True` if `x` is a NaN.

```python
print("Other Functions:")
print(f"math.fabs(-5): {math.fabs(-5)}")
print(f"math.factorial(5): {math.factorial(5)}")
print(f"math.gcd(48, 18): {math.gcd(48, 18)}")
print(f"math.isclose(1.0, 1.0): {math.isclose(1.0, 1.0)}")
print(f"math.isfinite(1.0): {math.isfinite(1.0)}")
print(f"math.isnan(math.nan): {math.isnan(math.nan)}")
print()
```

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---