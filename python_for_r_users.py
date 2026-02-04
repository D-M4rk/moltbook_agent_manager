"""
Python Data Science Tutorial for R Programmers
===============================================

This script covers Python fundamentals with comparisons to R.
Run sections independently or the whole script.

Author: Databot
Date: February 2, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("=" * 80)
print("PYTHON FOR R USERS - Interactive Tutorial")
print("=" * 80)


# ==============================================================================
# LESSON 1: BASIC DATA TYPES
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 1: BASIC DATA TYPES")
print("=" * 80)

# In R: x <- 5
# In Python: x = 5 (no <- operator!)
agent_name = "CodeWizard"  # character in R
karma_points = 150  # integer in R
average_likes = 12.5  # numeric in R
is_active = True  # logical in R (note: capital T!)

print(f"\nAgent: {agent_name}")
print(f"Karma: {karma_points}")
print(f"Average Likes: {average_likes}")
print(f"Active: {is_active}")

# Python has f-strings (like glue in R)
# R: glue("Agent: {agent_name}")
# Python: f"Agent: {agent_name}"


# ==============================================================================
# LESSON 2: COLLECTIONS (Lists vs Vectors)
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 2: COLLECTIONS")
print("=" * 80)

# LISTS (like R's list(), but 0-indexed!)
# R: agents <- c("CodeWizard", "MemeLord", "Philosopher")
agents = ["CodeWizard", "MemeLord", "Philosopher"]

print("\n📋 Python Lists vs R Vectors:")
print(f"Python list: {agents}")
print(f"First element: agents[0] = {agents[0]}")  # R: agents[1]
print(f"Last element: agents[-1] = {agents[-1]}")  # R: tail(agents, 1)
print(f"Length: len(agents) = {len(agents)}")  # R: length(agents)

# DICTIONARIES (like R's named list)
# R: agent <- list(name = "CodeWizard", karma = 150, followers = 42)
agent_profile = {
    "name": "CodeWizard",
    "karma": 150,
    "followers": 42,
    "personality": "Analytical"
}

print("\n📖 Python Dictionary vs R Named List:")
print(f"Python dict: {agent_profile}")
print(f"Access value: agent_profile['karma'] = {agent_profile['karma']}")  # R: agent$karma or agent[["karma"]]


# ==============================================================================
# LESSON 3: CONTROL FLOW
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 3: CONTROL FLOW")
print("=" * 80)

# IF STATEMENTS (similar to R, but note the colon and indentation!)
# R uses {} for blocks, Python uses indentation
karma = 150

if karma >= 100:
    status = "Elite Agent"  # Indentation matters!
elif karma >= 50:  # R: else if
    status = "Active Agent"
else:
    status = "New Agent"

print(f"\n✓ IF statements: With {karma} karma, status = '{status}'")

# FOR LOOPS (very similar to R)
# R: for (agent in agents) { print(agent) }
print("\n✓ FOR loops:")
for agent in agents:
    print(f"  - {agent} is ready!")

# Python's range() is like R's seq()
# R: for (i in 1:5) { print(i) }
print("\nRange example (R's seq equivalent):")
for i in range(1, 6):  # Note: range(1, 6) gives 1,2,3,4,5 (excludes 6!)
    print(f"  Post #{i}")

# LIST COMPREHENSION (like R's sapply/lapply, but cleaner!)
# R: sapply(1:5, function(x) x^2)
squares = [x**2 for x in range(1, 6)]
print(f"\nList comprehension: [x**2 for x in range(1, 6)] = {squares}")

# With filtering (like R's Filter())
# R: karma_scores[karma_scores > 100]
karma_scores = [100, 150, 75, 200, 50]
elite = [score for score in karma_scores if score >= 100]
print(f"Filtered list: {elite}")


# ==============================================================================
# LESSON 4: FUNCTIONS
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 4: FUNCTIONS")
print("=" * 80)

# R: calculate_engagement <- function(likes, followers) { ... }
def calculate_engagement_rate(likes, followers):
    """
    Calculate engagement rate as a percentage.
    
    Similar to R function:
    calculate_engagement_rate <- function(likes, followers) {
        if (followers == 0) return(0)
        rate <- (likes / followers) * 100
        round(rate, 2)
    }
    """
    if followers == 0:
        return 0
    rate = (likes / followers) * 100
    return round(rate, 2)

def create_post_message(agent_name, topic, emoji="🤖"):
    """Function with default argument (like R's default parameters)."""
    return f"{emoji} {agent_name} is posting about: {topic}"


rate = calculate_engagement_rate(50, 200)
message = create_post_message("CodeWizard", "Python Tips")

print(f"\n✓ Function result: {rate}%")
print(f"✓ Message: {message}")


# ==============================================================================
# LESSON 5: NUMPY (like R's base vector operations)
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 5: NUMPY - Python's Answer to R Vectors")
print("=" * 80)

# NumPy arrays are like R's numeric vectors
# R: karma <- c(150, 200, 120, 180, 95)
karma_array = np.array([150, 200, 120, 180, 95])

print("\n📊 NumPy Arrays (like R vectors):")
print(f"Array: {karma_array}")

# Vectorized operations (just like R!)
# R: karma * 2
print(f"Double all: {karma_array * 2}")

# R: karma + 50
print(f"Add 50 to all: {karma_array + 50}")

# R: sqrt(karma)
print(f"Square root: {np.sqrt(karma_array).round(2)}")

# Statistics (similar to R)
print(f"\n📈 Statistics:")
print(f"mean(karma): {karma_array.mean()}")  # R: mean(karma)
print(f"sd(karma): {karma_array.std():.2f}")  # R: sd(karma)
print(f"median(karma): {np.median(karma_array)}")  # R: median(karma)
print(f"sum(karma): {karma_array.sum()}")  # R: sum(karma)

# Boolean indexing (like R's logical indexing)
# R: karma[karma > 150]
high_karma = karma_array[karma_array > 150]
print(f"\nBoolean indexing karma[karma > 150]: {high_karma}")


# ==============================================================================
# LESSON 6: PANDAS (Python's dplyr/tidyverse)
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 6: PANDAS - Python's Answer to dplyr/tidyverse")
print("=" * 80)

# Create a DataFrame (like R's data.frame or tibble)
# R: agent_data <- tibble(
#       agent_name = c("CodeWizard", "MemeLord", ...),
#       karma = c(150, 200, ...),
#       ...
#     )

agent_data = pd.DataFrame({
    "agent_name": ["CodeWizard", "MemeLord", "Philosopher", "ScienceNerd", "CreativeSoul"],
    "karma": [150, 200, 120, 180, 95],
    "followers": [42, 68, 35, 55, 28],
    "posts_count": [15, 25, 12, 18, 8],
    "personality": ["Analytical", "Humorous", "Thoughtful", "Factual", "Artistic"]
})

print("\n📊 DataFrame (like R's tibble):")
print(agent_data)

# EXPLORING DATA
print("\n" + "-" * 80)
print("6.1: EXPLORING DATA (like summary(), str(), glimpse())")
print("-" * 80)

# R: head(agent_data)
print("\nhead(agent_data):")
print(agent_data.head())

# R: summary(agent_data)
print("\nsummary(agent_data) - describe():")
print(agent_data.describe())

# R: str(agent_data)
print("\nstr(agent_data) - info():")
print(agent_data.info())


# SELECTING COLUMNS
print("\n" + "-" * 80)
print("6.2: SELECTING COLUMNS (like select())")
print("-" * 80)

# R: select(agent_data, agent_name, karma)
# Python: agent_data[["agent_name", "karma"]]
print("\nselect(agent_data, agent_name, karma):")
print(agent_data[["agent_name", "karma"]])


# FILTERING ROWS
print("\n" + "-" * 80)
print("6.3: FILTERING ROWS (like filter())")
print("-" * 80)

# R: filter(agent_data, karma > 150)
# Python: agent_data[agent_data["karma"] > 150]
print("\nfilter(agent_data, karma > 150):")
high_karma_agents = agent_data[agent_data["karma"] > 150]
print(high_karma_agents)

# R: filter(agent_data, karma > 100 & followers > 40)
# Python: agent_data[(agent_data["karma"] > 100) & (agent_data["followers"] > 40)]
print("\nfilter(agent_data, karma > 100 & followers > 40):")
popular = agent_data[(agent_data["karma"] > 100) & (agent_data["followers"] > 40)]
print(popular)


# MUTATING (CREATING NEW COLUMNS)
print("\n" + "-" * 80)
print("6.4: MUTATING (like mutate())")
print("-" * 80)

# R: mutate(agent_data, engagement_rate = (posts_count / followers) * 100)
# Python: agent_data["engagement_rate"] = ...
agent_data["engagement_rate"] = (agent_data["posts_count"] / agent_data["followers"] * 100).round(2)

# R: mutate(agent_data, status = case_when(...))
# Python: agent_data["status"] = agent_data["karma"].apply(lambda x: ...)
agent_data["status"] = agent_data["karma"].apply(
    lambda x: "Elite" if x >= 150 else "Active" if x >= 100 else "New"
)

print("\nmutate(agent_data, engagement_rate, status):")
print(agent_data)


# SORTING
print("\n" + "-" * 80)
print("6.5: SORTING (like arrange())")
print("-" * 80)

# R: arrange(agent_data, desc(engagement_rate))
# Python: agent_data.sort_values("engagement_rate", ascending=False)
print("\narrange(agent_data, desc(engagement_rate)):")
sorted_agents = agent_data.sort_values("engagement_rate", ascending=False)
print(sorted_agents[["agent_name", "engagement_rate"]])


# GROUPING AND SUMMARIZING
print("\n" + "-" * 80)
print("6.6: GROUPING (like group_by() %>% summarize())")
print("-" * 80)

# R: agent_data %>%
#      group_by(status) %>%
#      summarize(
#        avg_karma = mean(karma),
#        total_posts = sum(posts_count),
#        count = n()
#      )

print("\ngroup_by(status) %>% summarize(...):")
status_summary = agent_data.groupby("status").agg({
    "karma": "mean",
    "posts_count": "sum",
    "agent_name": "count"
})
status_summary.columns = ["avg_karma", "total_posts", "count"]
print(status_summary)


# PIPING (METHOD CHAINING)
print("\n" + "-" * 80)
print("6.7: PIPING (like %>% in R)")
print("-" * 80)

# R: agent_data %>%
#      filter(karma > 100) %>%
#      select(agent_name, karma, followers) %>%
#      arrange(desc(karma))

# Python: Use method chaining (similar to %>%)
print("\nPython method chaining (like %>%):")
result = (
    agent_data[agent_data["karma"] > 100]
    [["agent_name", "karma", "followers"]]
    .sort_values("karma", ascending=False)
)
print(result)


# ==============================================================================
# LESSON 7: VISUALIZATION (ggplot2 vs matplotlib)
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 7: VISUALIZATION (matplotlib - like base R plots)")
print("=" * 80)

# Note: For ggplot2-style plots in Python, use plotnine
# But matplotlib is the standard, like base R graphics

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Agent Analytics Dashboard", fontsize=16, fontweight="bold")

# 1. Bar plot (like barplot() in R)
axes[0, 0].bar(agent_data["agent_name"], agent_data["karma"], color="steelblue")
axes[0, 0].set_title("Karma Scores by Agent")
axes[0, 0].set_ylabel("Karma")
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Scatter plot (like plot() in R)
axes[0, 1].scatter(
    agent_data["followers"], 
    agent_data["posts_count"],
    s=agent_data["karma"],  # size proportional to karma
    alpha=0.6, 
    color="coral"
)
axes[0, 1].set_title("Followers vs Posts (size = karma)")
axes[0, 1].set_xlabel("Followers")
axes[0, 1].set_ylabel("Posts Count")

# 3. Pie chart
status_counts = agent_data["status"].value_counts()
axes[1, 0].pie(
    status_counts.values, 
    labels=status_counts.index,
    autopct='%1.1f%%',
    colors=["#ff9999", "#66b3ff", "#99ff99"]
)
axes[1, 0].set_title("Status Distribution")

# 4. Horizontal bar chart
sorted_data = agent_data.sort_values("engagement_rate")
axes[1, 1].barh(sorted_data["agent_name"], sorted_data["engagement_rate"], color="mediumseagreen")
axes[1, 1].set_title("Engagement Rate by Agent")
axes[1, 1].set_xlabel("Engagement Rate (%)")

plt.tight_layout()
plt.savefig("agent_analytics_dashboard.png", dpi=150, bbox_inches="tight")
print("\n✓ Dashboard saved as 'agent_analytics_dashboard.png'")
plt.show()


# ==============================================================================
# LESSON 8: REAL-WORLD EXAMPLE - TIME SERIES ANALYSIS
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 8: REAL-WORLD EXAMPLE - Analyzing Agent Activity Over Time")
print("=" * 80)

# Create time series data (like in R with lubridate)
np.random.seed(42)
dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]

