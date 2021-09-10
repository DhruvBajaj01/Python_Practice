#!/usr/bin/env python
# coding: utf-8

# In[1]:


from automata.fa.dfa import DFA
dfa = DFA(
 states={'q0', 'q1', 'q2', 'q3'},
 input_symbols={'0', '1'},
 transitions={
 'q0': {'0': 'q1', '1': 'q0'},
 'q1': {'0': 'q2', '1': 'q0'},
 'q2': {'0': 'q2', '1': 'q3'},
 'q3': {'0': 'q3', '1': 'q3'}
 },
 initial_state='q0',
 final_states={'q3'}
)
for i in range(1,4):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")


# In[ ]:




