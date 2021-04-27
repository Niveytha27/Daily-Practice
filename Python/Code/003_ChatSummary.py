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
import re
from datetime import datetime


# Core Logic
def summarizer(chatdata):
    sub_lst = []
    main_lst = []
    for idx, elem in enumerate(chatdata):
        elem = str(chatdata[(idx + 1) % len(chatdata)])
        if re.match(r"^[*]+", elem):
            main_lst.append(sub_lst)
            sub_lst = []
        elif re.match(r"([\s\w]+)|([\w]+)", elem):
            sub_lst.append(elem)
    print_values(main_lst)


def print_values(main_lst):
    print('Collection Number   |' + 'Conversation Number |' + 'Chat Starter        |' + 'Chat Closer         |' +
          'Chat Start time     |' + 'Chat End time       |' + 'Chat Duration(secs) ')

    chat_dict = {}
    for sub_lst in main_lst:
        chat_info = []
        for item in sub_lst:
            if re.search("Collec*", item):
                lst1 = re.split(r"[:|\n]", item)

                chat_dict["Collection Number"] = int(lst1[1])
                chat_dict["Conversation Number"] = int(lst1[3])

            if re.search('USER|EXPERT', item):
                lst2 = re.split(r"[(+)]", item)
                chat_info.append(lst2)

        chat_dict["Chat Starter"] = chat_info[0][0]
        chat_dict["Chat Closer"] = chat_info[-1][0]
        chat_dict["Chat Start time"] = chat_info[0][1]
        chat_dict["Chat End time"] = chat_info[-1][1]
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(chat_dict["Chat Start time"], fmt)
        d2 = datetime.strptime(chat_dict["Chat End time"], fmt)
        chat_dict["Chat Duration"] = int((d2 - d1).total_seconds())
        result = "|".join(f"{value}".ljust(20) for value in chat_dict.values())
        print(result)


# Driver
with open('../Data/003_ChatSummary.txt') as f:
    chatdata = f.readlines()
    summarizer(chatdata)
