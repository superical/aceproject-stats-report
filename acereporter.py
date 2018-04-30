#!/usr/bin/python
# coding: utf-8

# In[ ]:

#get_ipython().magic('matplotlib inline')

import datetime
import gantt
import numpy as np
import pandas as pd
import math

from scipy import stats
import statsmodels.api as sm
import calendar
import re
from enum import Enum
from io import BytesIO
import base64
import os

import json
from pprint import pprint
import requests


# In[ ]:

import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--proj', nargs='?', type=int)
argparser.add_argument('--targetprof', nargs='?', const=1, default=1, type=float)
argparser.add_argument('--headcount', nargs='?', const=1, default=1, type=float)
argparser.add_argument('--rcpts', nargs='+', type=str)

argparser.add_argument('--BURNDOWN_LAST_NUM_DAYS', nargs='?', const=7, default=7, type=int)
argparser.add_argument('--GANTT_PAST_NUM_DAYS', nargs='?', const=14, default=14, type=int)
argparser.add_argument('--GANTT_FUTURE_NUM_DAYS', nargs='?', const=15, default=15, type=int)

argparser.add_argument('--PLOT_PRIORITY_COUNT_LAST_NUM_DAYS', nargs='?', const=90, default=90, type=int)
argparser.add_argument('--PLOT_PRIORITY_DAYSTAKEN_LAST_NUM_DAYS', nargs='?', const=180, default=180, type=int)
argparser.add_argument('--PLOT_DAY_CREATED_LAST_NUM_DAYS', nargs='?', const=90, default=90, type=int)
argparser.add_argument('--PLOT_WORDCLOUD_LAST_NUM_DAYS', nargs='?', const=7, default=7, type=int)

argparser.add_argument('--TASKS_PENDING_UAT_MIN_DAYS', nargs='?', const=3, default=3, type=int)

argparser.add_argument('--aceacc', nargs='?', default=os.environ.get('ACEREPORT_ACC_ID'), type=str)
argparser.add_argument('--aceid', nargs='?', default=os.environ.get('ACEREPORT_ACE_ID'), type=str)
argparser.add_argument('--acepw', nargs='?', default=os.environ.get('ACEREPORT_ACE_PW'), type=str)

argparser.add_argument('--cloudconvert-key', nargs='?', default=os.environ.get('ACEREPORT_CLOUDCONVERT_API_KEY'), type=str)
argparser.add_argument('--sendgrid-key', nargs='?', default=os.environ.get('ACEREPORT_SENDGRID_API_KEY'), type=str)

argparser.add_argument('--convert-svg', dest='CONVERT_SVG2PNG', action='store_true')
argparser.add_argument('--no-convert-svg', dest='CONVERT_SVG2PNG', action='store_false')
argparser.set_defaults(CONVERT_SVG2PNG=True)

argparser.add_argument('--notebook-mode', dest='notebook_mode', action='store_true')
argparser.set_defaults(notebook_mode=False)

argparser.add_argument('--hide-effortchart', dest='hide_effortchart', action='store_true')
argparser.set_defaults(hide_effortchart=False)

argparser.add_argument('--sender-name', nargs='?', default=os.environ.get('EMAIL_SENDER_NAME'), type=str)
argparser.add_argument('--sender-email', nargs='?', default=os.environ.get('EMAIL_SENDER_ADDR'), type=str)

#args = argparser.parse_args(args='--notebook-mode')
args = argparser.parse_args()

print(args)

if args.proj is None or args.aceid is None or args.acepw is None or args.rcpts is None or len(args.rcpts) < 1:
    raise ValueError('Parameter proj, aceid, acepw or rcpts cannot be undefined.')


# In[ ]:

PROJECT_ID = args.proj
REPORT_RECIPIENTS = args.rcpts

"""
if PROJECT_ID == 46:
    TARGET_PROFICIENCY_LEVEL = 0.3
    NUM_HEADCOUNT = 3
elif PROJECT_ID == 35:
    TARGET_PROFICIENCY_LEVEL = 0.3
    NUM_HEADCOUNT = 2
else:
    TARGET_PROFICIENCY_LEVEL = 1
    NUM_HEADCOUNT = 1
"""

TARGET_PROFICIENCY_LEVEL = args.targetprof
NUM_HEADCOUNT = args.headcount

BURNDOWN_LAST_NUM_DAYS = args.BURNDOWN_LAST_NUM_DAYS
GANTT_PAST_NUM_DAYS = args.GANTT_PAST_NUM_DAYS
GANTT_FUTURE_NUM_DAYS = args.GANTT_FUTURE_NUM_DAYS

PLOT_PRIORITY_COUNT_LAST_NUM_DAYS = args.PLOT_PRIORITY_COUNT_LAST_NUM_DAYS
PLOT_PRIORITY_DAYSTAKEN_LAST_NUM_DAYS = args.PLOT_PRIORITY_DAYSTAKEN_LAST_NUM_DAYS
PLOT_DAY_CREATED_LAST_NUM_DAYS = args.PLOT_DAY_CREATED_LAST_NUM_DAYS
PLOT_WORDCLOUD_LAST_NUM_DAYS = args.PLOT_WORDCLOUD_LAST_NUM_DAYS

TASKS_PENDING_UAT_MIN_DAYS = args.TASKS_PENDING_UAT_MIN_DAYS

ACE_ACCID = args.aceacc
ACE_USERID = args.aceid
ACE_PASSWORD = args.acepw

CLOUDCONVERT_API_KEY = args.cloudconvert_key
SENDGRID_API_KEY = args.sendgrid_key

NOTEBOOK_MODE = args.notebook_mode

HIDE_EFFORTCHART = args.hide_effortchart

EMAIL_SENDER_NAME = args.sender_name
EMAIL_SENDER_ADDR = args.sender_email

CONVERT_SVG2PNG = args.CONVERT_SVG2PNG
APP_VERSION = '0.2.2'


# In[ ]:

if NOTEBOOK_MODE is False:
    import matplotlib
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
import seaborn as sns


# In[ ]:

