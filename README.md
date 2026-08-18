Task Prioritizer by Bethiah Peirce

This tool helps the user determine what tasks to work on first.
After adding each task with its due date, effort level, and impact on final
grade, the app uses Claude to rank which should be compleated first.

## Why I built this
I built this tool so I could expand my knowlege on using LLM API in my programming.
It was interesting to gain more experience with how AI is being used today in
the workplace. I also wanted to see how well AI was able to reason through 
prioritization tradeoffs, an importance skill that product and project managers
need to control a backlog of tasks. I am now able to compare my own decision 
making processes with Claude's and test which is more realistic and achievable.

## How it works
1. Plug in information about an assignment or task, providing its due date,
effort level, and importance to your grade, then add it to the task list.
2. The app calculates how many days are left until each assignment is due.
3. After you hit the Prioritize button, the data is sent to Claude, who will
reason the tradeoffs and returns a ranked list of what to compleate first along
with explanations.

## Built with
- Python
- Streamlit
- Anthropic Claude APIt

## Running Locally
1. Clone this repo
2. Install dependencies (requirements.txt)
3. Add your own Anthropic API key
    - Create a '.env' file in the project folder
    - Add this line: `ANTHROPIC_API_KEY=your-key-here`
4.  Run the app

## What I Learned
Similarly to what I do when reasoning my task compleation in real life, I found
that Claude often prioritizes due date over everything else. It will consider the due dates,
and in almost every case it will decide that the most important task is the one due soonest.
It also prioritized compleating tasks that took less effort first, as Clause also
decided that getting tasks finished as fast as possible was better than slowly
working on the largest assignment first.