activity_log = pd.DataFrame({
    "date": pd.to_datetime(dates),
    "agent_name": np.random.choice(["CodeWizard", "MemeLord", "Philosopher"], 30),
    "action": np.random.choice(["post", "comment", "like"], 30),
    "karma_change": np.random.randint(-5, 20, 30)
})

print("\n📊 Activity Log (first 10 rows):")
print(activity_log.head(10))

# Time series aggregation (like R's dplyr with dates)
print("\n📈 Daily Activity Summary:")
daily_summary = (
    activity_log
    .groupby(activity_log["date"].dt.date)
    .agg({
        "action": "count",
        "karma_change": "sum"
    })
    .rename(columns={"action": "total_actions", "karma_change": "karma_gained"})
)
print(daily_summary.head(10))

# Agent performance summary
print("\n🏆 Agent Performance Summary:")
agent_summary = (
    activity_log
    .groupby("agent_name")
    .agg({
        "action": "count",
        "karma_change": ["sum", "mean", "std"]
    })
)
agent_summary.columns = ["total_actions", "total_karma", "avg_karma_per_action", "karma_volatility"]
print(agent_summary)


# ==============================================================================
# LESSON 9: KEY DIFFERENCES SUMMARY
# ==============================================================================
print("\n" + "=" * 80)
print("LESSON 9: KEY DIFFERENCES - R vs Python Quick Reference")
print("=" * 80)

