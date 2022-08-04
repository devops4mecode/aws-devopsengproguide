import boto3
import csv
from datetime import datetime
import os

codepipeline = boto3.client('codepipeline')

#Analyze payload from CloudWatch Event
def pipeline_execution(data):
    #print (data)
    pipelinename=data['detail']['pipeline']
    pipeline_execution_id=data['detail']['execution-id']
    pipeline_status=data['detail']['state']
    
    time= data['time']
    formatted_time_object = datetime.strptime(time,'%Y-%m-%dT%H:%M:%Sz')
    formatted_date = datetime.strftime(formatted_time_object,'%Y-%m-%d')
    day = formatted_time_object.day
    month_number = formatted_time_object.month
    datetime_object = datetime.strptime(str(month_number), "%m")
    year = formatted_time_object.year
    month_name = datetime_object.strftime("%B")+'-'+str(year)
    week_number_of_month = (day - 1) // 7 + 1
    weekday = formatted_time_object.isoweekday()
    current_pipeline=codepipeline.list_pipeline_executions(pipelineName=pipelinename,maxResults=1)
    pipeline_start_date=current_pipeline['pipelineExecutionSummaries'][0]['startTime']
    pipeline_end_date=current_pipeline['pipelineExecutionSummaries'][0]['lastUpdateTime']
    pipeline_start_time_in_sec=pipeline_start_date.timestamp()
    pipeline_end_time_in_sec=pipeline_end_date.timestamp()
    pipeline_duration=str(round((pipeline_end_time_in_sec-pipeline_start_time_in_sec) / 60,2))
    print(pipeline_duration)

    pipelinelist=[pipelinename,pipeline_execution_id,pipeline_status,pipeline_duration,formatted_date,year,month_name,day,weekday,week_number_of_month]
    stage_details=codepipeline.list_action_executions(pipelineName=pipelinename,filter={'pipelineExecutionId' : pipeline_execution_id})

    keys = len(stage_details['actionExecutionDetails'])
    print(keys)
    pipelinedict={"do4m_demo_pipeline":3,"SpringPetclinic":2,"do4m-angular-cal-pipeline":1}
    temp=0
    stagecounter=0
    stage_name='initial1'
    action_name='initial2'
    templist=[]
    while temp < keys:
      if (stage_name!=stage_details['actionExecutionDetails'][temp]['stageName']) and (action_name!=stage_details['actionExecutionDetails'][temp]['actionName']):
        stage_name=stage_details['actionExecutionDetails'][temp]['stageName']
        action_name=stage_details['actionExecutionDetails'][temp]['actionName']
        startTime_in_date=stage_details['actionExecutionDetails'][temp]['startTime']
        endTime_in_date=stage_details['actionExecutionDetails'][temp]['lastUpdateTime']
        startTime_in_sec=startTime_in_date.timestamp()
        endTime_in_sec=endTime_in_date.timestamp()
        status=stage_details['actionExecutionDetails'][temp]['status']
        duration_in_sec=endTime_in_sec-startTime_in_sec
        duration_in_min=round((duration_in_sec / 60),2)
        print(duration_in_min)
        stagecounter+=1
        print(stage_name,action_name,stagecounter)
        templist.append(status)
        templist.append(duration_in_min)
        print(templist)
      temp=temp+1
    templist.reverse()
    separator=(pipelinedict[pipelinename]-stagecounter) * 2
    while separator > 0:
      templist.append("")
      separator -= 1
    print(templist)
    pipelinelist.extend(templist)
    print(pipelinelist)
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('do4m-pipeline-report-sg')
    key = 'reports/pipeline.csv'
    # download s3 csv file to lambda tmp folder
    local_file_name = '/tmp/pipeline.csv'
    bucket.download_file(key,local_file_name)
    
    with open('/tmp/pipeline.csv','r') as infile:
        reader = list(csv.reader(infile))
        reader = reader[::-1] # the date is ascending order in file
        reader.insert(0,pipelinelist)
    with open('/tmp/pipeline.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in reversed(reader): # reverse order
            writer.writerow(line) 
            
    # upload file from tmp to s3 key
    bucket.upload_file('/tmp/pipeline.csv', key)
    
    return {
        'message': 'success!!'
    }

def lambda_handler(event, context):
    pipeline_execution(event)