class ApiRequest:
    
    GUID = None
    resultFormat = 'json'
    apiUrl = 'http://api.aceproject.com/?'
    
    def __init__(self, ace_accid, ace_userid, ace_password):
        if type(self).GUID == None:
            res = self.get('login', {'accountid': ace_accid, 'username': ace_userid, 'password': ace_password})[0]
            type(self).GUID = res['GUID']
    
    def get(self, fct, params=None):
        paramStr = ''
        if params != None:
            for paramKey in params.keys():
                paramStr += '&{}={}'.format(paramKey, params[paramKey])
        requestUrl = '{}fct={}&guid={}&format={}{}'.format(self.apiUrl, fct, type(self).GUID, self.resultFormat, paramStr)
        #print(requestUrl)
        res = requests.get(requestUrl).text
        res = json.loads(res)
        if res['status'] == 'fail':
            print('API Request Error to', requestUrl, ':')
            pprint(res['results'])
            return False
        return res['results']


# In[ ]:

class BaseObject:
    
    request = None
    
    def __init__(self):
        self.request = ApiRequest(ACE_ACCID, ACE_USERID, ACE_PASSWORD)


# In[ ]:

class TaskStatus(Enum):
    ON_HOLD = 'On Hold'
    TO_DO = 'To Do'
    TO_DEBUG = 'To Debug'
    READY_FOR_QAT = 'Ready for QAT Review'
    DEPLOY_TO_UAT = 'Deploy to UAT'
    READY_FOR_UAT = 'Ready for UAT Review'
    UAT_PASSED = 'UAT Passed'
    DEPLOY_TO_PRODUCTION = 'Deploy to Production'
    REQUIREMENT_GATHER = 'Requirement Gathering'
    IN_PROGRESS = 'In Progress'
    PRODUCTION_DEPLOYMENT_COMPLETED = 'Production Deployment Completed'
    COMPLETED = 'Completed'
    ARCHIVED = 'Archived'
    UNKNOWN = -1
    
    @staticmethod
    def getCompletedStatuses():
        return [TaskStatus.COMPLETED, TaskStatus.ARCHIVED]
    
    @staticmethod
    def getStatus(statusStr):
        try:
            return TaskStatus(statusStr)
        except Exception:
            return TaskStatus.UNKNOWN
        
    
#test = TaskStatus.ON_HOLD
#print(test.value)

#TaskStatus.getStatus('Completed')


# In[ ]:

class Task(BaseObject):
    
    TASK_ID = None
    
    hours_diff = 12
    min_effort = 5
    
    _history = None
    _comments = None
    
    def __init__(self, task_id=None, **kwargs):
        super().__init__()
        
        if task_id != None:
            self.TASK_ID = task_id
            params = {'taskid': task_id}
            res = self.request.get('gettasks', params)[0]
        else:
            if len(kwargs['data']) < 1:
                raise ValueError('Task ID is None. So data param cannot be empty.')
            res = kwargs['data']
        
        #pprint(res)
        
        #self.task_no = int(res['TASK_NUMBER'])
        
        for resKey in res.keys():
            val = res[resKey]
            if resKey[:5] == 'DATE_':
                val = self.convertFieldToDate(val)
                    
            setattr(self, resKey, val)
     
    def convertFieldToDate(self, value):
        dateMatch = re.match('/Date\((\d+)\)/', value)
        if (bool(dateMatch) == True):
            return datetime.datetime.fromtimestamp(int(dateMatch.group(1))/1000.0) - datetime.timedelta(hours=self.hours_diff)
        return None
    
    def isCreatedOn(date):
        if self.DATE_TASK_CREATED.date() == date.date():
            return True
        return False
    
    @property
    def status(self):
        return TaskStatus.getStatus(self.TASK_STATUS_NAME)
    
    @property
    def effort(self):
        hours = self.ESTIMATED_TIME
        if hours == 0:
            hours = self.min_effort
        return hours
    
    @property
    def history(self):
        if self._history == None:
            params = {'taskid': self.TASK_ID}
            self._history = self.request.get('gettaskhistory', params)
            self._history.reverse()
            for hist in self._history:
                hist['DATE_CHANGED_DATE'] = self.convertFieldToDate(hist['DATE_CHANGED_DATE'])
        return self._history
    
    @property
    def comments(self):
        if self._comments == None:
            params = {'taskids': self.TASK_ID, 'plaintext': 'true'}
            self._comments = self.request.get('gettaskcomments', params)
            for comment in self._comments:
                comment['DATE_CHANGED_DATE'] = self.convertFieldToDate(comment['DATE_CHANGED_DATE'])
        return self._comments
    
    def getStatusOnDate(self, targetDate):
        historyList = self.history
        lastStatus = None
        if targetDate.date() >= self.history[0]['DATE_CHANGED_DATE'].date():
            for history in historyList:
                if history['MODIFICATION'] == 'Status' and history['DATE_CHANGED_DATE'].date() <= targetDate.date():
                    lastStatus = TaskStatus.getStatus(history['NEW_VALUE'])
        return lastStatus    
    
    def getStatusSinceDate(self, status):
        historyList = self.history
        sinceDate = None
        for history in historyList:
            if history['MODIFICATION'] == 'Status' and TaskStatus.getStatus(history['NEW_VALUE']) == status:
                if sinceDate == None or sinceDate < history['DATE_CHANGED_DATE']:
                    sinceDate = history['DATE_CHANGED_DATE']
        return sinceDate        
            
    
    def getCompletedDate(self):
        historyList = self.history
        if self.status == TaskStatus.COMPLETED:
            for history in historyList:
                if history['MODIFICATION'] == 'Status' and history['NEW_VALUE'] == TaskStatus.COMPLETED.value:
                    return history['DATE_CHANGED_DATE']
        return None       
    
    @staticmethod
    def createTaskFromData(taskData):
        return Task(data=taskData)
    
    


# In[ ]:

if False:
    task = Task(3395)
    pprint(task.history)
    status = task.getStatusOnDate(datetime.datetime.now()-datetime.timedelta(days=0))
    print(status)


# In[ ]:

