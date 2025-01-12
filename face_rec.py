import numpy as np
import pandas as pd
import cv2
from auth import authenticator
import redis
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity  
from datetime import datetime
from database.redis_client import save_attendance_log
from utils.sync_service import sync_redis_to_mongo
from datetime import datetime


# Load environment variables from .env file
load_dotenv()

# Retrieve Redis credentials from environment variables
hostname = os.getenv('REDIS_HOST')
portnumber = os.getenv('REDIS_PORT')
password = os.getenv('REDIS_PASSWORD')

# Establish Redis connection
try:
    r = redis.StrictRedis(
        host=hostname,
        port=portnumber,
        password=password
    )
    r.ping()
except redis.ConnectionError as e:
    print("Failed to connect to Redis:", e)
    exit(1)
if not hostname or not portnumber or not password:
    print("Missing Redis credentials in environment variables")
    exit(1)

# Function to retrieve data from Redis database
def retrive_data(name):
    # Retrieve dictionary from Redis
    retrive_dict = r.hgetall(name)
    if not retrive_dict:
        print(f"No data found for {name} in Redis.")
        return pd.DataFrame()  # Return an empty DataFrame if no data

    # Convert and process Redis data
    retrive_series = pd.Series(retrive_dict).apply(
        lambda x: np.frombuffer(x, dtype=np.float32)
    )
    retrive_series.index = [
        key.decode() if isinstance(key, bytes) else key for key in retrive_series.index
    ]

    # Prepare DataFrame
    retrive_df = retrive_series.to_frame().reset_index()
    retrive_df.columns = ['name_role', 'facial_features']
    retrive_df[['Name', 'Role']] = retrive_df['name_role'].str.split('@', expand=True)
    return retrive_df[['Name', 'Role', 'facial_features']]

# ... (rest of your script remains unchanged)



# configure face analysis
faceapp = FaceAnalysis(name='buffalo_sc',root='insightface_model', providers = ['CPUExecutionProvider'])
faceapp.prepare(ctx_id = 0, det_size=(640,640), det_thresh = 0.5)
try:
    faceapp = FaceAnalysis(
        name='buffalo_sc', 
        root='insightface_model', 
        providers=['CPUExecutionProvider']
    )
    faceapp.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.5)
except Exception as e:
    print(f"Error initializing FaceAnalysis: {e}")
    exit(1)

# ML Search Algorithm
def ml_search_algorithm(dataframe, feature_column, test_vector, 
                        name_role=['Name', 'Role'], thresh=0.5):
    """
    Cosine similarity-based search algorithm.
    """
    dataframe = dataframe.copy()
    x = np.asarray(dataframe[feature_column].tolist())

    # Calculate cosine similarity
    similar = cosine_similarity(x, test_vector.reshape(1, -1)).flatten()
    dataframe['cosine'] = similar

    # Filter matches by threshold
    data_filter = dataframe[dataframe['cosine'] >= thresh]
    if not data_filter.empty:
        best_match = data_filter.loc[data_filter['cosine'].idxmax()]
        return best_match[name_role[0]], best_match[name_role[1]]
    
    return 'Unknown', 'Unknown'                        name_role=['Name','Role'],thresh=0.5):
    """
    cosine similarity base search algorithm
    """
    # step-1: take the dataframe (collection of data)
    dataframe = dataframe.copy()
    # step-2: Index face embeding from the dataframe and convert into array
    X_list = dataframe[feature_column].tolist()
    x = np.asarray(X_list)
    
    # step-3: Cal. cosine similarity
    similar = pairwise.cosine_similarity(x,test_vector.reshape(1,-1))
    similar_arr = np.array(similar).flatten()
    dataframe['cosine'] = similar_arr

    # step-4: filter the data
    data_filter = dataframe.query(f'cosine >= {thresh}')
    if len(data_filter) > 0:
        # step-5: get the person name
        data_filter.reset_index(drop=True,inplace=True)
        argmax = data_filter['cosine'].argmax()
        person_name, person_role = data_filter.loc[argmax][name_role]
        
    else:
        person_name = 'Unknown'
        person_role = 'Unknown'
        
    return person_name, person_role

class RealTimePred:
    def saveLogs_redis(self):
        """Save logs to Redis and sync to MongoDB"""
        # Save current batch to Redis
        for name, role, timestamp in zip(
            self.logs['name'], 
            self.logs['role'],
            self.logs['current_time']
        ):
            if name != 'Unknown':
                save_attendance_log(name, role, timestamp)
        
        # Sync to MongoDB periodically
        sync_redis_to_mongo()
        
        # Reset logs
        self.reset_dict()

