# ACEProject Stats Report
A Python cron job to generate project report from tasks in a project on [AceProject](https://www.aceproject.com/) and send the report to project stakeholders.

### Background
AceProject lacks in many features I needed in their reports at work. Many of the features in this script and how they work are based on what were needed at my work to include in a number of project reports which would otherwise be done and sent manually. I wrote this script to save myself from wasting hours preparing all these reports manually every week for multiple projects to different stakeholders.

### Features in Report
- Gantt chart and tasks statuses
- Simple calculation of efforts
- An effort chart that resembles a burndown chart
- A set of basic stats about the tasks within a defined period
- Configurable arguments for so that each project report can have different settings (date range, emails, etc)
- Uses Sendgrid to send the report email
- A word cloud of the topics being discussed in the tasks in the project
- Report email is responsive and works on both desktop (particularly Outlook), web and mobile mail clients

### Screenshot
![Screenshot of an example email report](https://i.imgur.com/pDxRBbl.png)

### Usage
```
docker build -t aceproject_report .
docker run -d aceproject_report
```

### Notes
I've initially experimented with this idea in a Jupyter notebook and ran it manually. Soon, I decided that I should convert it to a Python script which I can then leave it to a scheduled cron job to run it automatically.