class Project(BaseObject):

    projectId = None
    request = None
    _tasks = None
    _tasksRaw = None
    _projectName = None
    
    def __init__(self, projectId, numMembers=1, expectedProficiency=0.2, effortPerDay=8):
        super().__init__()
        
        self.projectId = projectId
        
        res = self.request.get('getprojectinfo', {'projectId': self.projectId})[0]
        self._projectName = res['PROJECT_NAME']
        
        self.numMembers = numMembers
        self.expectedProficiency = expectedProficiency
        self.effortPerDay = effortPerDay
    
    @property
    def dailyExpectedEffortToBurn(self):
        return self.numMembers * self.effortPerDay * self.expectedProficiency
    
    def getTasksCreatedBeforeDate(self, targetDate, inclusive=False):
        if inclusive == True:
            tasks = [task for task in self.tasks if task.DATE_TASK_CREATED.date() <= targetDate.date()]
        else:
            tasks = [task for task in self.tasks if task.DATE_TASK_CREATED.date() < targetDate.date()]
        return tasks
    
    def getTasksCreatedBetweenDates(self, startDate, endDate):
        params = {
            'FilterFirstDate': 'DATE_TASK_CREATED',
            'FilterFirstDateOperator': 3,
            'FilterFirstDateValue': startDate.strftime('%Y-%m-%d'),
            'FilterSecondDate': 'DATE_TASK_CREATED',
            'FilterSecondDateOperator': 1,
            'FilterSecondDateValue': endDate.strftime('%Y-%m-%d')
        }
        return self.getTasks(params)
        
    def getIncompletedTasksOnDate(self, targetDate):
        completedStatuses = TaskStatus.getCompletedStatuses()
        tasks = self.getTasksCreatedBeforeDate(targetDate, True)
        tasks = [task for task in tasks if task.DATE_TASK_MODIFIED.date() >= (targetDate-datetime.timedelta(days=182)).date() or task.status not in [TaskStatus.COMPLETED, TaskStatus.ARCHIVED]]
        incompletedTasks = []
        for task in tasks:
            taskStatus = task.getStatusOnDate(targetDate)
            if taskStatus not in completedStatuses:
                incompletedTasks.append(task)
        return incompletedTasks
    
    def getTaskObject(self, task_id):
        projTasks = self.tasks
        found = [task for task in projTasks if task.TASK_ID == task_id]
        if len(found) == 0:
            return None
        return found[0]
            
    def getTasks(self, params={}):
        if 'projectId' not in params:
            params['projectId'] = self.projectId
        res = self.request.get('gettasks', params)
        tasks = []
        for data in res:
            tasks.append(Task.createTaskFromData(data))        
        return res, tasks
    
    def getTasksRawData(self):
        self.tasks
        return self._tasksRaw
    
    @property
    def projectName(self):
        return self._projectName
    
    @property
    def tasks(self):
        if self._tasks == None:
            self._tasksRaw, self._tasks = self.getTasks()
        return self._tasks
    
 


# In[ ]:

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


# In[ ]:

