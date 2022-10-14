# Machine process
1. Drive to rails 43 
2. Pick up tip at position 0 (in every iteration move one position further)
3. Drive to rails 26 
4. Aspirate 1000 ul from tip at position 0 
5. Drive to rail 1 and dispense 1000 ul at position 0 
6. Dispose tip
7. Repeat three times 

# Notes
SMP_CAR_32_A00

On rail 43 tip gets not captured. Problem occurs probably because existing ressource on deck is not the same which is defined in python code.

now i need a workaround for the issue that i have picked up the tip and that i can remove the tip somehow again because if i start any process now than there is a risk that i damage something. i could use the interface for manually dropping the tip. i could try to find the function for doing it in python code