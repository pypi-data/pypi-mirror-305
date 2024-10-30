# DateKeeper 

## What is this? 
This is a **simple** library for storing and viewing events.

## Quick Guide 
```python
edit = Edit()
check = Check
edit.add("Name event", "Description event", "start date (example: 2024-10-28 10:00)", "end date(example: 2024-10-30 20:00)")
check.history()
```
Great job adding your first event. 

---

### Using
Delete event (To find out the ID use the command: `history`. 
```python
edit.delete(id)
```
Reading events in different ways
```python
check.history() #All events.
check.today() #Events for today.
check.now() #Events that are happening at this hour.
check.archive() #Events that have expired.
```
---
## Developer 
my website: soon