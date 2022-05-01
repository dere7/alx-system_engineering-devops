# Blogy outage incident report

Yesterday Blogy experienced an outage. In this post I'll provide an incident report that explores the details of the problem and how I solved it.

## Issue Summary
From 7:30AM to 8:15PM EAT Blogy experienced an outage. The users where unable to access blogs at a time. The service was down 100% due to the issue. The issue was caused by depolying of untested configuration of wordpress.

## Timeline (all times East Africa Time)

* 7:27 AM: The sites is deployed
* 7:30 AM: Outage begins
* 8:46 AM: Users alerted me of the issue
* 7:30 PM: Figured out the cause
* 7:53 PM: Pushed updated configuration
* 8:15 PM: The site is back online

## Root Cause

I added some configurations to my wordpress blog and mistyped php extentsion to `.phpp`. At 7:27 AM I pushed this untested code to github. Due to this issues the site responded with HTTP error code 500 for users.

## Resolution and recovery

After the issue brought to my attention I've tried to debug by using different tools like **strace**. I came to conclusion that there is error in settings. I corrected the error the sites live again

## Corrective and Preventative Measures

* Testing before deployement
* Using monitoring tools like datadog

![Memes](https://www.thecoderpedia.com/wp-content/uploads/2020/06/Programming-Jokes-Sudo-Linux-Lover-1024x1024.jpg?x78269)
by [Dereje Desta](https://github.com/dere7)
