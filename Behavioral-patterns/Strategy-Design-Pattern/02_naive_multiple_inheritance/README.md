## Naive Fix: Multiple Inheritance

We tried to fix the issue by splitting behaviors into mixins.

### Why this is still bad:
- Tight coupling between Duck and behaviors
- Hard to change behavior at runtime
- Class explosion as behaviors grow
- Not all languages support multiple inheritance