def num_of_weekends(date1, date2):
    begin = date1
    end = date2
    diff = (end-begin).days
    day_of_week = begin.weekday()
    num_thur_fri = 2*(diff//7)
    for i in range(diff%7):
        if day_of_week in [5,6]:
            num_thur_fri += 1
        day_of_week = (day_of_week +1) %7
    return num_thur_fri


# In[ ]:

project = Project(PROJECT_ID, numMembers=NUM_HEADCOUNT, expectedProficiency=TARGET_PROFICIENCY_LEVEL) 
project.projectName


# In[ ]:

burndown_startDate = datetime.datetime.now()-datetime.timedelta(days=BURNDOWN_LAST_NUM_DAYS)
burndown_endDate = datetime.datetime.now()

effortToBurnPerDay = (project.numMembers * project.effortPerDay) * project.expectedProficiency

daily_tasks = []
daily_efforts = []
daily_completed = []
daily_created = []
daily_ideals = []
x_dates = []
x_labels = []

daily_relCreatedEffort = []
daily_relCompletedEffort = []

skipped_rdays = 0
total_workdays = 0

for rdate in daterange(burndown_startDate, burndown_endDate+datetime.timedelta(days=1)):
    if calendar.weekday(rdate.date().year, rdate.date().month, rdate.date().day) in [5, 6]:
        skipped_rdays += 1
        continue
    
    currDayTasks = project.getIncompletedTasksOnDate(rdate)
    currDayEffort = int(sum([task.effort for task in currDayTasks]))
    numCurDayTasks = len(currDayTasks)
    
    ytdTasks = project.getIncompletedTasksOnDate(rdate - datetime.timedelta(days=1+skipped_rdays))
    
    #Relative completed tasks from yesterday and today
    completedTasks = [task for task in ytdTasks if task.TASK_ID not in [task2.TASK_ID for task2 in currDayTasks]]
    numCompletedTasks = len(completedTasks)
    completedTasksEffort = sum([task.effort for task in completedTasks])
    
    # Backdate Completed Date to Actual End Date
    for task in completedTasks:
        if task.DATE_ACTUAL_END_DATE == None:
            continue
        if task.DATE_ACTUAL_END_DATE.date() < rdate.date():
            numWeeknds = num_of_weekends(task.DATE_ACTUAL_END_DATE, rdate)
            #backdateDays = min(len(daily_efforts), (rdate.date() - task.DATE_ACTUAL_END_DATE.date()).days)
            backdateDays = (rdate.date() - task.DATE_ACTUAL_END_DATE.date()).days
            backdateDays = max(0, backdateDays - numWeeknds)
            if backdateDays <= 0:
                continue
            if backdateDays >= len(daily_efforts):
                print('backdating task beyond chart period:', task.TASK_RESUME, backdateDays, rdate, numWeeknds)
                if len(daily_efforts) > 0:
                    #only backdate a task if this is not the first task
                    daily_efforts[0] -= task.effort
                    daily_ideals[0] -= task.effort
                    daily_tasks[0] -= 1
                    daily_completed[0] += 1
            else:    
                print('backdating task:', task.TASK_RESUME, backdateDays, rdate, numWeeknds)
                for idx, eff in enumerate(daily_efforts[-backdateDays:], start=len(daily_efforts)-backdateDays):
                    daily_efforts[idx] -= task.effort
                    daily_tasks[idx] -= 1

                daily_completed[-backdateDays] += 1
                
            numCompletedTasks -= 1
            
    
    createdTasks = [task for task in currDayTasks if task.TASK_ID not in [task2.TASK_ID for task2 in ytdTasks]]
    createdEffort = int(sum([task.effort for task in createdTasks]))
    
    if len(daily_ideals) == 0:
        currDayIdealEff = currDayEffort
    else:
        currDayIdealEff = max(0, daily_ideals[-1] - effortToBurnPerDay + createdEffort)

    daily_tasks.append(numCurDayTasks)
    daily_efforts.append(currDayEffort)
    daily_completed.append(numCompletedTasks)
    daily_created.append(len(createdTasks))
    daily_ideals.append(currDayIdealEff)
    x_dates.append(rdate)
    x_labels.append(rdate.date().strftime('%d %b'))
    
    daily_relCreatedEffort.append(createdEffort)
    daily_relCompletedEffort.append(completedTasksEffort)
    
    skipped_rdays = 0
    total_workdays += 1
    

# Data
burndown_df = pd.DataFrame({'id': np.arange(len(x_dates)), 'x': x_dates, 'daily_ideals': daily_ideals, 'daily_created': daily_created, 'daily_completed': daily_completed, 'daily_tasks': daily_tasks, 'daily_efforts': daily_efforts })



# In[ ]:

burndown_df


# In[ ]:




# In[ ]:

burndown_remaining_gradient = 0
burndown_ideals_gradient = 0
def plotBurndownChart(burndown_df):
    global burndown_remaining_gradient
    global burndown_ideals_gradient
    
    N = len(x_dates)
    ind = np.arange(N)  # the evenly spaced plot indices

    #Remaining Effort Line Regression
    #daily_effort_model = sm.OLS(np.array(burndown_df['daily_efforts'].tolist()) - int(burndown_df['daily_efforts'].tolist()[0]), ind)
    ind_xval = sm.add_constant(ind)
    daily_effort_model = sm.OLS(burndown_df['daily_efforts'].tolist(), ind_xval)
    daily_effort_results = daily_effort_model.fit().params
    #print('Daily Efforts Gradient111:', daily_effort_results)
    #daily_effort_regress_pts = [max(0, daily_effort_results[0]*i+int(burndown_df['daily_efforts'].tolist()[0])) for i in ind]
    daily_effort_regress_pts = [max(0, daily_effort_results[1]*i+daily_effort_results[0]) for i in ind]
    print('Daily Efforts Gradient:', daily_effort_results[1])
    burndown_remaining_gradient = daily_effort_results[1]

    #Ideal Effort Line Regression
    daily_ideal_slope, daily_ideal_intercept, daily_ideal_rval, daily_ideal_pval, daily_ideal_stderr = stats.linregress(ind, burndown_df['daily_ideals'])
    daily_ideal_regress_pts = [max(0, daily_ideal_slope*i+daily_ideal_intercept) for i in ind]
    print('Daily Ideals Gradient:', daily_ideal_slope)
    burndown_ideals_gradient = daily_ideal_slope

    #daily_ideal_model = sm.OLS(np.array(burndown_df['daily_ideals'].tolist()) - int(burndown_df['daily_ideals'].tolist()[0]), ind)
    #daily_ideal_results = daily_ideal_model.fit().params
    #daily_ideal_regress_pts = [max(0, daily_ideal_results[0]*i+int(burndown_df['daily_ideals'].tolist()[0])) for i in ind]
    #print('Daily Ideals Gradient:', daily_ideal_results[0])

    sns.set_style('darkgrid')
    sns.set_color_codes("bright")
    
    # multiple line plot
    fig, ax = plt.subplots()
    ax.set_position([0, 0, 1, 1])

    ax.plot( 'id', 'daily_efforts', data=burndown_df, marker='', color='m', linewidth=2, label="Remaining Efforts")
    ax.plot( ind, daily_effort_regress_pts, marker='', color='m', linestyle=':', linewidth=1, label="Remaining Efforts Trend")
    ax.plot( 'id', 'daily_ideals', data=burndown_df, marker='', color='pink', linewidth=2, label="Ideal Remaining Effort")
    ax.plot( ind, daily_ideal_regress_pts,  marker='', color='pink', linestyle=':', linewidth=2, label="Ideal Remaining Effort Trend")
    #ax.plot( ind, daily_ideal_regress_pts2,  marker='', color='pink', linestyle=':', linewidth=2, label="Ideal Remaining Effort Trend")
    ax.set_xticks(ind)
    #ax.set_yticks(np.arange(0, max(burndown_df['daily_efforts']), 2))
    ax.set_yticks(np.linspace(max(0, ax.get_ybound()[0]-5), ax.get_ybound()[1]+5, 15, dtype=np.int))
    ax.set_xticklabels(x_labels)

    #ax.set_title('Burndown Chart')
    ax.set_xlabel('Days')
    ax.set_ylabel('Remaining Efforts')


    ax2 = ax.twinx()

    ax2.bar(ind-0.15/2, burndown_df['daily_created'], width=0.15, color='b', label="Tasks Created")
    ax2.bar(ind+0.15/2, burndown_df['daily_completed'], width=0.15, color='y', label="Tasks Completed")

    ax2.plot( 'id', 'daily_tasks', data=burndown_df, marker='o', markerfacecolor='blue', markersize=4, color='skyblue', linestyle='dashed', linewidth=2, label='Remaining Tasks')
    #ax2.set_yticks(np.arange(0, max(burndown_df['daily_tasks']+2), 2))
    ax2.set_yticks(np.linspace(0, ax2.get_ybound()[1]+1, ax2.get_ybound()[1]+2, dtype=np.int))
    ax2.grid(None)
    ax2.set_ylabel('Remaining and Created/Completed Tasks')



    #fig.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    #fig.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    #fig.gca().xaxis.set_major_locator(mdates.DayLocator())

    fig.autofmt_xdate()

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc=0)

    #ax.set_xlim([0, len(ind)-1])
    #ax2.set_xlim([0, len(ind)-1])
    
    fig.set_size_inches(16.5, 10.5)

    figBytes = BytesIO()
    fig.savefig(figBytes, format='png', bbox_inches=0)
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    return figData

burndownChartImage = plotBurndownChart(burndown_df)


# In[ ]:




# In[ ]:

