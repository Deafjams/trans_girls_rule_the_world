"""
Cronjob for trans girls bot
"""
import os
import plan
import trans_girls_rule_the_world

def trans_girls_cron():
    """
    Config for trans girls cron
    """
    cron = plan.Plan('trans_girls_rule_the_world')
    path = trans_girls_rule_the_world.__path__[0]
    environment = {
        'TRANS_GIRLS_CONSUMER_KEY': os.environ['TRANS_GIRLS_CONSUMER_KEY'],
        'TRANS_GIRLS_CONSUMER_SECRET': os.environ['TRANS_GIRLS_CONSUMER_SECRET'],
        'TRANS_GIRLS_OAUTH_TOKEN': os.environ['TRANS_GIRLS_OAUTH_TOKEN'],
        'TRANS_GIRLS_OAUTH_SECRET': os.environ['TRANS_GIRLS_OAUTH_SECRET']
    }

    cron.script(
        'rule.py', 
        every='3.minutes', 
        path=path,
        environment=environment
    )

    #update cron if crontab exists, write new cron if crontab doesn't exist
    try:
        cron.run('update')

    except plan.PlanError:
        cron.run('write')

if __name__ == '__main__':
    trans_girls_cron()
