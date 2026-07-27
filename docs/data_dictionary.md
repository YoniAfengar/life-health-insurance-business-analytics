# Data Dictionary

# Overview

This document describes the variables used in the Life & Health Insurance Business Analytics project.

The dataset contains demographic, socioeconomic, and insurance claim information for 13,000 synthetic customers.

---

# Dataset Summary

| Property | Value |
|----------|-------|
| Records | 13,000 |
| Variables | 7 |
| Missing Values | None |
| Duplicate Records | None |

---

# Variables

## Age

**Type:** Numerical

**Description:**

Customer age in years.

**Example values**

- 23
- 41
- 58

---

## Gender

**Type:** Categorical

**Description:**

Customer gender.

**Possible values**

- Male
- Female

---

## Income

**Type:** Numerical

**Description:**

Annual customer income.

The values represent income before any analysis or transformation.

---

## Marital_Status

**Type:** Categorical

**Description:**

Customer marital status.

**Possible values**

- Single
- Married
- Divorced
- Widowed

---

## Education

**Type:** Categorical

**Description:**

Highest education level attained by the customer.

**Possible values**

- High School
- Bachelor's
- Master's
- PhD

---

## Occupation

**Type:** Categorical

**Description:**

Customer occupation category.

The dataset contains multiple occupation groups that are used for comparative analysis.

---

## Claim_Amount

**Type:** Numerical

**Description:**

Insurance claim amount associated with each customer.

This is the primary response variable analyzed throughout the project.

---

# Numerical Variables

| Variable | Type |
|----------|------|
| Age | Integer |
| Income | Numeric |
| Claim_Amount | Numeric |

---

# Categorical Variables

| Variable | Categories |
|----------|------------|
| Gender | 2 |
| Marital_Status | 4 |
| Education | 4 |
| Occupation | Multiple |

---

# Unit of Analysis

Each row in the dataset represents **one insurance customer and one associated insurance claim**.

No repeated customer identifiers are available.

---

# Notes

The dataset is synthetic and intended for educational and analytical purposes.

It should not be interpreted as representing real insurance customers or real insurance claims.