from zyjj_client_sdk.base.tool import llm_json_parse
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


