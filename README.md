# Voyager-coder
Generalizing the voyager to making any code.


Voyager: https://github.com/MineDojo/Voyager (https://arxiv.org/abs/2305.16291)

## Outline
1. User prompts the model for a task
2. The model responds with a plan of action
3. The user verifies that the plan is correct or modify the plan and repeat step 2.
4. The model then creates a set of unit tests that could verify the plan and write comments for the location of code changes.
5. The user then verifies the code change comments and the unit test to proceed with the code implementation.
6. The model generates the code implementation and runs the unit tests.
7. If the unit tests fail, then the model should generate a hypothesis of why it failed and generate a plan. Move to step 3.
8. If the unit tests succeed, then adds any useful fuctions/skills to the skill library.
