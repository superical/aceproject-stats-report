FROM python:3.5-slim

WORKDIR /usr/src/acereport

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --yes --force-yes \
      cron \
 && apt-get clean \
 && apt-get install gcc --yes --force-yes \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install python-gantt numpy pandas scipy statsmodels seaborn requests pillow sendgrid cloudconvert beautifulsoup4 wordcloud lxml

ENV ACEREPORT_ACC_ID                __VALUE_HERE__
ENV ACEREPORT_ACE_ID                __VALUE_HERE__
ENV ACEREPORT_ACE_PW                __VALUE_HERE__
ENV ACEREPORT_SENDGRID_API_KEY      __VALUE_HERE__
ENV ACEREPORT_CLOUDCONVERT_API_KEY  __VALUE_HERE__
ENV EMAIL_SENDER_NAME               __VALUE_HERE__
ENV EMAIL_SENDER_ADDR               __VALUE_HERE__
ENV ADMIN_EMAIL                     __VALUE_HERE__

RUN echo "Asia/Singapore" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

COPY . .

RUN printenv | grep -v "NO_PROXY" >> /etc/environment
RUN touch /var/log/cron-ss.log
RUN touch /var/log/cron-ph.log
RUN printf "15 9 * * 1 cd /usr/src/acereport && /usr/local/bin/python /usr/src/acereport/main.py --proj ## --targetprof 0.3 --headcount 5 --subject \"Project Weekly Overview\" --rcpts  >> /var/log/cron-ss.log 2>&1\n\
18 9 * * 1 cd /usr/src/acereport && /usr/local/bin/python /usr/src/acereport/main.py --proj ## --targetprof 0.3 --headcount 2 --subject \"Project Weekly Overview\" --rcpts  >> /var/log/cron-ph.log 2>&1\n\
30 9 1 * * cd /usr/src/acereport && /usr/local/bin/python /usr/src/acereport/main.py --proj ## --targetprof 0.3 --headcount 2 --hide-effortchart --PLOT_WORDCLOUD_LAST_NUM_DAYS 30 --subject \"Project Monthly Overview\" --rcpts  >> /var/log/cron-ph.log 2>&1\n" > cronfile

CMD service cron start \
    && crontab cronfile \
    && service cron restart \
    && tail -f /dev/null