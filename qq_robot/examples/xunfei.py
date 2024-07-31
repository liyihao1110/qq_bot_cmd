from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import json

# 星火认知大模型Spark Max的配置信息
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
with open('./examples/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    SPARKAI_APP_ID = config['appid']
    SPARKAI_API_KEY = config['key']
    SPARKAI_API_SECRET = config['secret']
SPARKAI_DOMAIN = 'generalv3.5'


def ifly(content):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=content
    )]
    handler = ChunkPrintHandler()
    result = spark.generate([messages], callbacks=[handler])

    # 提取回复文本
    if result and hasattr(result, 'generations') and result.generations:
        reply_text = result.generations[0][0].text
    else:
        reply_text = "No response from the model."

    return reply_text
