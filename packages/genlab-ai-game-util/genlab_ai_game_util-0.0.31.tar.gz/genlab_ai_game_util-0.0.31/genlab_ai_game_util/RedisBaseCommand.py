import json
import sys
import os
import time
import random
import glob

from genlab_ai_game_util import RedisClient

sys.stdout.reconfigure(line_buffering=True)


class RedisBaseCommand:

    def getAllTextMap(self):
        return self.allTextMap

    def __init__(self):

        # 使用glob读取当前目录下所有的.txt文件
        txt_files = glob.glob("*.txt")
        # 创建字典，将文件名作为key，文件内容作为value
        file_content_map = {}
        for file_name in txt_files:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                file_content_map[file_name] = content

        self.allTextMap = file_content_map

        # 获取所有环境变量
        env_vars = os.environ
        redis_env_string = os.getenv("redis")
        # 获取当前的 UNIX 时间戳
        current_time = time.time()

        self.inputFile = sys.argv[1]
        self.outputFile = sys.argv[2]
        self.redisKey = sys.argv[4]
        keep_seconds = int(sys.argv[5])
        keep_seconds += random.randint(0, keep_seconds // 5)
        self.finishTime = current_time + keep_seconds
        self.streamIdx = 0

        redis_env = json.loads(redis_env_string)
        redis_pw = redis_env['password']
        if redis_pw == "":
            redis_pw = None
        self.redisClient = RedisClient(host=redis_env['host'], port=redis_env['port'], password=redis_pw,
                                       socket_timeout=3,
                                       socket_connect_timeout=3)

        # # 输出所有环境变量
        # for key, value in env_vars.items():
        #     print(f'{key}: {value}')

    def command(self, input_json):
        return ''

    def pushStreamResult(self, streamResult):
        idx = self.streamIdx
        self.streamIdx = self.streamIdx + 1
        # 开始流
        result = {
            # 0代表运行成功
            'resultCode': 0,
            # 流方式
            'stream': True,
            'streamFinish': False,
            'streamIdx': self.streamIdx
        }
        with open(self.outputFile, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4)

        with open(self.outputFile + "_" + str(idx), 'w', encoding='utf-8') as file:
            json.dump(streamResult, file, indent=4)

    def run(self):
        # 获取当前进程ID
        current_pid = os.getpid()
        print(f"start python process {current_pid}")
        while True:
            try:
                current_time = time.time()
                if current_time > self.finishTime:
                    print("finish python process")
                    sys.exit(0)
                    return
                result = self.redisClient.bl_pop(self.redisKey, 1)
                if result['code'] != 0 or result['result'] is None:
                    continue
                print(f'blpop{result}')
                key, taskJson = result['result']
                if taskJson == None:
                    continue

                print(taskJson)
                redisJson = json.loads(taskJson)
                self.inputFile = redisJson['input']
                self.outputFile = redisJson['output']
                try:
                    with open(self.inputFile, 'r', encoding='utf-8') as file:
                        data = file.read()
                    # 入口参数
                    input_json = json.loads(data)
                    output_json = self.command(input_json)
                    # 如果使用了流的方式
                    if self.streamIdx > 0:
                        output_json = {
                            # 0代表运行成功
                            'resultCode': 0,
                            # 流方式
                            'stream': True,
                            'streamFinish': True,
                            'streamIdx': self.streamIdx
                        }
                    else:
                        result = {
                            # 0代表运行成功
                            'resultCode': 0,
                            # 非流方式
                            'stream': False,
                            # result会直接反馈给客户端
                            'result': output_json
                        }
                        output_json = result

                    with open(self.outputFile, 'w', encoding='utf-8') as file:
                        json.dump(output_json, file, indent=4)
                except Exception as e:
                    print(f"run python error :{e}")
                    result = {
                        # 0代表运行成功
                        'resultCode': -100,
                        # 非流方式
                        'stream': False
                    }
                    with open(self.outputFile, 'w', encoding='utf-8') as file:
                        json.dump(result, file, indent=4)

            except Exception as e:
                print(f"run python error :{e}")
