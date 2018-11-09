import allure

from Common import ParamManage, confighttp

failureException = AssertionError


def send_request(data, host, address, relevance):
    """
    再次封装请求
    :param data: 测试用例
    :param host: 测试地址
    :param address: 接口地址
    :param relevance: 关联对象
    :return:
    """
    if isinstance(data["headers"], dict):
        header = ParamManage.manage(data["headers"], relevance)  # 处理请求头
    else:
        raise failureException("请求头格式有误  %s" % data["headers"])
    if isinstance(data["parameter"], dict):
        parameter = ParamManage.manage(data["parameter"], relevance)  # 处理请求参数
    else:
        raise failureException("请求头格式有误  %s" % data["headers"])
    try:
        host = data["host"]
        address = data["address"]
    except KeyError:
        pass
    if data["request_type"] == 'post':
        if data["file"]:
            with allure.step("POST上传文件"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            result = confighttp.post(header=header,
                                     address=data["http_type"] + "://" + host + address,
                                     request_parameter_type=data["parameter_type"], files=parameter,
                                     timeout=data["timeout"])
        else:
            with allure.step("POST请求接口"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            result = confighttp.post(header=header, address=data["http_type"] + "://" + host + address,
                                     request_parameter_type=data["parameter_type"], data=parameter,
                                     timeout=data["timeout"])
    elif data["request_type"] == 'get':
        with allure.step("GET请求接口"):
            allure.attach("请求地址", data["http_type"] + "://" + host + address)
            allure.attach("请求头", str(header))
            allure.attach("请求参数", str(parameter))
        result = confighttp.get(header=header, address=data["http_type"] + "://" + host + address,
                                data=parameter, timeout=data["timeout"])
    elif data["request_type"] == "put":
        if data["file"]:
            with allure.step("PUT上传文件"):
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            result = confighttp.put(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"], files=parameter,
                                    timeout=data["timeout"])
        else:
            with allure.step("PUT请求接口"):
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            result = confighttp.put(header=header, address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"], data=parameter,
                                    timeout=data["timeout"])
    elif data["request_type"] == "delete":
        with allure.step("DELETE请求接口"):
            allure.attach("请求地址", data["http_type"] + "://" + host + address)
            allure.attach("请求头", str(header))
            allure.attach("请求参数", str(parameter))
        result = confighttp.delete(header=header, address=data["http_type"] + "://" + host + address,
                                   data=parameter, timeout=data["timeout"])
    else:
        return False, False
    return result
