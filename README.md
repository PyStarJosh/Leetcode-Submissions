# LeetCode Solutions

My solutions to LeetCode problems, organized by problem number with notes on approach and complexity.

## Structure

Each problem lives in its own folder under `solutions/`, named with a 4-digit zero-padded problem number followed by the problem slug:

```
solutions/
├── 0001-two-sum/
│   ├── README.md      # Problem notes, approach, complexity
│   └── solution.py    # The solution
├── 0015-3sum/
│   ├── README.md
│   └── solution.py
└── ...
```

The per-problem README documents the approach, time/space complexity, and any notes worth revisiting later.

## Conventions

- **Language:** Python 3
- **Naming:** Problem folders use `NNNN-problem-slug` format (e.g. `0042-trapping-rain-water`)
- **One solution per file** unless multiple approaches are worth comparing — in which case `solution_brute.py`, `solution_optimal.py`, etc.
- Each solution includes the function signature LeetCode expects, plus a small `if __name__ == "__main__"` block with example test cases for local debugging

## Goals

- Build intuition across common patterns (two pointers, sliding window, DP, graph traversal, etc.)
- Track progress and revisit weak areas
- Keep clean, readable solutions I can refer back to later

## Progress

- **Easy:** X solved
- **Medium:** X solved
- **Hard:** X solved
- **Total:** X / 3000+

---

*Solutions are my own work, written for learning purposes. Problem statements are property of LeetCode.*
