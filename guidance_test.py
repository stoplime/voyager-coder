import guidance

# we will use GPT-3 for most of the examples in this tutorial
# guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

# program = guidance('''The best thing about the beach is {{~gen 'best' temperature=1 max_tokens=10}}''')
# print(program())

program = guidance('''Is the following sentence offensive? Please answer with a single word, either "Yes", "No", or "Maybe".
Sentence: {{example}}
Answer:{{#select "answer" logprobs='logprobs'}} Yes{{or}} No{{or}} Maybe{{/select}}''')
executed_program = program(example='I hate tacos')

# program = guidance('''
# {{#system~}}
# Is the following sentence offensive? Please answer with a single word, either "Yes", "No", or "Maybe".
# {{~/system}}

# {{#user~}}
# Sentence: {{example}}
# {{~/user}}

# {{! this is a comment. note that we don't have to use a stop="stop_string" for the gen command below because Guidance infers the stop string from the role tag }}
# {{#assistant~}}
# Answer:{{#select "answer" logprobs='logprobs'}} Yes{{or}} No{{or}} Maybe{{/select}}
# {{~/assistant}}''')
# executed_program = program(example='I hate tacos')
# print(executed_program)