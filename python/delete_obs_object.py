# 引入模块
from obs import ObsClient

# 创建ObsClient实例
obsClient = ObsClient(
    access_key_id='******',    
    secret_access_key='******',    
    server='https://obs.cn-north-4.myhuaweicloud.com'
)
# 使用访问OBS
# resp = obsClient.getBucketMetadata('dli-cn-north-4-aae035c879b649ac93c1b3738fb7d56d')
# print(resp)

resp = obsClient.getObjectMetadata('dli-cn-north-4-aae035c879b649ac93c1b3738fb7d56d', 'cat/3.png')
print(resp)

resp = obsClient.deleteObject('dli-cn-north-4-aae035c879b649ac93c1b3738fb7d56d', 'cat1/a/')
print(resp)

resp = obsClient.getObjectMetadata('dli-cn-north-4-aae035c879b649ac93c1b3738fb7d56d', 'cat1')
print(resp)

# 关闭obsClient
obsClient.close()