# Assignment 03 — CHANGES

**Name:** Khun Maung Aye **Student ID:** 6705140019

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| #   | Code smell in the original                                           | What I changed it to                                                               | OOP concept applied                    | How I verified behaviour was unchanged |
| --- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------- | -------------------------------------- |
| 1   | Product data was kept as raw tuples in a parallel list               | Replaced with a `Product` class that validates name, price, and category           | Classes / composition                  | Ran `python Assignment_03.py` → PASS   |
| 2   | Membership discount and points logic used repeated `if/elif` chains  | Moved the policy into `Customer` subclasses (`None`, `Silver`, `Gold`, `Platinum`) | Polymorphism                           | PASS                                   |
| 3   | Totals and receipt printing were mixed together in one function      | Split calculation into pure methods and a separate receipt-building method         | Encapsulation / separation of concerns | PASS                                   |
| 4   | Magic numbers like `0.07`, `100`, and `10` were scattered throughout | Named constants centralise all thresholds and tax values                           | Clean design                           | PASS                                   |
| 5   | Order items were just indexes into loose lists                       | `Order` now owns `OrderItem` objects that contain a real product and quantity      | Composition                            | PASS                                   |

## 2 · Short reflection (4–6 sentences)

The biggest improvement was moving the customer policy out of conditional branching and into subclasses. Once the order, item, and product model were real objects, the calculations became easier. The careful part was preserving the exact legacy output: that meant even tiny differences in rounding, spacing, or print order count as a failure because this task is a refactor, not a redesign. I kept the original print text and the same arithmetic rules so that the self-test remained a valid behaviour check. That meant validating constructors, totals, and blank lines precisely. After all of that I considered this refactoring a success.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| #   | My prompt to the AI                                                                                | What it suggested (summary)                                                                                        | Accept / reject / edited         | How I checked it                                    |
| --- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------------- |
| 1   | "Refactor this messy store program into a clean OOP design while preserving the exact output."     | Suggested creating `Product`, `OrderItem`, `Customer`, and `Order` classes with polymorphic tiers                  | Edited                           | Ran `python Assignment_03.py` repeatedly until PASS |
| 2   | "How do I preserve the legacy receipt format exactly while separating calculations from printing?" | Keep all arithmetic in pure methods and build the text output in a receipt function                                | Accepted with minor naming edits | Verified output lines matched the target exactly    |
| 3   | "I need a safe design for tax and discount policies without using tier `if/elif` chains."          | Use a `Customer` class family and `Product.tax_rate()` so tax and discount logic stay polymorphic and object-owned | Edited                           | Checked both self-test and print formatting         |

**Ownership statement.** By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