differences = """
╔═══════════════════════╦═══════════════════════════╦═══════════════════════════╗
║ OPERATION             ║ R                         ║ PYTHON                    ║
╠═══════════════════════╬═══════════════════════════╬═══════════════════════════╣
║ Assignment            ║ x <- 5                    ║ x = 5                     ║
║ Comment               ║ # comment                 ║ # comment                 ║
║ Logical AND           ║ &                         ║ &                         ║
║ Logical OR            ║ |                         ║ |                         ║
║ Indexing              ║ vec[1] (1-indexed)        ║ list[0] (0-indexed)       ║
║ Last element          ║ tail(vec, 1)              ║ list[-1]                  ║
║ Length                ║ length(vec)               ║ len(list)                 ║
║ Range                 ║ 1:10                      ║ range(1, 11)              ║
║ String concat         ║ paste0(a, b)              ║ f"{a}{b}" or a + b        ║
║ True/False            ║ TRUE/FALSE                ║ True/False                ║
║ NULL                  ║ NULL                      ║ None                      ║
║ Print                 ║ print(x)                  ║ print(x)                  ║
║ Data frame            ║ data.frame(), tibble()    ║ pd.DataFrame()            ║
║ Select columns        ║ select(df, col1, col2)    ║ df[["col1", "col2"]]      ║
║ Filter rows           ║ filter(df, x > 5)         ║ df[df["x"] > 5]           ║
║ Add column            ║ mutate(df, y = x * 2)     ║ df["y"] = df["x"] * 2     ║
║ Group by              ║ group_by(df, x)           ║ df.groupby("x")           ║
║ Pipe                  ║ %>%                       ║ Method chaining           ║
║ Summary stats         ║ summary(x)                ║ x.describe()              ║
║ Apply function        ║ sapply(x, func)           ║ [func(i) for i in x]      ║
║ Read CSV              ║ read_csv("file.csv")      ║ pd.read_csv("file.csv")   ║
║ Write CSV             ║ write_csv(df, "file.csv") ║ df.to_csv("file.csv")     ║
╚═══════════════════════╩═══════════════════════════╩═══════════════════════════╝
"""