def getTasksDataFrame(inProgressBufferDays=0, attributes=[]):
    tasks = project.tasks
    tasks_data = []
    
    def getStartEndDate(task):
        def getCompletedTaskDate(task):
            startDate = task.DATE_ACTUAL_START_DATE
            endDate = task.DATE_ACTUAL_END_DATE
            if startDate == None:
                startDate = task.DATE_TASK_CREATED
            if endDate == None:
                endDate = task.getCompletedDate()
            return startDate, endDate
        
        def getInProgressTaskDate(task):
            startDate = task.DATE_EXPECTED_START_TASK
            endDate = task.DATE_EXPECTED_END_TASK
            if startDate == None:
                startDate = task.DATE_TASK_CREATED
            if endDate == None or endDate < datetime.datetime.now():
                endDate = datetime.datetime.now() + datetime.timedelta(days=inProgressBufferDays)
            return startDate, endDate
        
        def getOnHoldTaskDate(task):
            startDate, endDate = getInProgressTaskDate(task)
            endDate = task.DATE_TASK_MODIFIED
            return startDate, endDate
            
        return {
            TaskStatus.COMPLETED: getCompletedTaskDate(task),
            TaskStatus.ON_HOLD: getOnHoldTaskDate(task),
            TaskStatus.ARCHIVED: getOnHoldTaskDate(task)
        }.get(task.status, getInProgressTaskDate(task))
    
    for task in tasks:
        startDate, endDate = getStartEndDate(task)
        data = {
            'TASK_ID': task.TASK_ID, 
            'TASK_NUMBER': int(task.TASK_NUMBER), 
            'TASK_RESUME': task.TASK_RESUME, 
            'TASK_PRIORITY_NAME': task.TASK_PRIORITY_NAME,
            'DATE_EXPECTED_START_TASK': task.DATE_EXPECTED_START_TASK,
            'DATE_EXPECTED_END_TASK': task.DATE_EXPECTED_END_TASK,
            'DATE_ACTUAL_START_DATE': task.DATE_ACTUAL_START_DATE,
            'DATE_ACTUAL_END_DATE': task.DATE_ACTUAL_END_DATE,
            'DATE_TASK_CREATED': task.DATE_TASK_CREATED,
            'DATE_TASK_MODIFIED': task.DATE_TASK_MODIFIED,
            'START_DATE': startDate.date(),
            'END_DATE': endDate.date(),
            'PERCENTAGE_DONE': task.POURCENTAGE_DONE,
            'STATUS': task.status,
            'STATUS_LABEL': task.status.value
        }
        for attr in attributes:
            try:
                data[attr] = getattr(task, attr)
            except Exception:
                pass
            
        tasks_data.append(data)
    
    columns = [
        'TASK_ID', 
         'TASK_NUMBER', 
         'TASK_RESUME', 
         'TASK_PRIORITY_NAME', 
         'START_DATE',
         'END_DATE',
         'PERCENTAGE_DONE',
         'STATUS',
         'STATUS_LABEL'
    ]
    
    for attr in attributes:
        columns.append(attr)
    
    return pd.DataFrame(tasks_data, columns=columns)
    


# In[ ]:

gantt_df = getTasksDataFrame(inProgressBufferDays=0)
gantt_df


# In[ ]:

def convertCategoryAsResource(dataList):
    catList = []
    for cat in dataList:
        catList.append(cat)

    catList = list(set(catList))

    res = {}
    for cat in catList:
        res[cat] = gantt.Resource(cat)
    return res

def getTaskColour(task):
    return {
        TaskStatus.COMPLETED: '#EEEFDC',
        TaskStatus.ARCHIVED: '#EEEFC4',
        TaskStatus.READY_FOR_UAT: '#F9CC4F',
        TaskStatus.ON_HOLD: '#EAE2D7'
    }.get(task.STATUS, '#FFFC7A')

resStatuses = convertCategoryAsResource(gantt_df['STATUS_LABEL'])
resPriorities = convertCategoryAsResource(gantt_df['TASK_PRIORITY_NAME'])

projectChart = gantt.Project(name=project.projectName)
for idx, task in gantt_df.iterrows():
    color = None
    startDate = task.START_DATE
    endDate = task.END_DATE
        
    deltaDays = max(1, (endDate - startDate).days + 1 - num_of_weekends(startDate, endDate))
    #print(task.Summary, startDate, endDate, deltaDays, num_of_weekends(startDate, endDate))
    t = gantt.Task(task.TASK_RESUME, start=startDate, percent_done=100, duration=deltaDays, color=getTaskColour(task), resources=[resStatuses[task.STATUS_LABEL], resPriorities[task.TASK_PRIORITY_NAME]])
    projectChart.add_task(t)


# In[ ]:

gantt_filename = 'tmp_gantt2.svg'
gantt_startDate = datetime.datetime.now()-datetime.timedelta(days=GANTT_PAST_NUM_DAYS)
gantt_endDate = datetime.datetime.now()+datetime.timedelta(days=GANTT_FUTURE_NUM_DAYS)
projectChart.make_svg_for_tasks(filename=gantt_filename,
                     today=datetime.datetime.now().date(), start=gantt_startDate.date(), end=gantt_endDate.date())


# In[ ]:

gantt_base64Image = None
if CONVERT_SVG2PNG:
    import cloudconvert
    cloudconvert_api = cloudconvert.Api(CLOUDCONVERT_API_KEY)
    cloudconvert_process = cloudconvert_api.convert({
        "inputformat": "svg",
        "outputformat": "png",
        "input": "upload",
        "converteroptions": {
            "quality": "100"
        },
        "file": open(gantt_filename, 'rb')
    })
    cloudconvert_process.wait()
    gantt_convertedfilename = gantt_filename[0:-3]+'png'
    cloudconvert_process.download(gantt_convertedfilename)
    
    gantt_imagefile = open(gantt_convertedfilename, 'rb')
    gantt_base64Image = base64.b64encode(gantt_imagefile.read())

    try:
        os.remove(gantt_filename)
        os.remove(gantt_convertedfilename)
        print('Removed', gantt_filename, gantt_convertedfilename)
    except:
        print('Unable to remove one of:', gantt_filename, gantt_convertedfilename)


# In[ ]:




# In[ ]:

if NOTEBOOK_MODE is True:
    from IPython.core.display import display, HTML
    if CONVERT_SVG2PNG:
        display(HTML('<img src="data:image/jpg;base64, {}"/>'.format(gantt_base64Image.decode('utf8'))))

    display(HTML('<img src="{}" />'.format(gantt_filename)))


# In[ ]:




# In[ ]:

def plotPriorityChart(startDate, endDate):
    df = getTasksDataFrame(attributes=['DATE_TASK_CREATED'])
    df = df[df['DATE_TASK_CREATED'].dt.date >= startDate.date()][df['DATE_TASK_CREATED'].dt.date <= endDate.date()]
   
    f, ax = plt.subplots(figsize=(8, 8))
    priority_plot = sns.countplot(x='TASK_PRIORITY_NAME', data=df, palette="Set2");
    priority_plot.set(xlabel='Task Priority', ylabel='No. of Tasks')
    
        
    figBytes = BytesIO()
    f.savefig(figBytes, format='jpg')
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    return figData

