# Whatstat
# Text analysis of whatsapp texts:
Used info in websites to make a python code that works with whatsapp.txt chat history between two people.

1) Get raw data- Email chat history to yourself (Get Media omitted version)

2) Clean data- Get rid of i) <media omitted> and ii) all lines that do not follow expected order (as required by code)
(This can also be done by running code anyway and seeing which lines throws error )

3) Fill inputs and run code: Three input required in code, .txt file name, your name, and senders name as mentioned in the .txt file

4) Output- The code outputs 1) A .csv file per person (counted_XXX.csv)with dates in one column and number of messages sent that day by this person in another column 2) A XXX_messages.txt that has only the content of messages in it no dates or names--> This can be used later in worlde.net etc to get wordgrams or NLP info.

5) Debug- Most debugging can be done by looking at error messages. Typical issues are:
i) input .txt file has a line that does not conform to expected form
ii) File to write to is still open

 Icarus