### Real Time Prediction
# we need to save logs for every 1 mins
class RealTimePred:
    def __init__(self):
        self.logs = dict(name=[],role=[],current_time=[])
        
    def reset_dict(self):
        self.logs = dict(name=[],role=[],current_time=[])
        
    def saveLogs_redis(self):
        # step-1: create a logs dataframe
        dataframe = pd.DataFrame(self.logs)        
        # step-2: drop the duplicate information (distinct name)
        dataframe.drop_duplicates('name',inplace=True) 
        # step-3: push data to redis database (list)
        # encode the data
        name_list = dataframe['name'].tolist()
        role_list = dataframe['role'].tolist()
        ctime_list = dataframe['current_time'].tolist()
        encoded_data = []
        for name, role, ctime in zip(name_list, role_list, ctime_list):
            if name != 'Unknown':
                concat_string = f"{name}@{role}@{ctime}"
                encoded_data.append(concat_string)
                
        if len(encoded_data) >0:
            r.lpush('attendance:logs',*encoded_data)
        
                    
        self.reset_dict()     
        
        
    def face_prediction(self,test_image, dataframe,feature_column,
                            name_role=['Name','Role'],thresh=0.5):
        # step-1: find the time
        current_time = str(datetime.now())
        
        # step-1: take the test image and apply to insight face
        results = faceapp.get(test_image)
        test_copy = test_image.copy()
        # step-2: use for loop and extract each embedding and pass to ml_search_algorithm

        for res in results:
            x1, y1, x2, y2 = res['bbox'].astype(int)
            embeddings = res['embedding']
            person_name, person_role = ml_search_algorithm(dataframe,
                                                        feature_column,
                                                        test_vector=embeddings,
                                                        name_role=name_role,
                                                        thresh=thresh)
            if person_name == 'Unknown':
                color =(0,0,255) # bgr
            else:
                color = (0,255,0)

            cv2.rectangle(test_copy,(x1,y1),(x2,y2),color)

            text_gen = person_name
            cv2.putText(test_copy,text_gen,(x1,y1),cv2.FONT_HERSHEY_DUPLEX,0.7,color,2)
            cv2.putText(test_copy,current_time,(x1,y2+10),cv2.FONT_HERSHEY_DUPLEX,0.7,color,2)
            # save info in logs dict
            self.logs['name'].append(person_name)
            self.logs['role'].append(person_role)
            self.logs['current_time'].append(current_time)
            

        return test_copy


#### Registration Form
class RegistrationForm:
    def __init__(self):
        self.sample = 0
    def reset(self):
        self.sample = 0
        
    def get_embedding(self,frame):
        # get results from insightface model
        results = faceapp.get(frame,max_num=1)
        embeddings = None
        for res in results:
            self.sample += 1
            x1, y1, x2, y2 = res['bbox'].astype(int)
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),1)
            # put text samples info
            text = f"samples = {self.sample}"
            cv2.putText(frame,text,(x1,y1),cv2.FONT_HERSHEY_DUPLEX,0.6,(255,255,0),2)
            
            # facial features
            embeddings = res['embedding']
            
        return frame, embeddings
    
def save_data_in_redis_db(self, name, role):
    if not name or name.strip() == '':
        return 'name_false'

    if 'face_embedding.txt' not in os.listdir():
        return 'file_false'

    try:
        x_array = np.loadtxt('face_embedding.txt', dtype=np.float32)
        received_samples = x_array.size // 512
        x_array = x_array.reshape(received_samples, 512)

        # Calculate mean embeddings
        x_mean = x_array.mean(axis=0).astype(np.float32)
        r.hset('academy:register', f"{name}@{role}", x_mean.tobytes())

        # Cleanup
        os.remove('face_embedding.txt')
        self.reset()
        return True
    except Exception as e:
        print(f"Error processing embeddings: {e}")
        return 'error'
        # validation name
        if name is not None:
            if name.strip() != '':
                key = f'{name}@{role}'
            else:
                return 'name_false'
        else:
            return 'name_false'
        
        if 'face_embedding.txt' not in os.listdir():
            return 'file_false'
        
        
        x_array = np.loadtxt('face_embedding.txt',dtype=np.float32) # flatten array            
        
        # step-2: convert into array (proper shape)
        received_samples = int(x_array.size/512)
        x_array = x_array.reshape(received_samples,512)
        x_array = np.asarray(x_array)       
        
        x_mean = x_array.mean(axis=0)
        x_mean = x_mean.astype(np.float32)
        x_mean_bytes = x_mean.tobytes()
        
        r.hset(name='academy:register',key=key,value=x_mean_bytes)
        
        
        os.remove('face_embedding.txt')
        self.reset()
        
        return True
    
    