priorityPlotStartDate = datetime.datetime.now()-datetime.timedelta(days=PLOT_PRIORITY_COUNT_LAST_NUM_DAYS)
priorityPlotEndDate = datetime.datetime.now()
priorityPlotImage = plotPriorityChart(priorityPlotStartDate, priorityPlotEndDate)


# In[ ]:

if NOTEBOOK_MODE is True:
    from IPython.core.display import display, HTML
    #display(HTML('<img src="data:image/jpg;base64, {}"/>'.format(statusPlotImage.decode('utf8'))))


# In[ ]:

def plotStatusChart():
    df = getTasksDataFrame(attributes=['DATE_TASK_CREATED'])
    df = df[df['STATUS'] != TaskStatus.COMPLETED]
    
    x_statuses = []
    y_taskcounts_low = []
    y_taskcounts_normal = []
    y_taskcounts_high = []
    y_taskcounts_urgent = []
    for status in TaskStatus:
        if status == TaskStatus.UNKNOWN or status == TaskStatus.COMPLETED or status == TaskStatus.ARCHIVED:
            continue
        x_statuses.append(status.value)
        y_taskcounts_low.append(len(df[df['STATUS'] == status][df['TASK_PRIORITY_NAME'] == 'Low']))
        y_taskcounts_normal.append(len(df[df['STATUS'] == status][df['TASK_PRIORITY_NAME'] == 'Normal']))
        y_taskcounts_high.append(len(df[df['STATUS'] == status][df['TASK_PRIORITY_NAME'] == 'High']))
        y_taskcounts_urgent.append(len(df[df['STATUS'] == status][df['TASK_PRIORITY_NAME'] == 'Urgent']))
    
    y_taskcounts_low = np.array(y_taskcounts_low)
    y_taskcounts_normal = np.array(y_taskcounts_normal) + y_taskcounts_low
    y_taskcounts_high = np.array(y_taskcounts_high) + y_taskcounts_normal
    y_taskcounts_urgent = np.array(y_taskcounts_urgent) + y_taskcounts_high

    for idx, count in reversed(list(enumerate(y_taskcounts_urgent))):
        if count == 0:
            try:
                y_taskcounts_low = np.delete(y_taskcounts_low, idx)
                y_taskcounts_normal = np.delete(y_taskcounts_normal, idx)
                y_taskcounts_high = np.delete(y_taskcounts_high, idx)
                y_taskcounts_urgent = np.delete(y_taskcounts_urgent, idx)
                x_statuses = np.delete(x_statuses, idx)
            except Exception as e:
                print(str(e))
    
    f, ax = plt.subplots(figsize=(8, 8))
    sns.set_color_codes("bright")
    sns.barplot(x=x_statuses, y=y_taskcounts_urgent, label="Urgent", color="#962B3D")
    sns.barplot(x=x_statuses, y=y_taskcounts_high, label="High", color="#E38B83")
    sns.barplot(x=x_statuses, y=y_taskcounts_normal, label="Normal", color="#9DBFD2")
    sns.barplot(x=x_statuses, y=y_taskcounts_low, label="Low", color="#C0BCD5")
    
    ax.legend(ncol=2, loc="upper left", frameon=True)
    ax.set(xlabel='Task Status', ylabel='No. of Tasks')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha='right')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    figBytes = BytesIO()
    f.savefig(figBytes, format='jpg')
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    return figData

    
statusPlotImage = plotStatusChart()


# In[ ]:

def plotPriorityDaysTaken(startDate, endDate):
    df = getTasksDataFrame(attributes=['DATE_TASK_CREATED'])
    df = df[df['DATE_TASK_CREATED'].dt.date >= startDate.date()][df['DATE_TASK_CREATED'].dt.date <= endDate.date()]
    df = df[df['STATUS'] == TaskStatus.COMPLETED]
    df['DAYS_TAKEN'] = pd.Series(((df['END_DATE'] - df['DATE_TASK_CREATED'].dt.date) + datetime.timedelta(days=1)).dt.days, index=df.index)
    f, ax = plt.subplots(figsize=(8, 8))
    sns.set_color_codes("deep")
    priority_days_plot = sns.swarmplot(x="TASK_PRIORITY_NAME", y="DAYS_TAKEN", data=df, palette="Set1")
    priority_days_plot.set(xlabel='Task Priority', ylabel='Days Taken to Complete Task')
    
    figBytes = BytesIO()
    f.savefig(figBytes, format='jpg')
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    return figData

priorityDaysPlotStartDate = datetime.datetime.now()-datetime.timedelta(days=PLOT_PRIORITY_DAYSTAKEN_LAST_NUM_DAYS)
priorityDaysPlotEndDate = datetime.datetime.now()
priorityDaysPlotImage = plotPriorityDaysTaken(priorityDaysPlotStartDate, priorityDaysPlotEndDate)


# In[ ]:

def plotTasksDayCreated(startDate, endDate):
    df = getTasksDataFrame(attributes=['DATE_TASK_CREATED'])
    df = df[df['DATE_TASK_CREATED'].dt.date >= startDate.date()][df['DATE_TASK_CREATED'].dt.date <= endDate.date()]
    df['DAY_CREATED'] = pd.to_datetime(df['DATE_TASK_CREATED']).dt.strftime('%A')
    f, ax = plt.subplots(figsize=(8, 8))
    sns.set_color_codes("deep")
    daycreated_plot = sns.countplot(x='DAY_CREATED', data=df, palette="Set2");
    daycreated_plot.set(xlabel='Task Created on Day', ylabel='No. of Tasks')
    
    figBytes = BytesIO()
    f.savefig(figBytes, format='jpg')
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    return figData

tasksDayCreatedPlotStartDate = datetime.datetime.now()-datetime.timedelta(days=PLOT_DAY_CREATED_LAST_NUM_DAYS)
tasksDayCreatedPlotEndDate = datetime.datetime.now()
tasksDayCreatedPlotImage = plotTasksDayCreated(tasksDayCreatedPlotStartDate, tasksDayCreatedPlotEndDate)


# In[ ]:

