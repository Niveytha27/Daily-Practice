"""
Generate Chat Summary for the conversations
1. CollectionNumber
2. ConversationNumber
3. ChatStarter
4. ChatCloser
5. ChatStartTime
6. ChatEndTime
7. ChatDuration(seconds)

The printed output fields should be aligned properly.
"""

# Imports


# Core Logic
def summarizer(chatdata):
    pass

# Driver
with open('../Data/003_ChatSummary.txt') as f:
    chatdata = f.readlines()
    summarizer(chatdata)
    