print(differences)


# ==============================================================================
# FINAL TIPS
# ==============================================================================
print("\n" + "=" * 80)
print("🎓 FINAL TIPS FOR R USERS LEARNING PYTHON")
print("=" * 80)

tips = """
1. INDENTATION MATTERS! Python uses indentation instead of {} for blocks
   
2. ZERO-INDEXING: Python lists/arrays start at 0, not 1
   R: vec[1]  → Python: list[0]
   
3. METHOD CHAINING: Instead of %>%, chain methods:
   df.filter(...).select(...).sort_values(...)
   
4. MULTIPLE LIBRARIES: 
   - NumPy = base R vector operations
   - Pandas = dplyr/tidyverse
   - Matplotlib = base R graphics
   - Plotnine = ggplot2 (if you want ggplot2-style!)
   
5. LIST COMPREHENSIONS: Python's powerful alternative to apply functions
   [x**2 for x in range(10) if x % 2 == 0]
   
6. DICTIONARIES: Like named lists, but use [] not $
   R: agent$name  → Python: agent["name"]
   
7. TRUE/FALSE: Capitalized in Python (True/False vs TRUE/FALSE)

8. NONE vs NULL: Python uses None instead of NULL

9. RANGE: range(1, 10) gives 1-9, not 1-10!
   R: 1:10 → Python: range(1, 11)

10. HELP: 
    R: ?mean  → Python: help(mean) or mean?
"""

print(tips)

print("\n" + "=" * 80)
print("✅ Tutorial Complete! Practice with your Moltbook project data!")
print("=" * 80)
print("\nNext steps:")
print("1. Run this script: python python_for_r_users.py")
print("2. Modify the examples with your own data")
print("3. Check out plotnine for ggplot2-style graphics")
print("4. Explore scikit-learn for machine learning (like caret in R)")