def plotProjectWordcloud(startDate, endDate):
    from bs4 import BeautifulSoup
    from wordcloud import WordCloud, STOPWORDS
    from PIL import Image
    import re
    import random

    fulltext = ''
    taskmembers = []
    
    df = getTasksDataFrame(attributes=['TASK_DESC_CREATOR', 'TASK_GROUP_NAME', 'TASK_TYPE_NAME', 'DATE_TASK_MODIFIED', 'ASSIGNED', 'REVIEWER'])
    df = df[df['DATE_TASK_MODIFIED'].dt.date >= startDate.date()][df['DATE_TASK_MODIFIED'].dt.date <= endDate.date()]
    for idx, task in df.iterrows():
        comments = [comment['NEW_VALUE'] + ' ' + task['TASK_RESUME'] for comment in project.getTaskObject(task['TASK_ID']).comments]
        comments_str = ' '.join(comments)
        tasktext = task['TASK_DESC_CREATOR'] + ' ' + task['TASK_RESUME'] + ' ' + comments_str + ' ' + task['TASK_GROUP_NAME'] + ' ' + task['TASK_TYPE_NAME']
        
        tasktext = BeautifulSoup(tasktext, 'lxml').text
        tasktext =  re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tasktext)
        #print('tasktext: ', tasktext)
        
        task_words = [word.strip() for word in tasktext.split()]
        fulltext = fulltext + ' ' + tasktext
        
        taskmembers.extend(task['ASSIGNED'])
        taskmembers.extend(task['REVIEWER'])

    #print(len(words))
    
    stopwords = set(STOPWORDS)
    f = open('stopwords.txt', 'r')
    other_stopwords = [word.strip() for word in f.readlines()]
    f.close()
    other_stopwords.extend(set(taskmembers))
    for word in other_stopwords:
        stopwords.add(word)

    mask = np.array(Image.open('cloudshape.jpg'))
    
    max_font_size = None
    if len(fulltext) < 1:
        fulltext = 'Nothing'
        max_font_size = 30
        
    wc = WordCloud(max_words=300, max_font_size=max_font_size, mask=mask, stopwords=stopwords, margin=10, random_state=10, background_color='white', colormap='tab10', collocations=True).generate(fulltext)
    
    f, ax = plt.subplots(figsize=(12, 8))
    plt.title('Topics between {0} and {1}'.format(startDate.strftime("%d %B %Y"), endDate.strftime("%d %B %Y")))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    
    figBytes = BytesIO()
    wc.to_image().save(figBytes, format='png')
    figBytes.seek(0)
    figData = base64.b64encode(figBytes.getvalue())
    
    return figData

plotProjectWordcloudStartDate = datetime.datetime.now()-datetime.timedelta(days=PLOT_WORDCLOUD_LAST_NUM_DAYS)
plotProjectWordcloudEndDate = datetime.datetime.now()
plotProjectWordcloudImage = plotProjectWordcloud(plotProjectWordcloudStartDate, plotProjectWordcloudEndDate)


# In[ ]:

report_df = getTasksDataFrame(attributes=['DATE_EXPECTED_END_TASK', 'ESTIMATED_TIME'])
uncompletedTasks_df = report_df[~report_df['STATUS'].isin(TaskStatus.getCompletedStatuses() + [TaskStatus.ON_HOLD])]
needToUpdateEstimatedEndDate = uncompletedTasks_df[uncompletedTasks_df['END_DATE'] <= datetime.datetime.now().date()]
needToUpdateEstimatedEffort = uncompletedTasks_df[uncompletedTasks_df['ESTIMATED_TIME'] <= 0.0]


# In[ ]:

for idx, task in needToUpdateEstimatedEndDate.iterrows():
    print(task['TASK_RESUME'])

needToUpdateEstimatedEndDate


# In[ ]:

for idx, task in needToUpdateEstimatedEffort.iterrows():
    print(task['TASK_RESUME'])


# In[ ]:

def getTasksPendingUatData(minDays=0):
    uatTasks_df = getTasksDataFrame(attributes=['DATE_TASK_MODIFIED'])
    uatTasks_df = uatTasks_df[uatTasks_df['STATUS'] == TaskStatus.READY_FOR_UAT]
    
    result = []
    for idx, task in uatTasks_df.iterrows():
        taskObj = project.getTaskObject(task['TASK_ID'])
        if taskObj == None:
            continue
        statusSinceDate = taskObj.getStatusSinceDate(task['STATUS'])
        daysAgo = (datetime.datetime.now() - statusSinceDate).days + 1
        taskName = 'Task #{0}: {1}'.format(task['TASK_NUMBER'], task['TASK_RESUME'])
        taskName = (taskName[:38] + '…') if len(taskName) > 38 else taskName
        if daysAgo >= minDays:
            pendingTask = {'taskName': taskName, 'taskStatus': task['STATUS_LABEL'], 'daysAgo': daysAgo}
            result.append(pendingTask)
            print(taskName, '\t', task['STATUS_LABEL'], '\t', daysAgo)
    return result

tasksPendingUat = getTasksPendingUatData(0)


# In[ ]:

createdSinceTasks_df = getTasksDataFrame(attributes=['DATE_TASK_CREATED'])
createdSinceTasks_df = createdSinceTasks_df[~createdSinceTasks_df['STATUS'].isin(TaskStatus.getCompletedStatuses() + [TaskStatus.ON_HOLD])]
for idx, task in createdSinceTasks_df.iterrows():
    taskObj = project.getTaskObject(task['TASK_ID'])
    if taskObj == None:
        continue
    daysAgo = (datetime.datetime.now() - task['DATE_TASK_CREATED']).days + 1
    print(task['TASK_RESUME'], '\t\t\t', task['STATUS_LABEL'], '\t', daysAgo)


# In[ ]:

