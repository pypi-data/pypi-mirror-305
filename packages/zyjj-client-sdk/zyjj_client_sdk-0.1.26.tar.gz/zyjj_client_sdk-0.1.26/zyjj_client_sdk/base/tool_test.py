from zyjj_client_sdk.base.tool import llm_json_parse, async_batch_run
def test_json_parse():
    case1 = '{"age": 1}'
    case2 = """
    这里是一些文本
```json
{
    "key": "value",
    "number": 123,
    "list": [1, 2, 3],
    "nested": {
        "nested_key": "nested_value"
    }
}
```
"""
    case3 = '你好这个是 {"age": 1}'
    print(llm_json_parse(case1))
    print(llm_json_parse(case2))
    print(llm_json_parse(case3))


async def info(data: dict, age: int):
    print(data, age)
    if 2 in data:
        raise Exception('err')

def test_async_run():
    async_batch_run([1, 2, 3], info, split_size=2, args={'age': 1}, sleep=0, err_default=1)
