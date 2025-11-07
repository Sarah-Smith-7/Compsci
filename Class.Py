"""
Optimized Study Schedule for Your Input
"""

from datetime import datetime

# Convert time to minutes
def t2m(t): 
    return int(datetime.strptime(t.strip().upper(), "%I:%M %p").strftime("%H%M"))

DAYS = "MTWRF"
DAY_MAP = {d: i for i, d in enumerate(DAYS)}

class Block:
    def __init__(self, name, day, start, end, prio=100):
        self.name = name
        self.day = day.upper()
        self.start = t2m(start)
        self.end = t2m(end)
        self.prio = prio
        self.didx = DAY_MAP[self.day[0]] if self.day[0] in DAY_MAP else -1

    def conflict(self, other):
        if self.didx != other.didx: return False
        return self.start < other.end and self.end > other.start

    def __repr__(self):
        st = f"{self.start//100:02d}:{self.start%100:02d}"
        et = f"{self.end//100:02d}:{self.end%100:02d}"
        return f"{st}-{et} {self.name}"

# === YOUR INPUT ===
classes = [
    Block("Calc", "M", "9:30 AM", "10:45 AM"),
    Block("Calc", "W", "9:30 AM", "10:45 AM"),
    Block("Calc", "F", "9:30 AM", "10:45 AM"),
    Block("English", "T", "1:00 PM", "2:15 PM"),
    Block("English", "R", "1:00 PM", "2:15 PM"),
    Block("Physics", "M", "11:00 AM", "12:30 PM")
]

# Possible study times (you gave start times only — assuming 1-hour blocks unless specified)
study_options = [
    Block("Study", "F", "10:00 AM", "11:00 AM", prio=8),  # F 10:00 AM → 1 hr
    Block("Study", "W", "2:00 PM", "3:00 PM", prio=7)     # W 2:00–3:00 PM
]

# === SCHEDULING ===
from itertools import product

best = None
best_score = -1

# Try: include or skip each study block
for combo in product([False, True], repeat=len(study_options)):
    candidate = classes.copy()
    for i, use in enumerate(combo):
        if use:
            candidate.append(study_options[i])
    
    # Check for conflicts
    if any(a.conflict(b) for i,a in enumerate(candidate) for b in candidate[i+1:]):
        continue
    
    # Score: total study priority (classes = 100, don't count)
    score = sum(b.prio for b in candidate if b.prio <= 10)
    if score > best_score:
        best_score = score
        best = candidate

# === OUTPUT ===
print("BEST STUDY SCHEDULE\n" + "="*40)
if best:
    total_study_prio = sum(b.prio for b in best if b.prio <= 10)
    print(f"Total Study Priority: {total_study_prio}\n")
    
    for d in range(5):
        day_name = ['Monday','Tuesday','Wednesday','Thursday','Friday'][d]
        day_blocks = [b for b in best if b.didx == d]
        if not day_blocks: continue
        day_blocks.sort(key=lambda x: x.start)
        print(f"{day_name}:")
        for b in day_blocks:
            print(f"  {b}")
else:
    print("No valid study time could be added.")