import uuid
emailData = {
    'projectName': project.projectName,
    'totalEffortBurnt': sum(daily_relCompletedEffort),
    'effortCreationRate': sum(daily_relCreatedEffort) / total_workdays,
    'effortBurnVelocity': burndown_remaining_gradient,
    'expectedEffortBurnVelocity': burndown_ideals_gradient,
    'totalHeadCounts': project.numMembers,
    'effortPerDay': project.effortPerDay,
    'totalAvailableEffortResource': project.numMembers * project.effortPerDay * total_workdays,
    'expectedProficiency': project.expectedProficiency * 100.0,
    'expectedEffortToBurn': burndown_ideals_gradient * total_workdays,
    'expectedLinearEffortToBurn': project.dailyExpectedEffortToBurn * total_workdays,
    'effortEfficiencyRating': sum(daily_relCompletedEffort) / (project.dailyExpectedEffortToBurn * total_workdays) * 100.0,
    'ganttChartStartEndDate': [gantt_startDate, gantt_endDate, gantt_endDate - gantt_startDate],
    'burndownChartStartEndDate': [burndown_startDate, burndown_endDate, burndown_endDate - burndown_startDate],
    'priorityCountChartStartEndDate': [priorityPlotStartDate, priorityPlotEndDate, priorityPlotEndDate - priorityPlotStartDate],
    'priorityDaysTakenStartEndDate': [priorityDaysPlotStartDate, priorityDaysPlotEndDate, priorityDaysPlotEndDate - priorityDaysPlotStartDate],
    'tasksCreatedOnDayStartEndDate': [tasksDayCreatedPlotStartDate, tasksDayCreatedPlotEndDate, tasksDayCreatedPlotEndDate - tasksDayCreatedPlotStartDate],
    'tasksWordcloudStartEndDate': [plotProjectWordcloudStartDate, plotProjectWordcloudEndDate, plotProjectWordcloudEndDate - plotProjectWordcloudStartDate],
    'cidGanttChart': 'gantt-{}'.format(str(uuid.uuid4())),
    'cidBurndown': 'burndown-{}'.format(str(uuid.uuid4())),
    'cidStatusPriorityPlot': 'statusplot-{}'.format(str(uuid.uuid4())),
    'cidPriorityCountPlot': 'prioritycountplot-{}'.format(str(uuid.uuid4())),
    'cidDaysTakenPlot': 'daystakenplot-{}'.format(str(uuid.uuid4())),
    'cidDayCreatedPlot': 'daycreatedplot-{}'.format(str(uuid.uuid4())),
    'cidTasksWordcloud': 'taskswordcloudplot-{}'.format(str(uuid.uuid4())),
    'hideEffortChart': HIDE_EFFORTCHART,
    'pendingUatTasksMinDays': TASKS_PENDING_UAT_MIN_DAYS,
    'pendingUatTasks': tasksPendingUat,
    'currentDateTime': datetime.datetime.now(),
    'appVersion': APP_VERSION
}

pprint(emailData)


# In[ ]:




# In[ ]:

import emailhtml


# In[ ]:

emailHtmlBody = emailhtml.emailHtmlBody(emailData)


# In[ ]:

emailHtmlHeader = emailhtml.emailHtmlHeader()
emailHtmlFooter = emailhtml.emailHtmlFooter()

emailHtml = emailHtmlHeader + emailHtmlBody + emailHtmlFooter

emailHtml = emailHtml.replace('\n', '')


# In[ ]:




# In[ ]:

import sendgrid
from sendgrid.helpers.mail import *


# In[ ]:

if NOTEBOOK_MODE == True:
    raise ValueError('Breaking script before sending email...')


# In[ ]:

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
from_email = Email(EMAIL_SENDER_ADDR, EMAIL_SENDER_NAME)
subject = "[{}] Project Overview".format(project.projectName)
content = Content("text/html", emailHtml)

mail = Mail()

personalization = Personalization()
for email_addr in REPORT_RECIPIENTS:
    personalization.add_to(Email(email_addr))


mail.from_email = from_email
mail.subject = subject
mail.add_personalization(personalization)
mail.add_content(content)

attachment_gantt = Attachment()
if gantt_base64Image is None:
    attachment_gantt.content = ''
else:
    attachment_gantt.content = gantt_base64Image.decode('utf8')
attachment_gantt.type = "image/png"
attachment_gantt.filename = "gantt.png"
attachment_gantt.disposition = 'inline'
attachment_gantt.content_id = emailData['cidGanttChart']

attachment_burndown = Attachment()
attachment_burndown.content = burndownChartImage.decode('utf8')
attachment_burndown.type = "image/png"
attachment_burndown.filename = "burndown.png"
attachment_burndown.disposition = 'inline'
attachment_burndown.content_id = emailData['cidBurndown']

attachment_priorityplot = Attachment()
attachment_priorityplot.content = priorityPlotImage.decode('utf8')
attachment_priorityplot.type = "image/jpeg"
attachment_priorityplot.filename = "prioritycountplot.jpg"
attachment_priorityplot.disposition = 'inline'
attachment_priorityplot.content_id = emailData['cidPriorityCountPlot']

attachment_statusplot = Attachment()
attachment_statusplot.content = statusPlotImage.decode('utf8')
attachment_statusplot.type = "image/jpeg"
attachment_statusplot.filename = "statusplot.jpg"
attachment_statusplot.disposition = 'inline'
attachment_statusplot.content_id = emailData['cidStatusPriorityPlot']

attachment_prioritydaysplot = Attachment()
attachment_prioritydaysplot.content = priorityDaysPlotImage.decode('utf8')
attachment_prioritydaysplot.type = "image/jpeg"
attachment_prioritydaysplot.filename = "prioritydaysplot.jpg"
attachment_prioritydaysplot.disposition = 'inline'
attachment_prioritydaysplot.content_id = emailData['cidDaysTakenPlot']

attachment_tasksdaycreatedplot = Attachment()
attachment_tasksdaycreatedplot.content = tasksDayCreatedPlotImage.decode('utf8')
attachment_tasksdaycreatedplot.type = "image/jpeg"
attachment_tasksdaycreatedplot.filename = "tasksdaycreatedplot.jpg"
attachment_tasksdaycreatedplot.disposition = 'inline'
attachment_tasksdaycreatedplot.content_id = emailData['cidDayCreatedPlot']

attachment_taskswordcloudplot = Attachment()
attachment_taskswordcloudplot.content = plotProjectWordcloudImage.decode('utf8')
attachment_taskswordcloudplot.type = "image/png"
attachment_taskswordcloudplot.filename = "taskswordcloudplot.png"
attachment_taskswordcloudplot.disposition = 'inline'
attachment_taskswordcloudplot.content_id = emailData['cidTasksWordcloud']


mail.add_attachment(attachment_gantt)
mail.add_attachment(attachment_burndown)
mail.add_attachment(attachment_priorityplot)
mail.add_attachment(attachment_statusplot)
mail.add_attachment(attachment_prioritydaysplot)
mail.add_attachment(attachment_tasksdaycreatedplot)
mail.add_attachment(attachment_taskswordcloudplot)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

"""
for task in firstDateTasks:
    print(task.TASK_RESUME)
    
[task for task in secondDateTasks if task.TASK_ID not in [task2.TASK_ID for task2 in firstDateTasks]]
"""


# In[ ]:



