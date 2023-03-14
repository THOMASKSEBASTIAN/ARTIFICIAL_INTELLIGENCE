statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }

def online_count(statuses):
    count=0
    key=statuses.values()
    for i in key:
        if i=="online":
            count=count+1
    return count

print(online_count(statuses))