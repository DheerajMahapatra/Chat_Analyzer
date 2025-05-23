# import re
# import pandas as pd

# def preprocess(data):
    
#     #Pattern in chart (Spliting DateTime and Msg)
#     pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s\w+\s-\s"
    
#     #All msgs we have
#     message = re.split(pattern, data)[1:]
    
#     #All date we have
#     dates = re.findall(pattern, data)
    
#     #Split Date and Time
#     date = []
#     times = []
    
#     for i in dates:
#         date.append(i.split(",")[0])
#         times.append(i.split(",")[1])
        
#     time = []
    
#     for i in times:
#         time.append(i.split("\u202f")[0])
        
#     #Create DataFrame
#     df = pd.DataFrame({
#         'user_msg':message,
#         'date':date,
#         'time':time
#     })
    
#     #Spliting user name and msg
#     user = []
#     msg = []
    
#     for i in df['user_msg']:
#         x = re.split("([\w\w]+?):\s",i)
#         if x[1:]:   #user name
#             user.append(x[1])
#             msg.append(x[2])
            
#         else:
#             user.append('Group Notification')
#             msg.append(x[0])
            
#     df['user'] = user
#     df['msg'] = msg
#     df.drop(columns = ['user_msg'], inplace = True)
    
#     #Convert Date Column into dateTime format
#     df['date'] = pd.to_datetime(df['date'])
#     #df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y", errors='coerce')
#     df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y, %I:%M %p")


#     df['year'] = df['date'].dt.year
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day_name()
    
#     return df






import re
import pandas as pd

def preprocess(data):
    
    # Pattern to split DateTime and Msg
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s\w+\s-\s"
    
    # All messages
    message = re.split(pattern, data)[1:]
    
    # All dates
    dates = re.findall(pattern, data)
    
    # Split Date and Time
    date = []
    times = []
    
    for i in dates:
        date.append(i.split(",")[0])
        times.append(i.split(",")[1].strip().split(" -")[0])
    
    # Combine Date and Time
    datetime = [d + " " + t for d, t in zip(date, times)]

    # Create DataFrame
    df = pd.DataFrame({
        'user_msg': message,
        'datetime': datetime
    })

    # Split user and message
    user = []
    msg = []
    
    for i in df['user_msg']:
        x = re.split("([\w\W]+?):\s", i)
        if x[1:]:
            user.append(x[1])
            msg.append(x[2])
        else:
            user.append('Group Notification')
            msg.append(x[0])
    
    df['user'] = user
    df['msg'] = msg
    df.drop(columns=['user_msg'], inplace=True)

    # Convert to datetime with specified format
    #df['datetime'] = pd.to_datetime(df['datetime'], format="%d/%m/%Y %I:%M %p")
    df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True)


    # Create additional columns
    df['date'] = df['datetime'].dt.date
    df['time'] = df['datetime'].dt.time
    df['year'] = df['datetime'].dt.year
    df['month'] = df['datetime'].dt.month_name()
    df['day'] = df['datetime'].dt.day_name()

    return df
