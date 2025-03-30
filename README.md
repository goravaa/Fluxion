I’m trying to build a **pipeline leakage simulation system** that can model and simulate leakages in complex pipeline networks. The goal is to use a **modular approach** where a user can define multiple pipelines (with custom dimensions, junctions, etc.), select the fluid or gas type, and then start a simulation server that mimics real-world behavior — including pressure, flow, and leak dynamics.

Eventually, I want to turn this into a working **MVP** where users can:
- Add as many pipes as they want
- Choose liquid/gas properties
- Simulate in real time
- View live sensor data
- Inject leaks dynamically

I'll also be **experimenting with different deep learning models**, including **Physics-Informed Neural Networks (PINNs)** and traditional models, to detect and localize leaks. I’m following a few research papers for reference, and this project will evolve as I test ideas and validate results.